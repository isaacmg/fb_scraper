import shelve
from fb_posts import scrapeFacebookPageFeedStatus
#import fb_pages
def scrape(page_id):
    with open('app.txt', 'r') as f:
        f.readline().strip("/n")
        second_line = f.readline()
    app_id = "238791666290359"
    app_secret = second_line
    access_token = app_id + "|" + app_secret
    scrapeFacebookPageFeedStatus(page_id, access_token)
    timestamp = int(time.time())

group_id = "160558090672531"
scrape(group_id)
#&since=1364849754