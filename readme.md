# Facebook scraper and processer
[![Travis](https://travis-ci.org/isaacmg/fb_scraper.svg?branch=master)](https://travis-ci.org/isaacmg/fb_scraper)
[![Codecov branch](https://img.shields.io/codecov/c/github/isaacmg/fb_scraper.svg)]()

The goal of this project is to extract data from Facebook Posts (on pages and in groups) and then send it to Spark for analysis by NLP algorithms. For our purposes we want to extract information about upcoming paddling meetups, videos of rivers, flow info, and reports on streams. However, our solution should be generalizable to other datasets as well. In our setup data will then be combined with relevant data from Twitter, USGS, Instagram, and paddling message boards in order to provide targeted reccomendations to our users. Relevant information about rivers will be added to our PaddleSearch search engine for easy by our users searching later on. In the future we hope to utilize Facebook Webhooks in order to get the data in realtime, however this currently is not availible for groups. While this is primarily targeted to paddling we hope people will find this useful in fullfilling any data extraction/analysis task that uses the FB API.The scraper itself was orginally taken from the facebook-page-post-scraper by minimaxir which you can read about [here](https://github.com/minimaxir/acebook-page-post-scraper) for more information. 
## Instructions

To get the ID of a Facebook page or a group id go [here](https://lookup-id.com) and input the url of the page or group you are trying to scrape.

### You will need to have Python 3.5 installed along with Spark and Jupyter Notebooks.

1. Create a file called app.txt and place your app_id in it along with your app_secret.
2. Use fb_scrapper.py to pull data from a FB Group. You can either do this from whithin in it or by calling from your notebook (if you do choose this this way be sure to delete by test call at the bottom). To do this specify a group_id. Call scrape(group_id,0,func). The 0 parameter signifies your want to do a full scrape and not use the shelved file from the last scrape 
Example:
```python
from fb_scrapper import scrape_pages
group_id = "115285708497149"
full_scrape = 0
scraper_type = 0 
scrape_pages(group_id,full_scrape,scraper_type)
```
3. If you choose the first function (i.e 0) it will attempt to use Kafka to message scraping results in realtime AND write to the CSV. If you do not have Kafka use 1 instead and it will just generate the CSV.

4. Currently the bulk of the processing is being done from the Examining data using Spark.ipynb notebook. You can open the notebook and specify the name of your CSV (we are working on automating this).

5. Run through the notebook and make any changes/additions you want. We are currently working on adding an additional notebook (i.e. Streaming Data using Kafka + Spark Streaming.ipynb) which will include the use of Kafka and Spark streaming, however this is still very raw.
### Scrape away!
