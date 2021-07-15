from kafka import KafkaConsumer


def consume_customers():

    consumer = KafkaConsumer(
        'customers',
        group_id='my_favorite_group',
        bootstrap_servers='kafka:9092',
        enable_auto_commit=False,
        auto_offset_reset='smallest'
    )
    
    for msg in consumer:
        print (msg.value)

