from kafka import KafkaConsumer
from avro import schema, datafile, io
import io as io2
def consumer2():
    consumer = KafkaConsumer('test')
    schema_path="fies/fb_scheam.avsc"
    schema1 = schema.Parse(open(schema_path).read())
    for msg in consumer:
        bytes_reader = io2.BytesIO(msg.value)
        decoder = io.BinaryDecoder(bytes_reader)
        reader = io.DatumReader(schema1)
        message = reader.read(decoder)
        return(message)
def deserialize(x):
    schema_path = "data/files/fb_scheam.avsc"
    schema1 = schema.Parse(open(schema_path).read())
    bytes_reader = io2.BytesIO(x)
    decoder = io.BinaryDecoder(bytes_reader)
    reader = io.DatumReader(schema1)
    message = reader.read(decoder)
    return message
