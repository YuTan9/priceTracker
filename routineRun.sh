#!/bin/bash
if python priceTracker.py; then
	git add log.csv discount.png
	git commit -m "Price tracker auto update."
	git push origin master
else
	echo "MyProtein price tracker running on raspberry pi crashed." | mail -s "Price Tracker Bug" s110095@shsh.tw
fi