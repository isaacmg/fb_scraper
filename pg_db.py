import pony.orm import *
import os
db = pony.Database("postgres", user=os.environ['pg_user'], password=os.environ['pg_password'], host=os.environ['pg_host'], database=os.environ['pg_db'])
class Record(db.Entity):
    id = PrimaryKey(int, auto=True)
    group_name = Required(str)
    unix_tstamp = Required(int, size=64)
    posts_scraped = Required(int)
    end_tstamp = Required(int,size=64)

db.generate_mapping(create_tables=True)
