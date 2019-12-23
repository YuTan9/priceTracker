import requests
from bs4 import BeautifulSoup
import webbrowser
from datetime import date, datetime
import os

def main():
	today = date.today()
	# dd/mm/YY
	d1 = today.strftime("%Y%m%d")

	URL = 'https://www.myprotein.tw/voucher-codes.list'
	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.findAll("h2", {"class": "voucher-title"})
	day   = soup.findAll("div", {"class": "voucher-end-date"})
	msg   = soup.findAll("div", {"class": "voucher-message"})
	numbers = [d.text for d in title]
	# print(title)
	os.chdir("events")
	filename = "event" + d1 + ".html"
	f= open(filename,"w+")

	for i in range(len(numbers)):
		# print(items.getText().strip())
		f.write(title[i].prettify("UTF-8", formatter="html").replace("class=\"voucher-title\"", "class=\"voucher-title\" style=\"font-size:40pt; color: red\""))
		# f.write("<br>")
		f.write(day [i].prettify("UTF-8", formatter="html").replace("class=\"voucher-end-date no-timer\"", "class=\"voucher-end-date no-timer\" style=\"font-size:9pt\""))
		f.write(msg[i].prettify("UTF-8", formatter="html").replace("strong", "p style=\"font-size:12pt\""))
		f.write("<br><br><br><br>")

	cwd = os.getcwd()
	webbrowser.open("file://" + cwd + "/" + filename, new = 2)
	return

if __name__ == "__main__":
	main()
