def format_comments_to_csv(comments, reddit_title, subreddit, output_file):
    import csv

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Reddit Title', 'Comment Parent', 'Subreddit', 'Comment'])

        for comment in comments:
            parent_comment = comment.parent_id if hasattr(comment, 'parent_id') else ''
            writer.writerow([reddit_title, parent_comment, subreddit, comment.body])