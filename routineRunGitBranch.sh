#!/bin/bash
cd /home/pi/priceTracker
git pull
if python priceTracker.py; then
	git checkout -b routineRun
	git add log.csv discount.png
	git commit -m "Price tracker auto update."
	git push origin routineRun
	git checkout master
	git merge routineRun
else
	echo "MyProtein price tracker running on raspberry pi crashed." | mail -s "Price Tracker Bug" s110095@shsh.tw
fi
