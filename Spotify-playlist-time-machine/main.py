import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth


endpoint = "https://www.billboard.com/charts/hot-100/"

date = input("Enter the date (YYYY-MM-DD) to get the Top 100 Songs list: ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(f"{endpoint}{date}", headers=header)
web_page = response.text

soup = bs4.BeautifulSoup(web_page, 'html.parser')
song_titles = soup.select("li ul li h3")
song_titles_list = [song.getText().strip() for song in song_titles]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ID",
                                               client_secret="SECRET",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="USERNAME"))
user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_uris = []

for song in song_titles_list:
    result = sp.search(q=f"track:{song} year:{year}", type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=create_playlist["id"], items=song_uris)

print(f"Top 100 Songs playlist for {date} has been created.")