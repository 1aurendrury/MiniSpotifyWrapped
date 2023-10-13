import json
import requests
import spotipy
from datetime import date
from spotipy.oauth2 import SpotifyOAuth
import tweepy
import time

# access token is unique and constantly changing (~ 1 hour) to each user
# find your token here and paste it below (https://developer.spotify.com/)
accessToken = "enter token here"

# the line below utilizes the spotipy library which helped with authenticating my API app and obtaining my device IDs
# scope covers all access needed for features to work as intended
sp = spotipy.Spotify(auth_manager=SpotifyOAuth('enter app id here', 'enter id here', scope='playlist-modify-public user-top-read user-read-currently-playing user-modify-playback-state user-read-playback-state user-read-recently-played', redirect_uri="enter local host here"))
# unique to each device you use spotify on, this is necessary to change songs, etc.
deviceID = 'enter your device ID here'

# keep these lines! running these upon open will give you a fresh token in cache and instantiate all further functions
# print(sp.user_playlist_create("user id goes here", "test"))
# the above line specifically will create a test playlist
# print(sp.playlist_add_items(sp.user_playlist_create("user id goes here", "test")['id'], ["spotify:track:track id goes here"], 0))
# print(sp.next_track())
# print(sp.currently_playing())



# print out the top tracks from the user's specified range
# short_term (1 month), medium_term (6 months), or long_term (all-time data)
def getTopTracks(token, timeRange):
    spotifyURL = f"https://api.spotify.com/v1/me/top/tracks?time_range={timeRange}&limit=10&offset=0"
    userData = requests.get(
        spotifyURL, headers= {
            "Authorization": f"Bearer {token}"
        }

    )
    jsonData = userData.json()

    tracks = [track for track in jsonData['items']]

    spot = 0
    for track in tracks:
        spot+=1
        song = track['name']
        artists = [artist for artist in track['artists']]
        artistsNames = ", ".join([artist['name'] for artist in artists])
        album = track['album']['name']
        print(f"{spot} - {song} by {artistsNames} from the album {album}")


# get the current track playing on your spotify account!
def getCurrentTrack():
    data = requests.get(
        currentlyPlayingURL,
        headers={
            "Authorization": f"Bearer {accessToken}"
        }

    )
    jsonStuff = data.json()
    title = jsonStuff['item']['name']
    artists = [artist for artist in jsonStuff['item']['artists']]
    artistNames = ", ".join([artist['name'] for artist in artists])
    id = jsonStuff['item']['id']
    info = {
        "id": id,
        "link": jsonStuff['item']['external_urls']['spotify'],
        "title": title,
        "artists": artistNames
    }
    return info
    # if you just want the currently playing text in console, use the code below
    # current implementation is made to work with the tweeting feature
    # return(f"Currently playing: {title} by {artistNames}. {jsonStuff['item']['external_urls']['spotify']}")

# code below was used to obtain device ID
# def deviceID(token):
#     print(sp.devices())
#     spotifyURL = f"https://api.spotify.com/v1/me/player/devices"
#     userData = requests.get(
#         spotifyURL, headers= {
#             "Authorization": f"Bearer {token}"
#         }
#
#     )
#     jsonData = userData.json()
#     print(jsonData)

# skip forward to the next song in your queue on spotify
def skipForward(token):
    userData = requests.post(
        'https://api.spotify.com/v1/me/player/next-deviceid goes here-', headers= {
            "Authorization": f"Bearer {accessToken}"
        }

    )

# creates a playlist in the user's account with their most played songs this month
def topSongsOfTheMonth(token):
    newPlaylistData = json.dumps({
        "name": f"Top Songs of the Month ({date.today().month}/{date.today().year})",
        "description": f"Songs of the Month ({date.today().month}/{date.today().year})",
        "public": True
    })
    createPlaylistRequest = requests.post(
        url='https://api.spotify.com/v1/users/-user id goes here-/playlists',
        data= newPlaylistData,
        headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {accessToken}"})

    id = createPlaylistRequest.json()['id']
    topSongsURL = "https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=25&offset=0"
    topSongsData = requests.get(
        url='https://api.spotify.com/v1/me/top/tracks?time_range=short_term&limit=25&offset=0',
        headers= {
            "Authorization": f"Bearer {accessToken}"
        }
    )
    topSongsJson = topSongsData.json()
    # print(topSongsData.json())
    tracks = [track for track in topSongsJson['items']]
    links = []
    for track in tracks:
        links.append(track['uri'])

    addSongsData = json.dumps({
        "uris": links,
        "position": 0
    })
    sendSongsRequest = requests.post(
        url=f'https://api.spotify.com/v1/playlists/{id}/tracks',
        data= addSongsData,
        headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {accessToken}"})



# space for the twitter api work


myAPI = tweepy.Client(bearer_token= 'token goes here',
                      access_token= 'token goes here',
                      access_token_secret= 'token secret goes here',
                      consumer_key= 'key goes here',
                      consumer_secret= 'secret goes here')

apiv2 = tweepy.OAuth1UserHandler('various',
                                 'keys and tokens',
                                 'go',
                                 'here')

# while code is running, automatically tweet out the currently playing song on spotify as songs change
def tweetCurrentSong():
    currentID = None
    while True:
        currentSong = getCurrentTrack()
        if currentID != currentSong['id']:
            link = currentSong['links']
            title = currentSong['title']
            artists = currentSong['artists']
            myAPI.create_tweet(text = f'Currently playing: {title} by {artists}. {link}')
            currentID = currentSong['id']
        time.sleep(2)

# main function where all capability is stored
def main():
    pass
    #getTopTracks(accessToken, "short_term")
    # getCurrentTrack()
    #skipForward(accessToken)
    #deviceID(accessToken)
    #topSongsOfTheMonth(accessToken)
    # tweetCurrentSong()


if __name__ == '__main__':
    main()

