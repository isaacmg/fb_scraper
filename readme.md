# Facebook scraper and processer
[![Travis](https://travis-ci.org/isaacmg/fb_scraper.svg?branch=master)](https://travis-ci.org/isaacmg/fb_scraper)
[![Codecov branch](https://img.shields.io/codecov/c/github/isaacmg/fb_scraper.svg)]()
[![Code Health](https://landscape.io/github/isaacmg/fb_scraper/master/landscape.svg?style=flat)](https://landscape.io/github/isaacmg/fb_scraper/master)

The goal of this project is to implement a Facebook scraping and extraction engine. This project is originally based on the scraper from minimaxir which you can find [here](https://github.com/minimaxir/acebook-page-post-scraper). However, our project aims to take this one step further and create a continous scraping and processing system which can easily be deployed into production. Specfically, for our purposes we want to extract information about upcoming paddling meetups, event information, flow info, and other river related reports. However, this project should be useful for anyone who needs regular scrapping of FB pages or groups. 

## Instructions

To get the ID of a Facebook group go [here](https://lookup-id.com) and input the url of the page or group you are trying to scrape.

### You will need to have Python 3.5 installed along with Spark and Jupyter Notebooks.

1. Create a file called app.txt and place your app_id in it along with your app_secret.
2. Use get_posts.py to pull data from a FB Group. So far we have provided five basic functions. Basically you can either do a full scrape or scrape from the last time stamp. You can also choose whether you want to write to a CSV or send the posts as Kafka messages. See get_posts.py for more details.
Example:
```python
from get_posts import scrape_comments_from_last_scrape, scrape_posts_from_last_scrape
group_id = "115285708497149"
scrape_posts_from_last_scrape(group_id)
scrape_comments_from_last_scrape(group_id)
```
3. If you choose the first function (i.e 0) it will attempt to use Kafka to message scraping results in realtime AND write to the CSV. If you do not have Kafka use 1 instead and it will just generate the CSV.

4. Currently the bulk of the processing is being done from the Examining data using Spark.ipynb notebook. You can open the notebook and specify the name of your CSV (we are working on automating this).

5. Run through the notebook and make any changes/additions you want. We are currently working on adding an additional notebook (i.e. Streaming Data using Kafka + Spark Streaming.ipynb) which will include the use of Kafka and Spark streaming, however this is still very raw.
### Scrape away!
