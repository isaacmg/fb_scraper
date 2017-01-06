from fb_scrapper import scrape_pages
# Full scrape example with streaming
group_id = "115285708497149"
full_scrape = 0
scraper_type = 0
#scrape_pages(group_id,full_scrape,scraper_type)
# Full scrape example without streaming
#scrape_pages(group_id,0,1)
# Scrape lastest posts
scrape_pages(group_id,1,1)



