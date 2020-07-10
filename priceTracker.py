import requests
from bs4 import BeautifulSoup
import webbrowser
from datetime import date, datetime
import os

def main():
	today = date.today()
	# dd/mm/YY
	d1 = today.strftime("%Y%m%d")

	URL = 'https://si.myprotein.com/voucher-codes.list'
	headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.findAll("h2", {"class": "voucher-title"})
	day   = soup.findAll("div", {"class": "voucher-end-date"})
	msg   = soup.findAll("div", {"class": "voucher-message"})
	numbers = [d.text for d in title]
	# print(title)

	for i in range(len(numbers)):
		print(title[i].text, '\n', msg[i].text)

	return

if __name__ == "__main__":
	main()
