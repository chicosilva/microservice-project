
from kafka import KafkaConsumer
import uuid
import json
from .models import Customer


def consume_customers():
    
    consumer = KafkaConsumer(
        'customers',
        group_id='customers',
        bootstrap_servers='kafka:9092',
        enable_auto_commit=False,
        auto_offset_reset='largest'
    )
    
    for msg in consumer:
        data = json.loads(msg.value)
        create_customer(data)
    
    #consumer.commit();


def create_customer(data):
    
    customer = Customer()

    if Customer.objects.filter(uuid=data.get('uuid')).exists():
        customer = Customer.objects.get(uuid=data.get('uuid'))

    customer.name = data.get('name')
    customer.uuid = data.get('uuid')
    customer.email = data.get('email')
    customer.save()
