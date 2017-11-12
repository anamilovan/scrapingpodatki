from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from profile import profile
import csv

csv_file = open("email_list.csv", "w+")

url = 'https://scrapebook22.appspot.com'
response = urlopen(url).read()
soup = BeautifulSoup(response)


for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_html = urlopen(url + link["href"]).read()
        person_soup = BeautifulSoup(person_html)
        profileData = person_soup.findAll("li")

        email = person_soup.find("span", attrs={"class": "email"}).string
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True}).string

        profil = profile(email, name, city)

        csv_file.write(profil.to_csv() + "\n")


csv_file.close()