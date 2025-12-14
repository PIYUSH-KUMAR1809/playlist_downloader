import yt_dlp
import argparse
from pathlib import Path

FORMAT_MAPPING = {
    'mp4': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'mp3': 'bestaudio/best',
    'm4a': 'bestaudio[ext=m4a]/best',
    'wav': 'bestaudio/best',
}

def get_best_quality_format(format_name='mp4'):
    return FORMAT_MAPPING.get(format_name, FORMAT_MAPPING['mp4'])

def setup_ydl_options(output_dir, browser=None, cookies_file=None, is_playlist=True, format_name='mp4'):
    # Set filename format based on whether it's a playlist or single video
    filename_format = '%(playlist_index)s-%(title)s.%(ext)s' if is_playlist else '%(title)s.%(ext)s'
    
    opts = {
        'format': get_best_quality_format(format_name),
        'outtmpl': str(Path(output_dir) / filename_format),
        'ignoreerrors': True,
        'nocheckcertificate': True,
        'no_warnings': False,
        'quiet': False,
        'extract_flat': False,
        'writethumbnail': False,
        'postprocessors': [{
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        }],
    }

    # Add audio conversion post-processor if needed
    if format_name in ['mp3', 'wav', 'm4a']:
        opts['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format_name,
            'preferredquality': '192',
        })
    
    if browser:
        opts['cookiesfrombrowser'] = (browser, None, None, None)
    
    if cookies_file:
        opts['cookiefile'] = cookies_file
        
    return opts

def download_content(url, output_dir='downloads', browser=None, cookies_file=None, single_video=False, format_name='mp4'):
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print(f"\nAnalyzing URL: {url}...")
    
    try:
        # First check if it's a playlist or single video
        check_opts = {
            'extract_flat': True, 
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'ignoreerrors': True
        }
        
        if single_video:
            check_opts['noplaylist'] = True
        
        is_playlist = False
        with yt_dlp.YoutubeDL(check_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if info and 'entries' in info and not single_video:
                is_playlist = True
                print(f"Detected Playlist: {info.get('title', 'Unknown')}")
            else:
                title = info.get('title', 'Unknown') if info else 'Unknown'
                print(f"Detected Single Video: {title}")

        # Configure yt-dlp options based on content type
        ydl_opts = setup_ydl_options(output_dir, browser, cookies_file, is_playlist, format_name)
        if single_video:
            ydl_opts['noplaylist'] = True
        
        # Download the content
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nDownloading to: {output_dir}\n")
            ydl.download([url])
            print("\nDownload completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Download Youtube videos or playlists in high quality')
    parser.add_argument('url', help='URL of the video or playlist')
    parser.add_argument('--output-dir', '-o', default='downloads',
                      help='Directory to save the downloaded videos (default: downloads)')
    parser.add_argument('--browser', '-b',
                      help='Browser to load cookies from (e.g. chrome, firefox, safari). Helps avoid 403 errors.')
    parser.add_argument('--cookies-file', '-c',
                      help='Path to a Netscape formatted cookies.txt file (reliable fallback if browser extraction fails).')
    parser.add_argument('--single-video', '-s', action='store_true',
                      help='Force download as a single video, even if the URL is a playlist')
    parser.add_argument('--format', '-f', default='mp4', choices=['mp4', 'mp3', 'm4a', 'wav'],
                      help='Download format (default: mp4). Options: mp4, mp3, m4a, wav')
    
    args = parser.parse_args()
    download_content(args.url, args.output_dir, args.browser, args.cookies_file, args.single_video, args.format)

if __name__ == '__main__':
    main()