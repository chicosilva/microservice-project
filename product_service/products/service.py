from kafka import KafkaProducer
import uuid
import json
from faker import Faker


def produce_product(product):
    
    data =  {
        'id': f"{product.uuid}",
        'name': product.name,
        'description': product.description,
        'price': f"{product.price}",
        'qtd_available': product.qtd_available,
        'qtd_total': product.qtd_total,
    }
    
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #print(producer.bootstrap_connected())

    producer.send('products', data)