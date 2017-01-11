# Facebook scraper and processer
The goal of this project is to extract data from FB Posts (on pages and in groups) and then send it to Spark for analysis by NLP algorithms. In particular we want to extract information about upcoming paddling meetups, videos of rivers, flow info (particularly for streams without gages), and reports on streams. Data will be combined with relevant data from Twitter, USGS, Instagram, and paddling message boards in order to provide targeted reccomendations to our users. After which relevant information about rivers will be added to PaddleSearch for easy by our users searching later on. In the future we hope to utilize Facebook Webhooks in order to get the data in realtime, however this currently is not availible for groups. While this is primarily targeted to paddling we hope people will find this useful in fullfilling any data extraction/analysis from FB task.
## Instructions 
### You will need to have Python 3.5 installed along with Spark and Jupyter Notebooks.
1. Create a file called app.txt and place your app_id in it along with your app_secret.
2. Use fb_scrapper.py to pull data from a FB Group. You can either do this from whithin in it or by calling from your notebook (if you do choose this this way be sure to delete by test call at the bottom). To do this specify a group_id. Call scrape(group_id,0,func). The 0 parameter signifies your want to do a full scrape and not use the shelved file from the last scrape 
Example:
```
from fb_scrapper import scrape_pages
group_id = "115285708497149"
full_scrape = 0
scraper_type = 0 
scrape_pages(group_id,full_scrape,scraper_type)
```
3. If you choose the first function (i.e 0) it will attempt to use Kafka to message scraping results in realtime AND write to the CSV. If you do not have Kafka use 1 instead and it will just generate the CSV.
4. Currently the bulk of the processing is being done from the Examining data using Spark.ipynb notebook. You can open the notebook and specify the name of your CSV (we are working on automating this).
5. Run through the notebook and make any changes/additions you want. We are currently working on adding an additional notebook which will include the use of Kafka and Spark streaming, however this is still very raw.
###### Scrape away!
