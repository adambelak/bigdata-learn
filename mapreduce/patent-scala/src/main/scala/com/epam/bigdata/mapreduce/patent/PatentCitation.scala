package com.epam.bigdata.mapreduce.patent

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.Path
import org.apache.hadoop.io.Text
import org.apache.hadoop.mapreduce.Job
import org.apache.hadoop.mapreduce.lib.input.{FileInputFormat, KeyValueTextInputFormat}
import org.apache.hadoop.mapreduce.lib.output.{FileOutputFormat, TextOutputFormat}

object PatentCitation {

   def main(args: Array[String]) {
      val job = Job.getInstance(new Configuration(), "Patent Citation Scala Example")
      job setJarByClass PatentCitation.getClass
      job setMapperClass classOf[PatentCitationMapper]
      job setReducerClass classOf[PatentCitationReducer]
      job setInputFormatClass classOf[KeyValueTextInputFormat]
      job setOutputFormatClass classOf[TextOutputFormat[_, _]]
      job setMapOutputKeyClass classOf[Text]
      job setMapOutputValueClass classOf[Text]
      job setOutputKeyClass classOf[Text]
      job setOutputValueClass classOf[Text]
      FileInputFormat addInputPath(job, new Path(args(0)))
      FileOutputFormat setOutputPath(job, new Path(args(1)))
      System.exit(if (job.waitForCompletion(true)) 0 else 1);
   }

}
