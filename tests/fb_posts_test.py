import unittest
import os, sys
from kafka import KafkaProducer
from kafka_test import deserialize, consumer2
from kafka_producer_test import ProducerObject
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fb_posts_realtime import serialize
from fb_posts_realtime import get_as_json

def fun(x):
    return x + 1



class MyTest(unittest.TestCase):
    def test(self):
        testList = ('115285708497149_1731636350195402', 'One-day special session, Northampton, MA YMCA.', 'Northampton Pool Rolling Session', 'event', 'https://www.facebook.com/events/319137738480268/', '2017-01-09 18:51:17', 1, 0, 0, 1, 0, 0, 0, 0, 0)
        s = serialize(testList)
        self.assertEqual(get_as_json(testList), deserialize(s))

    def kafka_producer(self):
        print('this is text')
        a = ProducerObject()

        message = a.getMessage('115285708497149_1731636350195402', 'One-day special session, Northampton, MA YMCA.', 'Northampton Pool Rolling Session', 'event', 'https://www.facebook.com/events/319137738480268/', '2017-01-09 18:51:17', 1, 0, 0, 1, 0, 0, 0, 0, 0)
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send('foobar', message)
        producer.flush()

        #return_message = consumer()
        self.assertEqual(message,return_message)


if __name__ == '__main__':
    unittest.main()