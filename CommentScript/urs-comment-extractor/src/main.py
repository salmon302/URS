import praw
import csv
import sys
import logging
import argparse
import traceback
from typing import List, Dict, Any
from prawcore.exceptions import PrawcoreException

# Direct credentials to avoid import issues
REDDIT_CLIENT_ID = 'bS4MAjO-ctDRdr_v-wpkHg'
REDDIT_CLIENT_SECRET = '8R_d3oA2M0jr-_ZT7SQD9QQAyOfL5g'
REDDIT_USER_AGENT = 'URS Comment Extractor v1.0'
OUTPUT_FILE_NAME = 'reddit_comments.csv'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)

def format_parent_id(comment_id: str, parent_id: str, comments_dict: Dict[str, Any]) -> str:
    """Format the parent comment text. Returns empty string if it's a top-level comment."""
    if not parent_id or parent_id.startswith('t3_'):  # t3_ prefix means it's the post itself
        return ''
    
    # Strip prefix t1_ from IDs
    parent_id = parent_id.replace('t1_', '')
    if parent_id in comments_dict:
        # Return truncated parent comment text
        if len(comments_dict[parent_id]) > 100:
            return comments_dict[parent_id][:97] + "..."
        return comments_dict[parent_id]
    return parent_id

def fetch_comments(reddit: praw.Reddit, post_url: str) -> List[Dict[str, Any]]:
    """Fetch comments from a Reddit post URL."""
    try:
        logging.info(f"\nFetching submission from URL: {post_url}")
        
        submission = reddit.submission(url=post_url)
        logging.info(f"Found submission: {submission.title}")
        logging.info(f"Loading {submission.num_comments} comments...")
        
        submission.comments.replace_more(limit=None)
        
        # First pass - collect all comments to build parent lookup
        logging.info("Building comment reference dictionary...")
        comments_dict = {}  # ID -> body mapping
        for comment in submission.comments.list():
            if hasattr(comment, 'id') and hasattr(comment, 'body'):
                comments_dict[comment.id] = comment.body
        
        # Second pass - build comment objects with formatted parent text
        logging.info("Processing comments and building relationships...")
        comments = []
        for comment in submission.comments.list():
            try:
                parent_text = format_parent_id(comment.id, comment.parent_id, comments_dict)
                comments.append({
                    'title': submission.title,
                    'parent': parent_text,
                    'subreddit': submission.subreddit.display_name,
                    'comment': comment.body
                })
            except AttributeError:
                # Skip malformed comments
                continue
        
        logging.info(f"Successfully processed {len(comments)} comments")
        return comments
        
    except PrawcoreException as e:
        logging.error(f"Error fetching comments from {post_url}: {str(e)}")
        return []

def init_reddit() -> praw.Reddit:
    """Initialize Reddit API client with proper error handling."""
    try:
        logging.info("Initializing Reddit API client...")
        
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        
        # Test the connection
        reddit.user.me()
        logging.info("Successfully connected to Reddit API")
        return reddit
        
    except Exception as e:
        logging.error(f"Error initializing Reddit client: {str(e)}")
        logging.error("Full error:")
        logging.error(traceback.format_exc())
        sys.exit(1)

def write_comments_to_csv(all_comments: List[Dict[str, Any]]) -> None:
    """Write comments to CSV file with proper error handling."""
    try:
        logging.info(f"\nWriting {len(all_comments)} comments to {OUTPUT_FILE_NAME}...")
        
        with open(OUTPUT_FILE_NAME, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['Reddit Title', 'Comment Parent', 'Subreddit', 'Comment']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for comment in all_comments:
                writer.writerow({
                    'Reddit Title': comment['title'],
                    'Comment Parent': comment['parent'],
                    'Subreddit': comment['subreddit'],
                    'Comment': comment['comment']
                })
                
        logging.info(f"Successfully wrote comments to {OUTPUT_FILE_NAME}")
        
    except IOError as e:
        logging.error(f"Error writing to CSV file: {str(e)}")
        logging.error("Full error:")
        logging.error(traceback.format_exc())
        sys.exit(1)

def main():
    try:
        parser = argparse.ArgumentParser(description='Reddit Comment Extractor')
        parser.add_argument('urls', nargs='+', help='Reddit post URLs to process')
        args = parser.parse_args()

        reddit = init_reddit()
        all_comments = []
        
        for url in args.urls:
            comments = fetch_comments(reddit, url)
            all_comments.extend(comments)
        
        if not all_comments:
            logging.error("No comments were collected. Exiting.")
            sys.exit(1)
            
        write_comments_to_csv(all_comments)
        
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        logging.error("Full error:")
        logging.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()