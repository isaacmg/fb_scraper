from fb_scrapper import scrape_groups_pages
# To use our application you can use scrape_groups_pages or use one of our predefined functions

# Declare your group or page id here
group_id = "115285708497149"

# Choose which scraping function you want to call

# This function is currently not properly working and will scrape all comments
def scrape_comments_from_last_scrape(group_id):
    scrape_groups_pages(id, 1, 2, True)

# Scrape since the last time stamp for the id in the shelve file
def scrape_posts_from_last_scrape(group_id):
    scrape_groups_pages(group_id, 1, 1,  False)

# You must have Kafka running on localhost:9092 or change the port in fb_posts_realtime.py
# Also be advised this may be buggy (we are still in the process of writing tests for it).
def scrape_posts_from_last_scrape_kafka(group_id):
    scrape_groups_pages(group_id, 1, 0, False)

def scrape_all_posts(group_id):
    scrape_groups_pages(group_id, 0, 1, False)

def scrape_all_comments(group_id):
    scrape_groups_pages(group_id, 0, 2, True)


scrape_all_posts(group_id)

