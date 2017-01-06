import shelve
from fb_posts import scrapeFacebookPageFeedStatus2
from fb_posts_realtime import scrapeFacebookPageFeedStatus
import time
#import fb_pages
# Function to scrape with.
# Call with group id and whether you want to scrape all the way back 0 or since last scrape 1.
# To do: allow passing of an array of groups, allow passing of a custom scrape date, add functions for scraping of pages
def scrape_pages(page_id, from_time, function_number):
    funcs = [scrapeFacebookPageFeedStatus,scrapeFacebookPageFeedStatus2]
    scrape(page_id, from_time, funcs[function_number] )

def scrape(page_id,tstamp,scrape_func):
    with open('app.txt', 'r') as f:
        f.readline().strip("/n")
        second_line = f.readline()

    app_id = "238791666290359"
    app_secret = second_line
    access_token = app_id + "|" + app_secret

    if tstamp is 1:
        d = shelve.open('save_times')
        if page_id in d:
            time_opened = d[page_id]
            pageStamp = str(time_opened)
            scrape_func(page_id, access_token, pageStamp)
        else:
            print("key not found in dict proceeding with full scrape")
            pageStamp = -2180131200
    elif tstamp is 0:
        pageStamp = -2180131200
    else:
        pageStamp=tstamp
    scrape_func(page_id, access_token, pageStamp)
    timestamp = int(time.time())
    d = shelve.open('save_times')
    d[page_id] = timestamp


#if __name__ == '__main__':
    #group_id = "115285708497149"
    #scrape(group_id, 0,scrapeFacebookPageFeedStatus2)


