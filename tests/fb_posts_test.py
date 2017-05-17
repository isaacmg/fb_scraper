import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shelve
import time
from fb_scrapper import save_shelve,  get_tstamp, get_access, scrape_groups_pages
from fb_posts import FB_SCRAPE
from fb_comments_page import getFacebookCommentFeedData, request_until_succeed, processFacebookComment
from fb_posts_realtime import serialize, get_as_json, init_kafka
from kafka_test import deserialize
from run_es import init_es





def test_func(page_id,d):
    if page_id in d:
        return 1
    else:
        return 0

class MyTest(unittest.TestCase):
    def test_save_shelve(self):
        save_shelve("13142345","test")
        d = shelve.open('test')
        self.assertEqual(test_func("13142345",d), 1)
    def test_tstamp(self):
        self.assertEqual(get_tstamp("13142345", 0,"test"),-2180131200)
    def test_tstamp2(self):
        timestamp = int(time.time())
        d = shelve.open("test")
        d["13142345"] = timestamp
        self.assertEqual(get_tstamp("13142345", 1,"test"), str(timestamp))
    def test_access_t(self):
        self.assertEqual(get_access('data/files/text.txt'),"999999999|awerqwerdummytext")
    def test_getFacebookPageFeedData(self):
        access = os.environ['FB_ID'] +"|" + os.environ['FB_KEY']
        a = FB_SCRAPE(False, False, False, False)
        data = a.getFacebookPageFeedData("paddlesoft", access, 100, 0 )
        if("message" in data["data"][0]):
            good = 1
        else:
            good = 2
        self.assertEqual(good,1)
    def test_procesFacebookPageFeedStatus(self):
        a2 = FB_SCRAPE(False, False, False, False)
        a ={'message': 'I may have the opportunity to get a wavehopper.  the specs say 210 lbs max but it is a really big boat.  has anyone here tried putting more weight than that in it?', 'from':{'id': '55', 'name':'somename'}, 'comments': {'summary': {'can_comment': False, 'total_count': 1, 'order': 'chronological'}, 'data': []}, 'reactions': {'summary': {'total_count': 0, 'viewer_reaction': 'NONE'}, 'data': []}, 'created_time': '2017-02-03T13:55:35+0000', 'type': 'status', 'id': '115285708497149_1769803846378652'}
        access = os.environ['FB_ID'] + "|" + os.environ['FB_KEY']
        self.assertEqual(a2.processFacebookPageFeedStatus(a,access), ('115285708497149_1769803846378652', 'I may have the opportunity to get a wavehopper.  the specs say 210 lbs max but it is a really big boat.  has anyone here tried putting more weight than that in it?', '', 'status', '', '2017-02-03 08:55:35', 0, 1, 0, 0, 0, 0, 0, 0, 0,'55',))
    def test_getReactionsForStatus(self):
        a = FB_SCRAPE(False, False, False, False)
        access = os.environ['FB_ID'] + "|"  + os.environ['FB_KEY']
        status_id = "115285708497149_1700908723268165"
        print(a.getReactionsForStatus(status_id, access))
        self.assertEquals(a.getReactionsForStatus(status_id,access),{'angry': {'data': [], 'summary': {'total_count': 0}}, 'haha': {'data': [], 'summary': {'total_count': 0}}, 'id': '115285708497149_1700908723268165','like': {'data': [], 'summary': {'total_count': 7}},'love': {'data': [], 'summary': {'total_count': 0}}, 'sad': {'data': [], 'summary': {'total_count': 0}},'wow': {'data': [], 'summary': {'total_count': 1}}})
    def test_getFacebookCommentFeedData(self):
        access_token = os.environ['FB_ID'] + "|" + os.environ['FB_KEY']
        print(getFacebookCommentFeedData("176485839144245_1128860933906726", access_token, 100, -2180131200))
        data = {'paging': {
            'cursors': {'after': 'WTI5dGJXVnVkRjlqZAFhKemIzSTZANVEV6T0RFMU9ERXhNamszTnpBd09Eb3hORGt3TlRreU9UQTUZD',
                        'before': 'WTI5dGJXVnVkRjlqZAFhKemIzSTZANVEV6TkRNeE5qa3lNek0yTVRFeU56b3hORGt3TWpJM05qUXkZD'}},
         'data': [{'id': '1134316923361127', 'like_count': 0, 'created_time': '2017-03-23T00:07:22+0000',
                   'message': 'what is the start time on friday?',
                   'from': {'id': '10210829571228766', 'name': 'Mike Eddy'}},
                  {'id': '1138158112977008', 'like_count': 1, 'created_time': '2017-03-27T05:35:09+0000',
                   'message': 'Hey Mike - 6 pm to 9 pm.  Indoors.  Paperwork, expectations, get to know each other, knots, anchors, mechanical advantage overview, some systems, check a few ACA items off the list.    In the past we have met at Conway Fire, and will likely meet there again this year.  Its right in Conway Village.',
                   'from': {'id': '10154257133022102', 'name': 'Darron Laughland'}}]}

        self.assertEqual(sorted(getFacebookCommentFeedData("176485839144245_1128860933906726", access_token, 100, -2180131200)), sorted(data))
    def test_processFacebookComment(self):
        comment = {'id': '1108028642656622', 'created_time': '2017-02-24T21:32:02+0000', 'message': 'Sweet Thanks', 'like_count': 0, 'from': {'id': '10158516794680088', 'name': 'Jake Risch'}}
        self.assertEqual(processFacebookComment(comment,"176485839144245_1108023245990495",''),('1108028642656622', '176485839144245_1108023245990495', '', b'Sweet Thanks', b'Jake Risch', '2017-02-24 16:32:02', 0))
    def test_groups_pages(self):
        group_id = "paddlesoft"
        print("all passes up to here")
        self.assertEqual(scrape_groups_pages(group_id, 0,  False, False), "Sucessfully scraped from 0for page id paddlesoft")
        self.assertEqual(scrape_groups_pages(group_id, 1, False, False), "Sucessfully scraped from 1for page id paddlesoft")

    def test_serialize(self):
        testList = ('115285708497149_1731636350195402', 'One-day special session, Northampton, MA YMCA.','Northampton Pool Rolling Session', 'event', 'https://www.facebook.com/events/319137738480268/','2017-01-09 18:51:17', 1, 0, 0, 1, 0, 0, 0, 0, 0, 0)
        s = serialize(testList)
        print(get_as_json(testList))
        print(deserialize(s))
        self.assertEqual(get_as_json(testList), deserialize(s))
    def test_reaction_id(self):
        scraper = FB_SCRAPE(False, False, False, False)
        status_id = "457628327745071_746174208890480"
        access_token = "354322838020934|" + os.environ['FB_KEY']
        self.assertEqual(scraper.get_reaction_ids(status_id,access_token), {"paging": {"cursors": {"after": "TlRneU1qTXdORG94TkRnM05qUTBOell3T2pJMU5EQTVOakUyTVRNPQZDZD", "before": "TlRneU1qTXdORG94TkRnM05qUTBOell3T2pJMU5EQTVOakUyTVRNPQZDZD"}}, "data": [{"id": "10103915113063889", "type": "LIKE"}]})
    def test_reaction_init_kafka(self):
        init_kafka("localhost:9092")
        # Kafka is running properly on Travis-CI if this doesn't fail
        self.assertEqual(1,1)
    def test_run_es(self):
        init_es()
        # TODO IMPLEMENT object comparision test
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
