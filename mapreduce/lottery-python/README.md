## lottery-python

### Steps

1. SSH into your Hortonworks Sandbox
```bash
$ ssh root@127.0.0.1 -p 2222
```
2. Login as `hdfs` on your Sandbox
```bash
$ su -l hdfs
```
3. Clone this repository and copy the source files to the target folder
```bash
$ git clone git@github.com:adambelak/bigdata-learn.git
$ cd bigdata-learn
$ mkdir -p target/mapper
$ mkdir -p target/reducer
$ cp mapreduce/lottery-python/mapper/*.py target/mapper
$ cp mapreduce/lottery-python/reducer/*.py target/reducer
```
4. Enter the target folder and copy the lottery.csv into the folder 
```bash
$ cd target
$ cp ../mapreduce/lottery-python/lottery.csv target/
```
5. Create HDFS working directory and upload the unzipped file
```bash
$ hadoop fs -mkdir -p /tmp/learn/mapreduce/lottery/input
$ hadoop fs -put lottery.csv /tmp/learn/mapreduce/lottery/input
```
7. Find and set up Hadoop home directory
Check the `HADOOP_HOME` variable:
```bash
$ echo $HADOOP_HOME
```
If the result is an empty line, set up the HADOOP_HOME variable for the current user. First find the hadoop-streaming.jar file (as root)
```bash
# find / -name hadoop-streaming.jar
```
The result at my sandbox was the following:  
```
/usr/hdp/2.3.2.0-2950/hadoop-mapreduce/hadoop-streaming.jar
/hadoop/yarn/local/filecache/12/pig.tar.gz/pig/test/e2e/pig/lib/hadoop-streaming.jar
```
We need the first one. Now set up the HADOOP_HOME variable for the current user:
```bash
$ echo "HADOOP_HOME=/usr/hdp/2.3.2.0-2950" >> ~/.bashrc
$ source ~/.bashrc
```
8. Run the MapReduce program
```bash
$ yarn jar $HADOOP_HOME/hadoop-mapreduce/hadoop-streaming.jar \
$ -input /tmp/learn/mapreduce/lottery/input/ -output /tmp/learn/mapreduce/lottery/python-output \ 
$ -file /home/hdfs/mapreduce-examples/lottery/mapper/mapper.py -mapper 'python mapper.py' \ 
$ -file /home/hdfs/mapreduce-examples/lottery/reducer/reducer.py -reducer 'python reducer.py'  
```
The program doesn't run if your output directory exists. Choose a non-existing directory or remove the `python-output` folder
```bash
$ hadoop fs -rm -R /tmp/learn/mapreduce/lottery/python-output
```
9. If you want, you can check the status of your MapReduce program 
http://127.0.0.1:8088/cluster
10. If your program finished, you can check the result
First list the output files
```bash
$ hadoop fs -ls /tmp/learn/mapreduce/lottery/python-output
```
You'll see two entries. One of these the `part-00000` file (or something similar) which contains the result. Copy it to the local filesystem
```bash
$ mkdir output
$ hadoop fs -get /tmp/learn/mapreduce/lottery/python-output/part-00000 output/
```
Now you can open it
```bash
$ vi output/part-00000
```

