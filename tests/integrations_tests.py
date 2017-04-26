import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from fb_posts import scrape_comments_from_last_scrape, scrape_posts_from_last_scrape, scrape_posts_from_last_scrape_kafka, scrape_all_comments
scrape_posts_from_last_scrape("115285708497149")
scrape_posts_from_last_scrape_kafka("319872211700098")
scrape_all_comments("319872211700098")
