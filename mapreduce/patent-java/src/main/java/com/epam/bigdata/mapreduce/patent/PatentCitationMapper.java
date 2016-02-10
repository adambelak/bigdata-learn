package com.epam.bigdata.mapreduce.patent;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class PatentCitationMapper extends Mapper<Text, Text, Text, Text> {
    @Override
    protected void map(Text key, Text value, Context context) throws IOException, InterruptedException {
        String[] citation = key.toString().split(",");
        Text cited = new Text(citation[0]);
        Text citing = new Text(citation[1]);
        context.write(cited, citing);
    }
}
