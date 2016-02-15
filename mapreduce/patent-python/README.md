## patent-python
This example based on the [Advanced Map Reduce Program: Patient Citation](http://blog.hampisoftware.com/index.php/2015/09/09/advanced-map-reduce-program-patient-citation/) tutorial.

### Steps

1. SSH into your Hortonworks Sandbox
```bash
$ ssh root@127.0.0.1 -p 2222
```
2. Login as `hdfs` on your Sandbox
```bash
$ su -l hdfs
$ cd ~
```
3. Clone this repository and copy the source files to the target folder
```bash
$ git clone https://github.com/adambelak/bigdata-learn.git
$ cd bigdata-learn
$ mkdir -p target/mapper
$ mkdir -p target/reducer
$ cp mapreduce/patent-python/mapper/*.py target/
$ cp mapreduce/patent-python/reducer/*.py target/
```
4. Enter the `target` folder and download [acite75_99.zip](http://nber.org/patents/acite75_99.zip) file
```bash
$ cd target
$ wget http://nber.org/patents/acite75_99.zip
```
5. Unzip acite75_99.zip
```bash
$ unzip acite75_99.zip
```
6. Create HDFS working directory and upload the unzipped file
```bash
$ hadoop fs -mkdir -p /tmp/learn/mapreduce/patent/input
$ hadoop fs -put cite75_99.txt /tmp/learn/mapreduce/patent/input
```
7. Find and set up Hadoop home directory
Check the `HADOOP_HOME` variable:
```bash
$ echo $HADOOP_HOME
```
If the result is an empty line, set up the HADOOP_HOME variable for the current user. First find the `hadoop-streaming.jar` file.
```bash
$ find / -name hadoop-streaming.jar
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
$ -input /tmp/learn/mapreduce/patent/input/ -output /tmp/learn/mapreduce/patent/python-output \ 
$ -file $PWD/mapper/mapper.py -mapper 'python mapper.py' \ 
$ -file $PWD/reducer/reducer.py -reducer 'python reducer.py'  
```
The $PWD is a system variable which contains your current working directory.
The program doesn't run if your output directory exists. Choose a non-existing folder or remove the `python-output` folder
```bash
$ hadoop fs -rm -R /tmp/learn/mapreduce/patent/python-output
```
9. If you want, you can check the status of your MapReduce program 
http://127.0.0.1:8088/cluster
10. If your program finished, you can check the result
First list the output files
```bash
$ hadoop fs -ls /tmp/learn/mapreduce/patent/python-output
```
You'll see two entries. One of these the `part-00000` file (or something similar) which contains the result. Copy it to the local filesystem
```bash
$ mkdir output
$ hadoop fs -get /tmp/learn/mapreduce/patent/python-output/part-00000 output/
```
Now you can open it
```bash
$ vi output/part-00000
```

