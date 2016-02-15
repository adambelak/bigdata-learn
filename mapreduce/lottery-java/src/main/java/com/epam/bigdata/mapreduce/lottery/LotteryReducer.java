package com.epam.bigdata.mapreduce.lottery;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

/**
 * Created by Balazs_Viczan on 2016. 02. 10..
 */
public class LotteryReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int counter = 0;
        for (IntWritable value : values) {
            counter += value.get();
        }
        context.write(key, new IntWritable(counter));
    }
}
