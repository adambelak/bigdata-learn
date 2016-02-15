package com.epam.bigdata.mapreduce.lottery;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Created by Balazs_Viczan on 2016. 02. 10..
 */
public class LotteryMapper extends Mapper<Text, Text, Text, IntWritable> {
    @Override
    protected void map(Text key, Text value, Context context) throws IOException, InterruptedException {
        String[] splidetKey = key.toString().split(";");
        for (int i = 1; i <= 5; i++) {
            Text number = new Text(splidetKey[splidetKey.length - i]);
            IntWritable counter = new IntWritable(1);
            context.write(number, counter);
        }
    }
}
