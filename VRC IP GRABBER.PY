import os

def extract_video_id(youtube_url):
    if 'watch?v=' in youtube_url:
        video_id_start_index = youtube_url.index('watch?v=') + len('watch?v=')
        video_id = youtube_url[video_id_start_index:]
        if '&' in video_id:
            video_id = video_id[:video_id.index('&')]
        return video_id
    else:
        return None

# Function to check if terminal size is adequate
def check_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.lines, size.columns
    except Exception as e:
        print(f"Error checking terminal size: {e}")
        return 0, 0

# Function to display help information
def display_help():
    help_text = """
    This program extracts the VIDEO_ID from a YouTube URL and generates a CDNApp URL based on it.
    
    How to use:
    - Enter a valid YouTube URL containing 'watch?v='.
    - The program will extract the VIDEO_ID and display a CDNApp URL.
    - Type 'help' to display this help information again.
    
    Requirements:
    - Please ensure your terminal is fullscreen for optimal display.
    
    For support, visit:
    - GitHub: https://github.com/fallpy/fallpy
    
    For community discussions, join us on Discord:
    - Discord: https://discord.gg/E27sGgAGjQ
    """
    print(help_text)

# Check if the terminal is fullscreen
rows, columns = check_terminal_size()
if rows < 40 or columns < 100:
    print("Please fullscreen your terminal window for optimal display.")
    input("Press Enter to continue...")

print("  _____   _____   ______   _____  ______  _   _  _______  ______  _____    ____ __     __  ______        _       _          _____ __     __  ")
print(" |  __ \ |  __ \ |  ____| / ____||  ____|| \ | ||__   __||  ____||  __ \  |  _ \\ \   / / |  ____|/\    | |     | |        |  __ \\ \   / /  ")
print(" | |__) || |__) || |__   | (___  | |__   |  \| |   | |   | |__   | |  | | | |_) |\ \_/ /  | |__  /  \   | |     | |        | |__) |\ \_/ /   ")
print(" |  ___/ |  _  / |  __|   \___ \ |  __|  | . ` |   | |   |  __|  | |  | | |  _ <  \   /   |  __|/ /\ \  | |     | |        |  ___/  \   /    ")
print(" | |     | | \ \ | |____  ____) || |____ | |\  |   | |   | |____ | |__| | | |_) |  | |    | |  / ____ \ | |____ | |____  _ | |       | |     ")
print(" |_|     |_|  \_\|______||_____/ |______||_| \_|   |_|   |______||_____/  |____/   |_|    |_| /_/    \_\|______||______|(_)|_|       |_|     ")

print(" https://github.com/fallpy/fallpy/blob/main/LISCENCE ")
print(" https://discord.gg/E27sGgAGjQ ")

while True:
    youtube_url = input("\nPlease enter a YouTube URL (or type 'exit' to quit): ")

    if youtube_url.lower() == 'exit':
        print("Exiting program.")
        break
    elif youtube_url.lower() == 'help':
        display_help()
        continue

    video_id = extract_video_id(youtube_url)

    if video_id:
        cdnapp_url = f"https://cdnapp.de/watch?v={video_id}"
        print(f"The CDNApp URL with the extracted VIDEO_ID is: {cdnapp_url}")
    else:
        print("Invalid YouTube URL format. Please provide a URL with 'watch?v='.")
