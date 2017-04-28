import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from get_posts import *
scrape_posts_last_es("115285708497149")
scrape_posts_from_last_scrape("115285708497149")
scrape_posts_from_last_scrape_kafka("319872211700098")
scrape_all_comments("319872211700098")
