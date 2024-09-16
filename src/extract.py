
from datetime import datetime  
import json



def extract_and_analyze_trends(file_path):  
    try:  
        # Load the JSON data from the specified file  
        with open(file_path, 'r', encoding='utf-8') as json_file:  
            data = json.load(json_file)  

        # If the data is a list, we will extract the first element  
        if isinstance(data, list):  
            video_data = data[0]  # Access the first video if it's a list  
        else:  
            video_data = data  # Otherwise, treat it as a single object  

        # Extract relevant data  
        video_info = {  
            "video_id": video_data["video_id"],  
            "title": video_data["title"],  
            "description": video_data["description"],  
            "published_at": video_data["published_at"],  
            "channel_title": video_data["channel_title"],  
            "tags": video_data["tags"],  
            "view_count": video_data["view_count"],  
            "like_count": video_data["like_count"],  
            "comment_count": video_data["comment_count"],  
            "thumbnail_url": video_data["thumbnail_url"]  
        }  
 

        # Convert published_at to a more readable format  
        published_date = datetime.strptime(video_info["published_at"], "%Y-%m-%dT%H:%M:%SZ")  
        video_info["published_at"] = published_date.strftime("%B %d, %Y at %H:%M")  

       
        # Analyzing potential reasons for trending  
        engagement_ratio = (  
            (video_info["like_count"] + video_info["comment_count"]) / video_info["view_count"]  
        ) * 100  

        video_details = [  
            f"Video ID: {video_info['video_id']}\n"  
            f"Title: {video_info['title']}\n"  
            f"Description: {video_info.get('description', 'N/A')}\n"  
            f"Published At: {video_info['published_at']}\n"  
            f"Channel Title: {video_info['channel_title']}\n"  
            f"Tags: {', '.join(video_info['tags']) if video_info['tags'] else 'No Tags'}\n"  
            f"View Count: {video_info['view_count']}\n"  
            f"Like Count: {video_info['like_count']}\n"  
            f"Comment Count: {video_info['comment_count']}\n"  
            f"Thumbnail URL: {video_info['thumbnail_url']}\n"
            f"Engagement Ratio: {engagement_ratio:.2f}%"             
        ] 

        return(video_details) 

    except json.JSONDecodeError as e:  
        print("Error decoding JSON:", e)  
    except FileNotFoundError:  
        print(f"Error: The file '{file_path}' was not found.")  
    # except Exception as e:  
    #     print("An error occurred:", e)  





data_path = 'data/youtube_data.json'

extract_and_analyze_trends(data_path)