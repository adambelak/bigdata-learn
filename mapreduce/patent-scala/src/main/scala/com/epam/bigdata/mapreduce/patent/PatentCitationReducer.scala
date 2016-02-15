package com.epam.bigdata.mapreduce.patent

import java.lang.Iterable

import org.apache.hadoop.io.Text
import org.apache.hadoop.mapreduce.Reducer

import scala.collection.JavaConverters._

class PatentCitationReducer extends Reducer[Text, Text, Text, Text] {
   override def reduce(key: Text, values: Iterable[Text], context: Reducer[Text, Text, Text, Text]#Context) =
      context.write(key, new Text(values.asScala mkString (",")))
}
