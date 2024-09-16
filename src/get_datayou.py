from googleapiclient.discovery import build
from src.get_id import get_youtube_video_id
import json

YOUTUBE_API_KEY = 'your tube key'  # Your API key

def extract_video_details(data):
    video_details = []
    for item in data['items']:
        video_info = {
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'published_at': item['snippet']['publishedAt'],
            'channel_title': item['snippet']['channelTitle'],
            'tags': item['snippet'].get('tags', []),
            'view_count': int(item['statistics']['viewCount']),
            'like_count': int(item['statistics']['likeCount']),
            'comment_count': int(item['statistics']['commentCount']),
            'category_id': item['snippet']['categoryId'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url']
        }
        video_details.append(video_info)
    return video_details

def get_youtube_video(video_id):  
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)  

    try:  
        youtube_request = youtube.videos().list(part='snippet,statistics', id=video_id)  
        response = youtube_request.execute()  

        video_details = extract_video_details(response)

        # Write video details to a JSON file
        with open(f'data/youtube_data.json', 'w') as outfile:
            json.dump(video_details, outfile, indent=4)
        
        print("Video details saved succesfully")

    except Exception as e:  
        print(f"Error: {str(e)}")

# Hardcode the video ID
if __name__ == '__main__':
    # Take YouTube URL as input
    youtube_url = input("Enter a YouTube URL: ")

    # Extract video ID
    video_id = get_youtube_video_id(youtube_url)

    # Check if video ID is found and print it
    if video_id:
         get_youtube_video(video_id)
    else:
        print("Invalid YouTube URL or video ID not found")
