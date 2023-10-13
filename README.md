# Working with APIs, JSONs, and AWS with Python
- Hello there! In this project I am using the spotify API in conjunction with the Twitter API to automate sharing my music and learn more about my music taste. After my object oriented design class, I wanted to branch out and become more comfortable with function oriented programs such as python, as well as my comfortability with JSON while learning how to use APIs. I further expanded upon this by moving this code to an AWS EC2 instance to automate the twitter bot and allow it to continuously run on the cloud.

# How to use the code
- Import the packages below in the terminal of your PC or IDE
- Set up a project in both the Spotify and Twitter APIs, and put your tokens and keys in their respective spots in the code
- First, uncomment the first four lines to generate your personal access token for Spotify, then paste it to its respective line in the program. These lines utilize the Spotipy library in a way that easily authorizes your personal spotify account with your app and all necessary API permissions. (The rest of the code works with the Spotify API directly for JSON/API practice).
- Then, select which feature you want to try out, and simply uncomment it from the main function! For the tweeting function, the current song function must be uncommented as well.

# Features
- Spotify should be open and playing a song for several of the features to work as intended
## Top Songs
- Using the function, generate a list of your top 10 songs on Spotify in different time ranges (1 month, 6 months, and all time).
## Top Songs of the Month Playlist Generator
- Generate a playlist on your spotify profile that holds your top 30 songs over the past month! Using an AWS EC2 instance, I was also able to run this code continuously and have this playlist be created on the first day of every month.
## Current Song
- Return the current song you are listening to, include song title, artist, and album.
## Next Song
- Skip to the next song in your queue on Spotify by simply running the line of code!
## Auto-Tweet Your Current Songs
- Used with a Twitter bot and Twitter APIs, a bot will tweet out what song you are listening to each time you play a new song. I was able to achieve this with an AWS EC2 instance to continuously run this code and check for updates to the current song every second.
