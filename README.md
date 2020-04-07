# GoodreadQuotesScraper
Web spider for crawling goodread quotes using Scrapy.
![](https://github.com/wilsoncwj/GoodreadQuotesScraper/blob/master/screenshots/website.png?raw=true)

## Installing Scrapy and virtual environment
`pip install scrapy`

`pip install pipenv`

## Running the scraper
Activate virtual environment using `source ./bin/activate`

Within the Scrapy virtual environment, run the following command
`scrapy crawl quotes`

## Fields of interest
- quote
- author
- number of likes
- image url (if any)
- tags
