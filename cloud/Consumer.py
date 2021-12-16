from confluent_kafka import Consumer
import certifi

if __name__ == '__main__':

  topic = "fire-predict"  
  conf = {  
    'group.id': "fire-predict",
    'bootstrap.servers': 'cell-1.streaming.sa-saopaulo-1.oci.oraclecloud.com:9092', #usually of the form cell-1.streaming.<region>.oci.oraclecloud.com:9092  
    'security.protocol': 'SASL_SSL',  
  
    'ssl.ca.location': certifi.where(),  # from step 6 of Prerequisites section
     # optionally instead of giving path as shown above, you can do 1. pip install certifi 2. import certifi and
     # 3. 'ssl.ca.location': certifi.where()
  
    'sasl.mechanism': 'PLAIN',  
    'sasl.username': 'matheusbrant/oracleidentitycloudservice/matheusbrantgo@gmail.com/ocid1.streampool.oc1.sa-saopaulo-1.amaaaaaaz2nkdgaatblh5dkumqibancjusgaghu24vhrec4yvhacwhrbixta',  # from step 2 of Prerequisites section
    'sasl.password': '2P0vj>Fxh4ghGe.KHD:p',  # from step 7 of Prerequisites section
   }  

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to topic
consumer.subscribe([topic])

# Process messages
try:
    while True:
        msg = consumer.poll(0)
        print(msg)
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting for message or event/error in poll()")
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            # Check for Kafka message
            record_key = "Null" if msg.key() is None else msg.key().decode('utf-8')
            record_value = msg.value().decode('utf-8')
            print("Consumed record with key "+ record_key + " and value " + record_value)
except KeyboardInterrupt:
    pass
finally:
    print("Leave group and commit final offsets")
    consumer.close()