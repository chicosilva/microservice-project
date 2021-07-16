from kafka import KafkaProducer
import uuid
import json
from faker import Faker


def produce_customer(customer):
    
    data =  {
        'id': f"{customer.uuid}",
        'name': customer.name,
        'email': customer.email,
    }
    
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #print(producer.bootstrap_connected())

    producer.send('customers', data)