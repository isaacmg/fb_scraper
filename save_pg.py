from pony.orm import *
import os
db = Database("postgres", user=os.environ['pg_user'], password=os.environ['pg_password'], host=os.environ['pg_host'], database=os.environ['pg_db'])
class Posts(db.Entity):
    id = PrimaryKey(int, auto=True)
    group_name = Required(str)
    text = Required(LongStr)
    status_id = Required(str)
    person_name = Required(str)
    num_reactions = Required(int)
    num_comments = Required(int)
    num_likes = Required(int)

db.generate_mapping(create_tables=True)

@db_session
def save_post_pg(group, status_name, text, reactions, num_comments, likes, name):
    Post(group_name = group, text=text, status_id=status_name, num_likes=likes,  num_reactions=reactions, num_comments=num_comments, person_name=name)
