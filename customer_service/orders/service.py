from kafka import KafkaConsumer, KafkaProducer
import uuid
import json
from orders.models import Order, OrderItem
from faker import Faker
from customers.models import Customer
from products.models import Product


def consume_customers():

    consumer = KafkaConsumer(
        'customers',
        group_id='my_favorite_group',
        bootstrap_servers='kafka:9092',
        enable_auto_commit=False,
        auto_offset_reset='smallest'
    )
    
    """
    for msg in consumer:
        print (msg.value)
    """


def consume_order():
    
    consumer = KafkaConsumer(
        'orders',
        group_id='orders',
        bootstrap_servers='kafka:9092',
        enable_auto_commit=False,
        auto_offset_reset='largest'
    )
    
    for msg in consumer:
        #print(json.loads(msg.value))
        data = json.loads(msg.value)
        create_order(data)
    
    consumer.commit();

def produce_order():
    
    order_id = uuid.uuid4()
    product_id = uuid.uuid4()

    data = {
        "order": {
            "id": f"{order_id}",
            "customer_id": f"{uuid.uuid4()}",
            "status": 'reservado',
            "discount": 5,
            "total": 95,
            "created_at": '2021-07-07',
            "return_date": '2021-07-07',
        },
        "itens": [
            {
                'id': f"{uuid.uuid4()}",
                'order_id': f"{order_id}",
                'product': {
                    'id': f"{product_id}",
                    'name': 'Product 1',
                },
                'qtd': 1,
                'total': 100,
            }
        ]
    }

    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #print(producer.bootstrap_connected())

    producer.send('orders', data)


def create_order(data):
    
    #data = {'order': {'id': 'd8544b52-5b5b-4a51-8610-64727216d542', 'customer_id': '1e2f0512-57b9-4634-8c17-7a3de84aa456', 'status': 'reservado', 'discount': 5, 'total': 95, 'created_at': '2021-07-07', 'return_date': '2021-07-07'}, 'itens': [{'id': 'feede807-a112-42f6-81c2-5cd2ab7e7326', 'order_id': 'd8544b52-5b5b-4a51-8610-64727216d542', 'product': {'id': '21aa60d0-385b-4da3-9aa7-ee83f1c7e3c9', 'name': 'Product 1'}, 'qtd': 1, 'total': 100}]}
    
    fake = Faker()

    customer = Customer()
    customer.name = fake.name()
    customer.email = fake.email()
    customer.save()

    order = data.get('order')
    itens = data.get('itens')

    obj_order = Order()

    if Order.objects.filter(uuid=order['id']).exists():
        obj_order = Order.objects.get(uuid=order['id'])

    obj_order.customer = customer
    obj_order.status = order['status']
    obj_order.total = order['total']
    obj_order.created_at = order['created_at']
    obj_order.return_date = order['return_date']
    obj_order.save()

    for item in itens:
        
        obj_product = item.get('product')

        product = Product()

        if Product.objects.filter(uuid=obj_product['id']).exists():
            product = Product.objects.get(uuid=obj_product['id'])

        product.uuid=obj_product['id']
        product.name=obj_product['name']
        product.save()

        orderitem = OrderItem()
        orderitem.order = obj_order
        orderitem.product = product
        orderitem.total = item['total']
        orderitem.qtd = item['qtd']
        orderitem.save()

    return obj_order