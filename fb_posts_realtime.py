import urllib.request
import json
import datetime
import csv
import time
import codecs
from kafka import KafkaProducer
from avro import schema, datafile, io
import io as io2

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test', b'another_message').get(timeout=60)

#producer.send('foober',"some message")
def serialize(items):
    SCHEMA = schema.Parse(json.dumps({
        "namespace": "example.avro",
        "type": "record",
        "name": "facebookPost",
        "fields": [
            {"name": "status_id", "type": "string"},
            {"name": "status_message", "type": "string"},
            {"name": "link_name", "type": "string"},
            {"name": "status_type", "type": "string"},
            {"name": "status_link", "type": "string"},
            {"name": "status_published", "type": "string"}, #Maybe use time type in future?
            {"name": "num_reactions", "type": "int"},
            {"name": "num_comments", "type": "int"},
            {"name": "num_shares", "type": "int"},
            {"name": "num_likes", "type": "int"},
            {"name": "num_loves", "type": "int"}
        ]
    }))
    writer = io.DatumWriter(SCHEMA)
    bytes_writer = io2.BytesIO()
    encoder = io.BinaryEncoder(bytes_writer)
    # There must be a better way of writing this item that isn't so long
    print(items[1])
    writer.write({"status_id": items[0], "status_message": items[1], "link_name": items[2], "status_type": items[3],"status_link": items[4], "status_published":items[5], "num_reactions": items[6], "num_comments": items[7], "num_shares":items[8], "num_likes":items[9], "num_loves":items[10] }, encoder)
    raw_bytes = bytes_writer.getvalue()
    return raw_bytes




def request_until_succeed(url):
    req = urllib.request.Request(url)
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return response.read().decode(response.headers.get_content_charset())


# Needed to write tricky unicode correctly to csv
def unicode_normalize(text):
    return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22,
                            0xa0:0x20 })

def getFacebookPageFeedData(page_id, access_token, num_statuses,tStamp):

    # Construct the URL string; see http://stackoverflow.com/a/37239851 for
    # Reactions parameters
    base = "https://graph.facebook.com/v2.6"
    node = "/%s/feed" % page_id
    fields = "/?" + "fields=message,link,created_time,type,name,id," + \
            "comments.limit(0).summary(true),shares,reactions" + \
            ".limit(0).summary(true)"
    parameters =  "&limit=%s&since=%s&access_token=%s" % (num_statuses, tStamp, access_token)
    url = base + node + fields + parameters


    # retrieve data
    data = json.loads(request_until_succeed(url))

    return data

def getReactionsForStatus(status_id, access_token):

    # See http://stackoverflow.com/a/37239851 for Reactions parameters
        # Reactions are only accessable at a single-post endpoint

    base = "https://graph.facebook.com/v2.6"
    node = "/%s" % status_id
    reactions = "/?fields=" \
            "reactions.type(LIKE).limit(0).summary(total_count).as(like)" \
            ",reactions.type(LOVE).limit(0).summary(total_count).as(love)" \
            ",reactions.type(WOW).limit(0).summary(total_count).as(wow)" \
            ",reactions.type(HAHA).limit(0).summary(total_count).as(haha)" \
            ",reactions.type(SAD).limit(0).summary(total_count).as(sad)" \
            ",reactions.type(ANGRY).limit(0).summary(total_count).as(angry)"
    parameters = "&access_token=%s" % access_token
    url = base + node + reactions + parameters

    # retrieve data
    data = json.loads(request_until_succeed(url))

    return data


def processFacebookPageFeedStatus(status, access_token):

    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.

    # Additionally, some items may not always exist,
    # so must check for existence first

    status_id = status['id']
    status_message = '' if 'message' not in status.keys() else \
            unicode_normalize(status['message'])
    link_name = '' if 'name' not in status.keys() else \
            unicode_normalize(status['name'])
    status_type = status['type']
    status_link = '' if 'link' not in status.keys() else \
            unicode_normalize(status['link'])

    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.

    status_published = datetime.datetime.strptime(
            status['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + \
            datetime.timedelta(hours=-5) # EST
    status_published = status_published.strftime(
            '%Y-%m-%d %H:%M:%S') # best time format for spreadsheet programs

    # Nested items require chaining dictionary keys.

    num_reactions = 0 if 'reactions' not in status else \
            status['reactions']['summary']['total_count']
    num_comments = 0 if 'comments' not in status else \
            status['comments']['summary']['total_count']
    num_shares = 0 if 'shares' not in status else status['shares']['count']

    # Counts of each reaction separately; good for sentiment
    # Only check for reactions if past date of implementation:
    # http://newsroom.fb.com/news/2016/02/reactions-now-available-globally/

    reactions = getReactionsForStatus(status_id, access_token) if \
            status_published > '2016-02-24 00:00:00' else {}

    num_likes = 0 if 'like' not in reactions else \
            reactions['like']['summary']['total_count']

    # Special case: Set number of Likes to Number of reactions for pre-reaction
    # statuses

    num_likes = num_reactions if status_published < '2016-02-24 00:00:00' \
            else num_likes

    def get_num_total_reactions(reaction_type, reactions):
        if reaction_type not in reactions:
            return 0
        else:
            return reactions[reaction_type]['summary']['total_count']

    num_loves = get_num_total_reactions('love', reactions)
    num_wows = get_num_total_reactions('wow', reactions)
    num_hahas = get_num_total_reactions('haha', reactions)
    num_sads = get_num_total_reactions('sad', reactions)
    num_angrys = get_num_total_reactions('angry', reactions)

    # Return a tuple of all processed data

    return (status_id, status_message, link_name, status_type, status_link,
            status_published, num_reactions, num_comments, num_shares,
            num_likes, num_loves, num_wows, num_hahas, num_sads, num_angrys)

def scrapeFacebookPageFeedStatus(page_id, access_token, tStamp):
    with open('%s_facebook_statuses.csv' % page_id, 'w', newline='',encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(["status_id", "status_message", "link_name", "status_type",
                    "status_link", "status_published", "num_reactions",
                    "num_comments", "num_shares", "num_likes", "num_loves",
                    "num_wows", "num_hahas", "num_sads", "num_angrys"])

        has_next_page = True
        num_processed = 0   # keep a count on how many we've processed
        scrape_starttime = datetime.datetime.now()

        print("Scraping %s Facebook Page: %s\n" % (page_id, scrape_starttime))

        statuses = getFacebookPageFeedData(page_id, access_token, 100, tStamp)

        while has_next_page:
            for status in statuses['data']:

                # Ensure it is a status with the expected metadata
                if 'reactions' in status:
                    s = processFacebookPageFeedStatus(status,
                        access_token)
                    print(s)
                    a = ""
                    for element in s:
                        a += "," + str(element)
                    print(a)


                    byew = a.encode()

                    # To do serialize data properly in Avro berfore sending
                    # Also make the key be the name of the facebook group for easy trackingcom
                    producer.send('test2', key=b'foo', value=byew)
                    #producer.send('test', key=b'foo', value=a)


                    w.writerow(processFacebookPageFeedStatus(status,
                        access_token))


                # output progress occasionally to make sure code is not
                # stalling
                num_processed += 1
                if num_processed % 100 == 0:
                    print("%s Statuses Processed: %s" % \
                        (num_processed, datetime.datetime.now()))

            # if there is no next page, we're done.
            if 'paging' in statuses.keys():
                statuses = json.loads(request_until_succeed(
                                        statuses['paging']['next']))
            else:
                has_next_page = False


        print("\nDone!\n%s Statuses Processed in %s" % \
            (num_processed, datetime.datetime.now() - scrape_starttime))




