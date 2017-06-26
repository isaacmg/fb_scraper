from pony.orm import *
import os
db = Database("postgres", user=os.environ['pg_user'], password=os.environ['pg_password'], host=os.environ['pg_host'], database=os.environ['pg_db'])
class Record(db.Entity):
    id = PrimaryKey(int, auto=True)
    group_name = Required(str)
    unix_tstamp = Required(int, size=64)
    posts_scraped = Required(int)
    end_tstamp = Required(int,size=64)

db.generate_mapping(create_tables=True)

@db_session
def save_scrape_PS( group, startTime, endTime, numberScraped):
    Record(group_name = group, unix_tstamp=startTime, end_tstamp=startTime, posts_scraped=numberScraped)
#TODO query DB to get timestamp
def get_time(group):
    return max(s.unix_tstamp for s in Record if s.group_name == group)
