
from googleapiclient.discovery import build  
import json  

# Your YouTube API Key  
YOUTUBE_API_KEY = 'youtue key'  



def get_youtube_video_categoryID():

    file_path = 'data/youtube_data.json'

    try:
        # Load the JSON data from the specified file  
        with open(file_path, 'r', encoding='utf-8') as json_file:  
            data = json.load(json_file)  

        # If the data is a list, we will extract the first element  
        if isinstance(data, list):  
            video_data = data[0]  # Access the first video if it's a list  
        else:  
            video_data = data  # Otherwise, treat it as a single object  
    

        video_category = video_data['category_id']
        return video_category


    except json.JSONDecodeError as e:  
        print("Error decoding JSON:", e)  
    except FileNotFoundError:  
        print(f"Error: The file '{file_path}' was not found.")  
    except Exception as e:  
        print("An error occurred:", e)  





def get_trending_videos(region_code='US', category_id=None, max_results=10):  
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)  
    
    try:  
        # Request to get the most popular (trending) videos  
        request = youtube.videos().list(  
            part='snippet,statistics',  
            chart='mostPopular',  
            regionCode=region_code,  
            maxResults=max_results  
        )  
        
        response = request.execute()  

        # Extract the video details  
        trending_videos = []  
        for item in response['items']:  
            video_info = {  
                'video_id': item['id'],  
                'title': item['snippet']['title'],  
                'description': item['snippet']['description'],  
                'published_at': item['snippet']['publishedAt'],  
                'channel_title': item['snippet']['channelTitle'],  
                'tags': item['snippet'].get('tags', []),  
                'view_count': int(item['statistics']['viewCount']),  
                'like_count': int(item['statistics'].get('likeCount', 0)),  
                'comment_count': int(item['statistics'].get('commentCount', 0)),  
                'category_id': item['snippet']['categoryId'],  
                'thumbnail_url': item['snippet']['thumbnails']['default']['url']  
            }  

            # Check if category_id is provided and if it matches the video's category  
            if category_id is None or video_info['category_id'] == category_id:  
                trending_videos.append(video_info)  
        
        # Write trending videos to a JSON file  
        with open('trending_data/trending_videos.json', 'w') as outfile:  
            json.dump(trending_videos, outfile, indent=4)  
        
        print(f"Trending videos saved to 'trending_videos.json'. Found {len(trending_videos)} videos.")  

    except Exception as e:  
        print(f"Error: {str(e)}")  
