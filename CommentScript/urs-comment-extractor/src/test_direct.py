import praw
import sys

# Direct credentials without importing
REDDIT_CLIENT_ID = 'bS4MAjO-ctDRdr_v-wpkHg'
REDDIT_CLIENT_SECRET = '8R_d3oA2M0jr-_ZT7SQD9QQAyOfL5g'
REDDIT_USER_AGENT = 'URS Comment Extractor v1.0'

def main():
    sys.stdout.write("Starting test...\n")
    sys.stdout.flush()
    
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        
        # Test by getting info from one submission
        url = "https://old.reddit.com/r/Awww/comments/1jfx2l4/what_an_elegant_moustache_sir/"
        submission = reddit.submission(url=url)
        
        sys.stdout.write(f"Title: {submission.title}\n")
        sys.stdout.write(f"Subreddit: {submission.subreddit.display_name}\n")
        sys.stdout.write(f"Number of comments: {submission.num_comments}\n")
        sys.stdout.flush()
        
    except Exception as e:
        sys.stdout.write(f"Error: {str(e)}\n")
        sys.stdout.write("".join(format_exception(*sys.exc_info())))
        sys.stdout.flush()
        sys.exit(1)

if __name__ == "__main__":
    main()