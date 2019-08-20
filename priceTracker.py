import requests
from bs4 import BeautifulSoup
import webbrowser
from datetime import date

today = date.today()
# dd/mm/YY
d1 = today.strftime("%Y%m%d")

URL = 'https://www.myprotein.tw/voucher-codes.list'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.findAll("h2", {"class": "voucher-title"})
date  = soup.findAll("div", {"class": "voucher-end-date"})
msg   = soup.findAll("div", {"class": "voucher-message"})
numbers = [d.text for d in title]
# print(title)

filename = "event" + d1 + ".html"
f= open(filename,"w+")

for i in range(len(numbers)):
	# print(items.getText().strip())
	f.write(title[i].prettify(formatter="html").replace("class=\"voucher-title\"", "class=\"voucher-title\" style=\"font-size:40pt; color: red\""))
	# f.write("<br>")
	f.write(date[i].prettify(formatter="html").replace("class=\"voucher-end-date no-timer\"", "class=\"voucher-end-date no-timer\" style=\"font-size:9pt\""))
	f.write(msg[i].prettify(formatter="html").replace("strong", "p style=\"font-size:12pt\""))
	f.write("<br><br><br><br>")

webbrowser.open(filename, new = 2)