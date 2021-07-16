
from kafka import KafkaConsumer
import uuid
import json
from faker import Faker
from products.models import Product
import decimal


def consume_products():
    
    consumer = KafkaConsumer(
        'products',
        group_id='products',
        bootstrap_servers='kafka:9092',
        enable_auto_commit=False,
        auto_offset_reset='largest'
    )
    
    for msg in consumer:
        data = json.loads(msg.value)
        create_product(data)
    
    #consumer.commit();


def create_product(data):
    
    product = Product()

    if Product.objects.filter(uuid=data.get('uuid')).exists():
        product = Product.objects.get(uuid=data.get('uuid'))

    product.name = data.get('name')
    product.price = clean_valor_moeda(data.get('price'))
    product.uuid = data.get('uuid')
    product.save()


def clean_valor_moeda(valor):
    
    if not valor or valor == "":
        return 0

    valor = valor.replace('R$', '')
    valor = valor.replace(' ', '')

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    return decimal.Decimal(valor)
