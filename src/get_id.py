import re

def get_youtube_video_id(url):
    # Define a regex pattern to extract video ID from different YouTube URL formats
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None
