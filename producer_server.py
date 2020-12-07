from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file) as f:
            row_data = json.load(f)
            for row in row_data:
                message = self.dict_to_binary(row)
                # send the correct data
                self.send(topic = self.topic,value=message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')
        