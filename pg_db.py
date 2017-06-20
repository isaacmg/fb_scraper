import pony
import os
db = pony.Database("postgres", user=os.environ['pg_user'], password=os.environ['pg_password'], host=os.environ['pg_host'], database=os.environ['pg_db'])
db.generate_mapping(create_tables=True)
class Record(db.Entity):
    id = PrimaryKey(int, auto=True)
    group_name = Required(str)
    unix_tstamp = Required(int)
    posts_scraped = Required(int)
    end_tstamp = Required(int)
