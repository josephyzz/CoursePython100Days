import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
movies = movies_titles[::-1]

with open("movies.txt", "a") as file:
    for movie in movies:
        file.write("%s\n" % movie)
