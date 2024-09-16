from src.extract import extract_and_analyze_trends
import google.generativeai as genai
import json



# Configure the Generative AI model
genai.configure(api_key="GEMINI_API_KEY")

# Paths to the video data files
data_path = 'data/youtube_data.json'  # Non-trending video data

trending_data_path = 'trending_data/trending_videos.json'  # Trending video data

# Analyze trends for both user video and trending video
users_video = extract_and_analyze_trends(data_path)
trending_video = extract_and_analyze_trends(trending_data_path)

# # Use Generative Model (Gemini)
model = genai.GenerativeModel("gemini-1.5-flash")

def respond():
    # Construct the prompt
    response = model.generate_content(
          f"""
        Provide the following information in html tags format do not add all the html templates
        if it is h1 just <h1><h1/> tag don't add some thing like body tag
        on every newline add <br> tag instead \n do not add (/n)
        the reponse should be one straihgt string:
        
        # Trending Video Analysis
        **Trending Video Analysis for {trending_video}**
        - **Title:** 
        - **Description:** 
        - **URL:** 
        - **Category:** 
        
        ## Analysis
        Analyze why this video is trending:
        - **Reasons:**
        1. High view count and engagement.
        2. Popular topic with broad appeal.
        3. Strong visual appeal.

        # User Video Analysis
        **User Video Analysis for {users_video}**
        - **Title:** 
        - **Description:** 
        - **URL:** 
        - **Category:**
        
        ## Analysis
        Analyze whether this video is trending or not:
        - **Trending Status:** Not Trending

        ## Improvement Suggestions
        - Optimize the title and description with relevant keywords.
        - Add a call to action to engage viewers.
        - Promote the video on social media platforms.
        """
    )
    
    # Return the generated HTML text
    print(response.text)
    return response.text
