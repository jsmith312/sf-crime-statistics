from kafka import KafkaConsumer
import json
import time

def main():
    consumer = KafkaConsumer("police.calls",
                             group_id ="test-group",
                             bootstrap_servers = ["localhost:9092"])
    for msg in consumer:
        message = msg.value
        print(f'got msg: {message}')

if __name__ == "__main__":
    main()