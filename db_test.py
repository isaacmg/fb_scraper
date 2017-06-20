import pony
with pony.orm.db_session
album = Album(artist=new_artist,
                  title=u"Read All About It",
                  release_date=datetime.date(1988,12,01),
                  publisher=u"Refuge",
                  media_type=u"CD")
