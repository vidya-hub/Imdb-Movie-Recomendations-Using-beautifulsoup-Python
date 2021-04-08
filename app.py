from bs4 import BeautifulSoup
import requests
import random


def get_descrtion(deslink):
    linkres = requests.get(deslink)
    linksoup = BeautifulSoup(linkres.content, 'html.parser')
    summarytext = (linksoup.find("body").find(id="wrapper")).find(
        id="root").find(id="pagecontent").find(id="content-2-wide").find(id="main_top").find("div",
                 {"class": "title-overview"}).find("div", {"class", "heroic-overview"}).find("div", {"class",
                    "plot_summary_wrapper"}).find("div", {"class", "plot_summary"}).find("div")
    return summarytext.text.strip()
res = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(res.content, 'html.parser')
body = soup.find("body", {"class", "fixed"})
article = ((body.find(id="wrapper").find(id="root")).find_all("div", {"class": "pagecontent"}))[
    2].find("div").find("div").find("div", {"class": "article"})
table = (article.find("span").find("div").find(
    "div").find("div", {"class": "lister"})).find("table")
table_list = table.find("tbody").find_all("tr")
total_movies_list = []


for movie_table in table_list:
    movie_rating_tag = movie_table.find(
        "td", {"class": "ratingColumn imdbRating"}).find("strong")
    movie_description_link ="https://www.imdb.com"+ movie_table.find(
        "td", {"class": "titleColumn"}).find("a")["href"]
    # movie_description = get_descrtion(movie_description_link)
    movie_title = movie_table.find(
        "td", {"class": "titleColumn"}).find("a").text
    user_rating = movie_rating_tag["title"]
    imdb_rating = movie_rating_tag.text
    total_movies_list.append(
        {"title": movie_title, "user ratings": user_rating, "imdb rating": imdb_rating, "description":movie_description_link,})
random_no = (random.randint(0, 249))
desc=get_descrtion(total_movies_list[random_no]["description"])
print(desc)
total_movies_list[random_no]["description"]= desc
print(total_movies_list[random_no])
