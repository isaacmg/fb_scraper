# FBLYZE: a Facebook page and group scraping and analysis system.


[![Travis](https://travis-ci.org/isaacmg/fb_scraper.svg?branch=master)](https://travis-ci.org/isaacmg/fb_scraper)
[![Codecov branch](https://img.shields.io/codecov/c/github/isaacmg/fb_scraper.svg)](https://codecov.io/gh/isaacmg/fb_scraper)
[![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=isaacmg&repoName=fb_scraper&branch=master&pipelineName=fb_scraper&accountName=isaacmg&type=cf-2)]( https://g.codefresh.io/repositories/isaacmg/fb_scraper/builds?filter=trigger:build;branch:master;service:58e3576497ef5f0100e617c8~fb_scraper)
[![Join the chat at https://gitter.im/fb_scraper/Lobby](https://badges.gitter.im/fb_scraper/Lobby.svg)](https://gitter.im/fb_scraper/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Docker Pulls](https://img.shields.io/docker/pulls/paddlesoft/fb_scraper.svg)](https://hub.docker.com/r/paddlesoft/fb_scraper/)
[![Code Health](https://landscape.io/github/isaacmg/fb_scraper/master/landscape.svg?style=flat)](https://landscape.io/github/isaacmg/fb_scraper/master)


[Getting started tutorial on Medium](https://medium.com/@paddlesoft/building-a-full-service-facebook-scraping-and-analysis-engine-e6b5e45e3ea3).

The goal of this project is to implement a Facebook scraping and extraction engine. This project is originally based on the scraper from minimaxir which you can find [here](https://github.com/minimaxir/facebook-page-post-scraper). However, our project aims to take this one step further and create a continous scraping and processing system which can easily be deployed into production. Specifically, for our purposes we want to extract information about upcoming paddling meetups, event information, flow info, and other river related reports. However, this project should be useful for anyone who needs regular scrapping of FB pages or groups.

## Instructions

To get the ID of a Facebook group go [here](https://lookup-id.com) and input the url of the group you are trying to scrape. Pages you can just use after the slash (i.e. http://facebook.com/paddlesoft would be paddlesoft).

### Update we have switched to using a DB for recording information. Please see documentation for revised instructions. 

### Docker
We recommend you use our Docker images as it contains everything you need. For instructions on how to use our Dockerfile please see the [wiki page](https://github.com/isaacmg/fb_scraper/wiki/Docker-Image). Our Dockerfile is tested regularly on Codefresh so you can easily see if the build is passing above. 

### Running Locally

You will need to have Python 3.5+. If you want to use the examples (located in /data) you will need Jupyter Notebooks and Spark.

1. Create a file called app.txt and place your app_id in it along with your app_secret. Alternatively you can set this up in your system environment variables in a way similar to the way you would for Docker.
2. Use get_posts.py to pull data from a FB Group. So far we have provided five basic functions. Basically you can either do a full scrape or scrape from the last time stamp. You can also choose whether you want to write to a CSV or send the posts as Kafka messages. See get_posts.py for more details.
Example:
```python
from get_posts import scrape_comments_from_last_scrape, scrape_posts_from_last_scrape
group_id = "115285708497149"
scrape_posts_from_last_scrape(group_id)
scrape_comments_from_last_scrape(group_id)
```
3. Note that our messaging system using Kafka currently only works with the basic json data (comparable to the CSV). We are working on addeding a new schema for the more complex data [see issue 11](https://github.com/isaacmg/fb_scraper/issues/11).  Plans to upgrade to add authentication for Kafka authentication are in progress.

4. Currently the majority of examples of actual analysis are contained in the Examining data using Spark.ipynb notebook located in the data folder. You can open the notebook and specify the name of your CSV.

5. ElasticSearch is ocassionally throwing an authentication error when to trying to save posts. If you get an authentication error when using ES please add it to [issue 15](https://github.com/isaacmg/fb_scraper/issues/15). Ability to connect to Bonsai and elastic.co are in the works.

6. There are some other use case examples on my main GitHub page which you can look at as well. However, I have omitted them from this repo since they are mainly in Java and require Apache Flink.

7. We are also working on automating scraping with Apache Airflow. The dags we have created so far are in the dags folder. It is recomended that you use the dags in conjunction with our Docker image. This will avoid directory errors.


### Scrape away!
