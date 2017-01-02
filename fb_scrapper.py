import shelve
from fb_posts import scrapeFacebookPageFeedStatus
import time
#import fb_pages
# Function to scrape with.
# Call with group id and whether you want to scrape all the way back 0 or since last scrape 1.
def scrape(page_id,tstamp):
    with open('app.txt', 'r') as f:
        f.readline().strip("/n")
        second_line = f.readline()

    app_id = "238791666290359"
    app_secret = second_line
    access_token = app_id + "|" + app_secret
    # To do check if dict has key before calling
    if tstamp is 1:
        d = shelve.open('save_times')
        time_opened = d[page_id]
        pageStamp = str(time_opened)
        scrapeFacebookPageFeedStatus(page_id, access_token, pageStamp)
    scrapeFacebookPageFeedStatus(page_id, access_token,-2180131200)
    timestamp = int(time.time())
    d = shelve.open('save_times')
    d[page_id] = timestamp


#group_id = "115285708497149"
#scrape(group_id, 0)

