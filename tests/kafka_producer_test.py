from kafka import KafkaProducer
from avro import schema, datafile, io
import io as io2
class ProducerObject:
    def get_as_json(self, items):
        message = {"status_id": items[0], "status_message": items[1], "link_name": items[2], "status_type": items[3],
                   "status_link": items[4], "status_published": items[5], "num_reactions": items[6],
                   "num_comments": items[7],
                   "num_shares": items[8], "num_likes": items[9], "num_loves": items[10]}
        return message
    def serialize(self, items):
        schema_path = "fb_scheam.avsc"
        SCHEMA = schema.Parse(open(schema_path).read())
        writer = io.DatumWriter(SCHEMA)
        bytes_writer = io2.BytesIO()
        encoder = io.BinaryEncoder(bytes_writer)
        # There must be a better way of writing this item that isn't so long
        writer.write(get_as_json(items), encoder)
        raw_bytes = bytes_writer.getvalue()

        return raw_bytes

    def getMessage(self, message):
        message = self.get_as_json(message)
        message = self.serialize(message)
        return message






