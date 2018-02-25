package io.emo

import java.util.Properties
import java.util.Arrays

import org.apache.kafka.clients.consumer.{ConsumerRecord, ConsumerRecords, KafkaConsumer}
import org.apache.kafka.common.TopicPartition

object KConsumer extends App {
  val cxm_props = new Properties()
  cxm_props.put("bootstrap.servers","localhost:9093")
  cxm_props.put("group.id", "c-1")
  cxm_props.put("enable.auto.commit", true)
  cxm_props.put("auto.commit.interval.ms", 1000)
  cxm_props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
  cxm_props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
  val kConsumer = new KafkaConsumer[String, String](cxm_props)
  val topic = "topic-1"
  val listener = new SaveOffsetsOnRebalance(kConsumer)
  kConsumer.subscribe(Arrays.asList(topic), listener)
  val records : ConsumerRecords[String, String] = kConsumer.poll(2000)
  val iterator = records.iterator()
  while( iterator.hasNext()) {
    val consumer_record = iterator.next()
    println(consumer_record.key() + " " + consumer_record.offset() + " " + consumer_record.value())
  }
}
