import shelve
from fb_posts import FB_SCRAPE
from pg_db import save_scrape_PS
import psycopg2
import time
import os

#import fb_pages
# Function to scrape with.
# Call with group id and whether you want to scrape all the way back 0 or since last scrape 1.
# To do: allow passing of an array of groups, allow passing of a custom scrape date, add functions for scraping of pages
# To do create unit tests to make sure it runs.
def scrape_groups_pages(page_id, from_time, useKafka, useES):
    scrape(page_id, from_time, useKafka, useES)
    return "Sucessfully scraped from " + str(from_time) + "for page id " + str(page_id)

# Get to time scrape from
def get_tstamp(page_id, tstamp ,path):
    if tstamp is 1:
        with shelve.open(path) as d:
            if page_id in d:
                time_opened = d[page_id]
                pageStamp = str(time_opened)
                print("Scraping since unix time " + pageStamp)
            else:
                print("key not found in dict proceeding with full scrape")
                pageStamp = -2180131200

    elif tstamp is 0:
        pageStamp = -2180131200
    else:
        pageStamp=tstamp
    return pageStamp

# Save the time the last time page was scraped
def save_shelve(page_id, path):
    timestamp = int(time.time())
    save_scrape_PS(page_id,timestamp, 123031, 30)
    d = shelve.open(path)
    d[page_id] = timestamp
    d.close()
    return "shelve successfully saved at time"

#
def get_access(path):
    try:
        with open(path, 'r') as f:
            app_id =f.readline().strip("\n")
            print(app_id)
            second_line = f.readline()
            app_secret = second_line
            access_token = app_id + "|" + app_secret
            print(access_token)
    except:
        print("app.txt not found will now try getting data from environment variables")
        access_token = os.environ['FB_ID'] + "|" + os.environ['FB_KEY']
    return access_token


def scrape(page_id,tstamp, useKafka, useES):
    access_token = get_access('app.txt')
    pageStamp = get_tstamp(page_id, tstamp, "save_times")
    save_shelve(page_id,'save_times')
    scraper = FB_SCRAPE(useKafka, useES, False, False)
    scraper.scrapeFacebookPageFeedStatus2( page_id, access_token, pageStamp)
    if os.environ.get("COMMENTS") is not None:
        scraper.scrapeComments()

# Function to save results into table



    return "results saved"






#if __name__ == '__main__':
    #group_id = "115285708497149"
    #scrape(group_id, 0,scrapeFacebookPageFeedStatus2)
