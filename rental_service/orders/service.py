from kafka import KafkaProducer
import uuid
import json


def produce_order(order):
    
    customer = order.customer

    l_itens = []

    for item in order.get_itens.all():

        l_itens.append(
            
            {
                'uuid': f"{order.uuid}",
                'product': {
                    'id': f"{item.product.uuid}",
                    'name': item.product.name,
                },
                'qtd': item.qtd,
                'total': f"{item.total}",
            }
        
        )

    data = {
        "order": {
            "id": f"{order.uuid}",
            "customer_id": f"{customer.uuid}",
            "status": order.status,
            "discount": f"{order.discount}",
            "total": f"{order.total}",
            "created_at": order.created_at.strftime("%Y-%m-%d %H:%M"),
            "return_at": order.return_at.strftime("%Y-%m-%d"),
        },
        "itens": l_itens
    }

    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #print(producer.bootstrap_connected())

    producer.send('orders', data)


