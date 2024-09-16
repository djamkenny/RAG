import os
from src.utils import load_data #to load our data
from src.preprocess import preprocess_data 

# from src.analyze import analyze_data

from src.get_datayou import  get_youtube_video
from src.get_id import get_youtube_video_id
from src.trending import  get_youtube_video_categoryID, get_trending_videos

def get_user_info(url, code):

     # Take YouTube URL as input
    youtube_url = url

    # Extract video ID
    video_id = get_youtube_video_id(youtube_url)

    # Check if video ID is found and print it
    if video_id:
    
         get_youtube_video(video_id)
    else:
        print("Invalid YouTube URL or video ID not found")


    # Input for region code and category ID  
    region_code = code
    # category_id = input("Enter the YouTube category ID to filter trending videos (or leave blank for all categories): ")  
    category_id = get_youtube_video_categoryID()


    # Call the function to get trending videos  
    get_trending_videos(region_code, category_id if category_id else None)  

# url = input("Enter a YouTube URL: ")

# code = get_youtube_video_id(url)

# get_user_info(url, code)