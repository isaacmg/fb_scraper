import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kafka import KafkaConsumer
from avro import schema, datafile, io
import io as io2
from fb_posts_realtime import serialize
from fb_posts_realtime import get_as_json

def fun(x):
    return x + 1
def deserialize(x):
    schema_path = "fb_scheam.avsc"
    schema1 = schema.Parse(open(schema_path).read())
    bytes_reader = io2.BytesIO(x)
    decoder = io.BinaryDecoder(bytes_reader)
    reader = io.DatumReader(schema1)
    message = reader.read(decoder)
    return message


class MyTest(unittest.TestCase):
    def test(self):
        testList = ('115285708497149_1731636350195402', 'One-day special session, Northampton, MA YMCA.', 'Northampton Pool Rolling Session', 'event', 'https://www.facebook.com/events/319137738480268/', '2017-01-09 18:51:17', 1, 0, 0, 1, 0, 0, 0, 0, 0)
        s = serialize(testList)
        self.assertEqual(get_as_json(testList), deserialize(s))
    def kafka_producer(self):

if __name__ == '__main__':
    unittest.main()