package io.emo

import java.util.Properties

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}

object KProducer extends App {
  val prod_props = new Properties()
  prod_props.put("bootstrap.servers", "localhost:9093")
  prod_props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
  prod_props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")
  prod_props.put("acks", "all")
  prod_props.put("retries", 0)
  prod_props.put("batch.size", 16384)
  prod_props.put("linger.ms", 1)
  prod_props.put("buffer.memory", 33554432)

  val kProducer = new KafkaProducer[String, String](prod_props)

  for (indx <- 1 to 2000) {
    val record: ProducerRecord[String, String] =
      new ProducerRecord("topic-1", "record_" + indx)
    kProducer.send(record)
  }
  kProducer.close()
}
