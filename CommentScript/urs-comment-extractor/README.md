# README for URS Comment Extractor

## Overview

The URS Comment Extractor is a Python script that utilizes the Universal Reddit Scraper to extract comments from specified Reddit posts and outputs them in a structured CSV format. This tool is designed for users who want to analyze comments from Reddit posts efficiently.

## Features

- Input Reddit post URLs to fetch comments.
- Outputs comments in a CSV format with the following structure:
  - Reddit Title
  - Comment Parent (if the comment is a reply, may be blank)
  - Subreddit
  - Comment

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.x
- Universal Reddit Scraper
- pandas (for handling CSV operations)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/urs-comment-extractor.git
   cd urs-comment-extractor
   ```

2. Run the main script:

   ```bash
   python src/main.py
   ```

3. Follow the prompts to input the Reddit post URLs from which you want to extract comments.

4. The comments will be saved in a CSV file in the specified format.

## Example

After running the script and providing the necessary Reddit post URLs, you will receive a CSV file with the extracted comments structured as follows:

| Reddit Title | Comment Parent | Subreddit | Comment |
|--------------|----------------|-----------|---------|
| Example Title | Parent Comment | r/example | This is a comment. |

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.