package com.epam.bigdata.mapreduce.patent;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class PatentCitationReducer extends Reducer<Text, Text, Text, Text> {
    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        StringBuilder builder = new StringBuilder();
        for (Text value : values) {
            builder.append(value.toString()).append(",");
        }
        builder.substring(0, builder.length() - 1);
        context.write(key, new Text(builder.toString()));
    }
}
