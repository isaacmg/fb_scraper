from kafka import KafkaProducer
if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('test', key=b'foo', value=b'big cock').get(timeout=60)

