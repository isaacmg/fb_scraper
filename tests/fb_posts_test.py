import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import shelve
import time
from fb_scrapper import save_shelve,  get_tstamp, get_access
from fb_posts import getFacebookPageFeedData, processFacebookPageFeedStatus, getReactionsForStatus
from fb_comments_page import getFacebookCommentFeedData, request_until_succeed


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
        access = "238791666290359|" + os.environ['FB_KEY']
        data = getFacebookPageFeedData("paddlesoft", access, 100, 0 )
        if("message" in data["data"][0]):
            good = 1
        else:
            good = 2
        self.assertEqual(good,1)
    def test_procesFacebookPageFeedStatus(self):
        a ={'message': 'I may have the opportunity to get a wavehopper.  the specs say 210 lbs max but it is a really big boat.  has anyone here tried putting more weight than that in it?', 'comments': {'summary': {'can_comment': False, 'total_count': 1, 'order': 'chronological'}, 'data': []}, 'reactions': {'summary': {'total_count': 0, 'viewer_reaction': 'NONE'}, 'data': []}, 'created_time': '2017-02-03T13:55:35+0000', 'type': 'status', 'id': '115285708497149_1769803846378652'}
        access = "238791666290359|" + os.environ['FB_KEY']
        self.assertEqual(processFacebookPageFeedStatus(a,access), ('115285708497149_1769803846378652', 'I may have the opportunity to get a wavehopper.  the specs say 210 lbs max but it is a really big boat.  has anyone here tried putting more weight than that in it?', '', 'status', '', '2017-02-03 08:55:35', 0, 1, 0, 0, 0, 0, 0, 0, 0))
    def test_getReactionsForStatus(self):
        access = "238791666290359|" + os.environ['FB_KEY']
        status_id = "115285708497149_1700908723268165"
        print(getReactionsForStatus(status_id, access))
        self.assertEquals(getReactionsForStatus(status_id,access),{'angry': {'data': [], 'summary': {'total_count': 0}}, 'haha': {'data': [], 'summary': {'total_count': 0}}, 'id': '115285708497149_1700908723268165','like': {'data': [], 'summary': {'total_count': 6}},'love': {'data': [], 'summary': {'total_count': 0}}, 'sad': {'data': [], 'summary': {'total_count': 0}},'wow': {'data': [], 'summary': {'total_count': 1}}})
    def test_getFacebookCommentFeedData(self):
        access_token = "238791666290359|" + os.environ['FB_KEY']
        data = {'paging': {
            'cursors': {'after': 'WTI5dGJXVnVkRjlqZAFhKemIzSTZANVEV6T0RFMU9ERXhNamszTnpBd09Eb3hORGt3TlRreU9UQTUZD',
                        'before': 'WTI5dGJXVnVkRjlqZAFhKemIzSTZANVEV6TkRNeE5qa3lNek0yTVRFeU56b3hORGt3TWpJM05qUXkZD'}},
         'data': [{'id': '1134316923361127', 'like_count': 0, 'created_time': '2017-03-23T00:07:22+0000',
                   'message': 'what is the start time on friday?',
                   'from': {'id': '10210829571228766', 'name': 'Mike Eddy'}},
                  {'id': '1138158112977008', 'like_count': 1, 'created_time': '2017-03-27T05:35:09+0000',
                   'message': 'Hey Mike - 6 pm to 9 pm.  Indoors.  Paperwork, expectations, get to know each other, knots, anchors, mechanical advantage overview, some systems, check a few ACA items off the list.    In the past we have met at Conway Fire, and will likely meet there again this year.  Its right in Conway Village.',
                   'from': {'id': '10154257133022102', 'name': 'Darron Laughland'}}]}

        self.assertEqual(getFacebookCommentFeedData("176485839144245_1128860933906726", access_token, 100, -2180131200), data)





        #Fix timeout errors



if __name__ == '__main__':
    unittest.main()
