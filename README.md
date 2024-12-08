# Instagram Post Downloader

This project allows you to fetch Instagram posts from specific accounts within a specified time range (the last week). It downloads media (images/videos) and saves metadata (likes, captions, URLs) in an Excel sheet. 

## Features
- Fetch posts from multiple Instagram accounts.
- Download images and videos from Instagram posts.
- Save metadata (likes, captions, URLs) in an Excel file.
- Organize downloaded media in a separate directory.

## Requirements
Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `instaloader` for Instagram data scraping
- `openpyxl` for working with Excel files

### Installation
1. Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    ```
2. Navigate into the project directory:
    ```bash
    cd <repository-name>
    ```
3. Install the required dependencies:
    ```bash
    pip install instaloader openpyxl
    ```

## Setup
### Configure the Script
1. Open the `buzzz.py` file in a text editor.
2. Update the `accounts` list with the Instagram usernames you want to fetch posts from:
    ```python
    accounts = ["audiin", "bmwindia_official", "mercedesbenzind"]
    ```
3. By default, the script fetches posts from the last week, but you can modify the timeframe by adjusting the date filtering logic in the script.

### Login Credentials
To access data, you may need to log in using Instagram credentials. Replace `USERNAME` and `PASSWORD` in the script with your login details:
(use a public business dummy account only)
```python
loader.login("USERNAME", "PASSWORD")
```
## Usage

### Step 1: Run the Script
Execute the script by running the following command in your terminal:

```bash
python buzzz.py
```
Step 2: Fetch Data
The script will automatically fetch posts from the specified Instagram accounts within the last 7 days.

For each post:

Media files (images/videos) will be saved in the downloaded_media directory.
Post metadata (likes, captions, URLs) will be stored in the Excel file named instagram_posts_last_week_with_media.xlsx.
Example Output
The script will display progress for each account:

```bash
Fetching posts for @audiin from the last week (2024-12-01 to 2024-12-08)
Fetched: 2024-12-05 10:15:45, 120 likes, Media: Image, URL: https://www.instagram.com/p/abc123/
Media downloaded: downloaded_media/audiin/abc123.jpg
```

