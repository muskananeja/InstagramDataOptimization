import instaloader
import openpyxl
from openpyxl.styles import Alignment
from datetime import datetime, timedelta
import os
import time

# Instagram accounts
accounts = ["audiin", "bmwindia_official", "mercedesbenzind"]

# Initialize Instaloader
L = instaloader.Instaloader()

# Timeframe for the last week
today = datetime.now()
one_week_ago = today - timedelta(days=7)

# Directory to store downloaded media
media_dir = "downloaded_media"
os.makedirs(media_dir, exist_ok=True)

# Excel file to store metadata
output_excel = "instagram_posts_last_week_with_media3.xlsx"

# Create a workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Instagram Posts"

# Write the header row
header = ["Username", "Post Date", "Likes", "Caption", "URL", "Media Type", "Media Path"]
sheet.append(header)

# Style the header row
for col in sheet.iter_cols(min_row=1, max_row=1, min_col=1, max_col=len(header)):
    for cell in col:
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Maximum posts to process from each account to avoid infinite loop
max_posts = 100

# Fetch posts for each account
for username in accounts:
    print(f"Fetching posts for @{username} from the last week ({one_week_ago.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')})")
    try:
        # Get profile
        profile = instaloader.Profile.from_username(L.context, username)

        processed_posts = 0  # Counter to track processed posts
        first_three_processed = 0  # Counter to track the first three posts processed

        for post in profile.get_posts():
            post_date = post.date

            # Process the first three posts regardless of timeframe
            if first_three_processed < 3:
                print(f"Processing post {first_three_processed + 1}: {post.shortcode}")
                first_three_processed += 1
            else:
                # Apply timeframe logic for the remaining posts
                if post_date < one_week_ago:
                    print(f"Post {post.shortcode} is outside the timeframe. Stopping.")
                    break

            # Process post details
            post_url = f"https://www.instagram.com/p/{post.shortcode}/"
            caption = post.caption[:100] if post.caption else "No caption"  # Truncate caption to 100 characters
            media_type = "Video" if post.is_video else "Image"

            # Construct file path for media
            media_path = os.path.join(media_dir, f"{username}_{post.shortcode}.{post.url.split('.')[-1]}")

            # Check if media already exists
            if os.path.exists(media_path):
                print(f"Media for post {post.shortcode} already exists, skipping download.")
                media_path = f"Media already downloaded: {media_path}"
            else:
                # Download media
                try:
                    L.download_post(post, target=f"{media_dir}/{username}")
                    print(f"Media downloaded: {media_path}")
                except Exception as e:
                    print(f"Error downloading media for post {post.shortcode}: {e}")
                    media_path = "Download Failed"

            # Append metadata to the sheet
            sheet.append([username, post_date.strftime('%Y-%m-%d %H:%M:%S'), post.likes, caption, post_url, media_type, media_path])
            print(f"Fetched: {post_date}, {post.likes} likes, Media: {media_type}, URL: {post_url}")

            processed_posts += 1  # Increment counter for processed posts

            # Stop processing after reaching the max_posts limit
            if processed_posts >= max_posts:
                print(f"Processed {max_posts} posts, stopping.")
                break

        time.sleep(20)  # Avoid rate limiting

    except Exception as e:
        print(f"Error fetching posts for @{username}: {e}")

# Save the workbook
wb.save(output_excel)
print(f"Data and media saved to '{output_excel}' and '{media_dir}'")
