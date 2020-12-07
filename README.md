# SF Crime Statistics with Spark Streaming #
## Project Overview ## 
In this project, we have a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and we'll provide statistical analyses of the data using Apache Spark Structured Streaming.

## Requirements ##
- Spark 3.0.1
- Scala 2.12.x
- Java 1.8.x
- Python 3.6.x or above
- Docker

## How to run ##
### Run Kafka and Zookeeper ###
`docker-compose up -d`

### Run KafkaProducer Server ###
`python kafka_server.py`

### Start Spark Streaming job ###
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 --master local[*] data_stream.py`
