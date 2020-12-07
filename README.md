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

## How did changing values on the SparkSession property parameters affect the throughput and latency of the data? ##
From what I noticed, It either increased or decreased the `processRowsPerSecond`.

## What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal? ##
First, to tell what properties affected the performance of the stream processing I analzyed the `processRowsPerSecond` field in the progress report. So to reach a more optimal value I found that the these 3 fields seemed to affted this metric the most:
- `spark.streaming.kafka.maxRatePerPartition` - Maximum rate (number of records per second) at which data will be read from each Kafka partition
- `spark.sql.shuffle.partitions` - The default number of partitions to use when shuffling data for joins or aggregations.
- `spark.executor.cores	` - increase the number of cores in an executor node.