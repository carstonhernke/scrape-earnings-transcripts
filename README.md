# scrape-earnings-transcripts
A simple Python script for scraping earnings transcripts from [Seeking Alpha](https://seekingalpha.com/). *Use at your own risk.*

This script uses the excellent [requests](http://docs.python-requests.org/en/master/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) Python libraries. By default it pulls earnings transcrips for all companies, and saves them as .txt files named as _ticker_MONTH.DAY.YEAR.txt_. It should be easily modifiable to pull only transcripts for a specific company, or a specific date range. Using [NLTK](https://www.nltk.org/) for NLP and analysis would be a great next step.
