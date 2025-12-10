import json
import csv
import argparse
from pathlib import Path
import sys
from datetime import datetime

def convert_to_csv(json_file, csv_file=None):
    """
    Converts a JSON file of YouTube comments to CSV.
    Handles both single video (list of comments) and playlist (list of videos with comments) formats.
    """
    input_path = Path(json_file)
    if not input_path.exists():
        print(f"Error: File not found: {json_file}")
        sys.exit(1)

    if not csv_file:
        csv_file = input_path.with_suffix('.csv')
    
    output_path = Path(csv_file)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)

    if not data:
        print("JSON file is empty.")
        return

    # Determine structure
    all_comments = []
    
    # Check if it's a playlist structure (list of videos) or single video (list of comments)
    is_playlist = False
    if isinstance(data, list) and len(data) > 0:
        first_item = data[0]
        if 'comments' in first_item and isinstance(first_item['comments'], list):
            is_playlist = True
    
    if is_playlist:
        print("Detected playlist structure.")
        for video in data:
            video_title = video.get('title', '')
            video_id = video.get('video_id', '')
            for comment in video.get('comments', []):
                comment['video_title'] = video_title
                comment['video_id'] = video_id
                all_comments.append(comment)
    else:
        print("Detected single video structure.")
        all_comments = data

    if not all_comments:
        print("No comments found to convert.")
        return

    # Define CSV columns
    # Common fields in yt-dlp comment output
    fieldnames = [
        'id', 'parent', 'author', 'author_id', 'text', 'like_count', 
        'timestamp', 'date', 'is_favorited', 'is_pinned', 'video_id', 'video_title'
    ]

    print(f"Converting {len(all_comments)} comments to CSV...")

    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            
            for comment in all_comments:
                # Add a readable date field if timestamp exists
                if 'timestamp' in comment and comment['timestamp']:
                    try:
                        dt = datetime.fromtimestamp(comment['timestamp'])
                        comment['date'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except (ValueError, TypeError):
                        comment['date'] = ''
                
                writer.writerow(comment)
                
        print(f"Successfully saved to: {output_path.absolute()}")

    except Exception as e:
        print(f"Error writing CSV: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert YouTube comments JSON to CSV')
    parser.add_argument('json_file', help='Input JSON file path')
    parser.add_argument('-o', '--output', help='Output CSV file path (optional)')
    
    args = parser.parse_args()
    
    convert_to_csv(args.json_file, args.output)

if __name__ == '__main__':
    main()
