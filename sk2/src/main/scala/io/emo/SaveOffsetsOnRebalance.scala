package io.emo

import java.util

import org.apache.kafka.clients.consumer.{ConsumerRebalanceListener, KafkaConsumer}
import org.apache.kafka.common.TopicPartition

class SaveOffsetsOnRebalance(consumer: KafkaConsumer[String, String]) extends ConsumerRebalanceListener{

  override def onPartitionsRevoked(partitions: util.Collection[TopicPartition]): Unit = {
    println("onPartitionsRevoked")
    val iterator = partitions.iterator()
    while (iterator.hasNext) {
      var p: TopicPartition = iterator.next()
      println(p.partition() + " " + p.topic())
    }
  }

  override def onPartitionsAssigned(partitions: util.Collection[TopicPartition]): Unit = {
    println("onPartitionsAssigned")
    val iterator = partitions.iterator()
    while (iterator.hasNext) {
      var p: TopicPartition = iterator.next()
      println(p.partition() + " " + p.topic() + " " + consumer.position(p))
      consumer.seek(p, 639)
      println(p.partition() + " " + p.topic() + " " + consumer.position(p))
    }
    println("onPartitionsAssigned")
  }
}
