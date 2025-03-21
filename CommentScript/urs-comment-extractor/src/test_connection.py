import praw
from config.settings import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT
)

def test_connection():
    print("Testing Reddit API connection...")
    print(f"Client ID: {REDDIT_CLIENT_ID}")
    print(f"User Agent: {REDDIT_USER_AGENT}")
    
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        
        # Test by getting a known subreddit
        subreddit = reddit.subreddit("Awww")
        print(f"Successfully connected! Subreddit title: {subreddit.title}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    test_connection()