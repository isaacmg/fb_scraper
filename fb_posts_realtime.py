import urllib.request
import json
import datetime
import csv
import time
from kafka import KafkaProducer

def init_kafka(port):
    producer = KafkaProducer(bootstrap_servers=port)
    producer.send('test', b'another_message').get(timeout=60)
    return producer

def get_as_json(items):
    message= {"status_id": items[0], "status_message": items[1], "link_name": items[2], "status_type": items[3],
     "status_link": items[4], "status_published": items[5], "num_reactions": items[6], "num_comments": items[7],
     "num_shares": items[8], "num_likes": items[9], "num_loves": items[10]}
    return message

# TODO move serilization schema to file

def serialize(items):
    from avro import schema, io
    import io as io2

    schema_path = "data/files/fb_scheam.avsc"
    schema = schema.Parse(open(schema_path).read())
    writer = io.DatumWriter(schema)
    bytes_writer = io2.BytesIO()
    encoder = io.BinaryEncoder(bytes_writer)
    # There must be a better way of writing this item that isn't so long
    writer.write(get_as_json(items), encoder)
    raw_bytes = bytes_writer.getvalue()

    return raw_bytes

def send_message(producer, message, page_id):
    message_data = serialize(message)
    print(message_data)
    # Also make the key be the name of the facebook group for easy tracking
    my_str_as_bytes = str.encode(page_id)
    producer.send('fb', key=my_str_as_bytes, value=message_data)
    return "message sent"

