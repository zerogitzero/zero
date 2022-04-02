print("Welcome to Costica Downloader and Converter ")
print("Loading...")

import pytube
import youtube_downloader
import file_converter

print('''
What do you want?

(1) Download YT Videos Manually
(2) Download a YT Playlist
(3) Download YT Videos and Convert Into MP3

Downloading copyrighted YT videos is illegal!
I am not responsible for your downloads! Go at your own risk!

''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Downloading...")
        filename = youtube_downloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
else:
    print("Invalid input! Terminating...")