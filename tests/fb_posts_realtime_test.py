import unittest
import os, sys
from kafka import KafkaProducer
from kafka import KafkaConsumer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class MyTest(unittest.TestCase):

    def test_kaf (self):



if __name__ == '__main__':
    unittest.main()