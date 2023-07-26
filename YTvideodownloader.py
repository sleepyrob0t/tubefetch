from pytube import YouTube
import re

def is_valid_youtube_url(url):
    # Regular expression pattern to match YouTube video URLs
    pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$"
    return re.match(pattern, url)

def download_youtube_video(url):
    try:
        # Create a YouTube object from the given URL
        yt = YouTube(url)
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        # Download the video
        video_stream.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the YouTube Video Downloader!")
    while True:
        video_url = input("Please enter a valid YouTube video URL (or 'exit' to quit): ")

        if video_url.lower() == "exit":
            break

        if is_valid_youtube_url(video_url):
            download_youtube_video(video_url)
        else:
            print("Invalid YouTube URL. Please try again.")

if __name__ == "__main__":
    main()