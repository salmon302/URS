# settings.py

# Settings for the URS Comment Extractor

# Output file configuration
OUTPUT_FILE_NAME = 'reddit_comments.csv'  # Name of the output CSV file

# Reddit API credentials
REDDIT_CLIENT_ID = 'bS4MAjO-ctDRdr_v-wpkHg'
REDDIT_CLIENT_SECRET = '8R_d3oA2M0jr-_ZT7SQD9QQAyOfL5g'
REDDIT_USER_AGENT = 'URS Comment Extractor v1.0'

# Optional authentication - needed for private subreddits
# Leave as None if not needed
REDDIT_USERNAME = None
REDDIT_PASSWORD = None

# Script settings
MAX_RETRIES = 3  # Number of times to retry failed requests
BATCH_SIZE = 100  # Number of comments to process in each batch

# CSV Output Format
CSV_COLUMNS = [
    'Reddit title',
    'Comment Parent',
    'Subreddit',
    'Comment'
]