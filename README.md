# Price Tracker
An online shopping platform, My Protein, promotes on different holidays and seasons, and there were no data showing discount trends to determine if it was a good time to make a purchase. 
This application uses Beautiful Soup library and shell script to crawl, log, and render the data. 

# Execution
* Crawl the current discount

  `$> python priceTracker.py`
* Crawl and update to Github repo

  Make necessary changes to fit your configuration (repo url, commit message, branch name, etc.)

  `$> sh routineRun.sh`
* Setup crontab to run automatically

  `$> crontab -e`

  Then enter `0 0 * * * sh <routineRun.sh location>`
