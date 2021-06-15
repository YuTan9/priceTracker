#!/bin/bash
cd /home/pi/priceTracker
git pull
git checkout routineRun
if python priceTracker.py; then
	git add log.csv
	git commit -m "Price tracker auto update."
	git checkout routineRun
	git push origin routineRun
	git checkout master
	git merge routineRun
else
	echo "MyProtein price tracker running on raspberry pi crashed." | mail -s "Price Tracker Bug" s110095@shsh.tw
fi
git checkout master
