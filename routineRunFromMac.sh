#!/bin/bash
cd ~/Desktop/priceTracker
git pull
git checkout routineRun
if python priceTracker.py 2>error.log; then
	git add log.csv
	git commit -m "Price tracker auto update."
	git push origin routineRun
	git checkout master
	git merge --no-edit routineRun
	git push
else
	ERRORMSG=$(cat error.log)
	echo "MyProtein price tracker running on raspberry pi crashed.\nError Message:\n $ERRORMSG" | mail -s "Price Tracker Bug" yutangutil@gmail.com
fi
git checkout master
