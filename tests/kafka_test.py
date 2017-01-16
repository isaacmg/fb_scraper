from kafka import KafkaConsumer
from avro import schema, datafile, io
import io as io2

consumer = KafkaConsumer('test3')
print("begin")

schema_path="fb_scheam.avsc"
schema1 = schema.Parse(open(schema_path).read())

for msg in consumer:
    bytes_reader = io2.BytesIO(msg.value)
    decoder = io.BinaryDecoder(bytes_reader)
    reader = io.DatumReader(schema1)
    message = reader.read(decoder)
    print(message)