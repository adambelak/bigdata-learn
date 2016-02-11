package com.epam.bigdata.mapreduce.patent

import org.apache.hadoop.io.Text
import org.apache.hadoop.mapreduce.Mapper

class PatentCitationMapper extends Mapper[Text, Text, Text, Text] {
   override def map(key: Text, value: Text, context: Mapper[Text, Text, Text, Text]#Context) = {
      val write = context.write _
      write.tupled(key.toString split (",") match { case Array(a, b) => (new Text(a), new Text(b)) })
   }
}
