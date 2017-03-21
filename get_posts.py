from fb_scrapper import scrape_groups_pages
# Full scrape example with streaming
group_id = "paddlesoft"
full_scrape = 0
# Scraper type with Kafka or not 0, 1
scraper_type = 0
#scrape_pages(group_id,full_scrape,scraper_type)
# Full scrape example without streaming
#scrape_pages(group_id,0,1)
# Scrape lastest posts



def scrape_comments_from_last_scrape(id):
    scrape_groups_pages(id, 1, 2, 1, True)

def scrape_posts_from_last_scrape(id):
    scrape_groups_pages(id, 1, 1, 1, False)

def scrape_posts_from_last_scrape_kafka(id):
    scrape_groups_pages(id, 1, 0, 1, False)

def scrape_all_posts(id):
    scrape_groups_pages(id, 0, 1, 1, False)
def scrape_all_comments(id):
    scrape_groups_pages(id, 0, 2, 1, True)


#scrape_all_posts(group_id)
scrape_all_comments(group_id)
scrape_comments_from_last_scrape(group_id)

