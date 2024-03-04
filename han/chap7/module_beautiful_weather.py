from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("city:",location.select_one("city").string)
    print("time:",location.select_one("tmEf").string)
    print("wether:",location.select_one("wf").string)
    print("min:",location.select_one("tmn").string)
    print("max:",location.select_one("tmx").string)