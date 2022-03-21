from bs4 import BeautifulSoup
import requests

requested_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{requested_date}")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

song_list = soup.find_all(name='h3', class_='a-no-trucate')
artist_list = soup.find_all(name='span', class_='a-no-trucate')

songs = []
artists = []

for song in song_list:
    song_name = song.getText().strip('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')
    songs.append(song_name)

for artist in artist_list:
    artist_name = artist.getText().strip('\n\n\t\n\t\n\t\t\n\t\t\t\t\t')
    artists.append(artist_name)


numbered = 1
for element in range(100):
    print(f'{numbered}. {songs[element]} by {artists[element]}')
    numbered += 1