## patent-scala
This example based on the [Advanced Map Reduce Program: Patient Citation](http://blog.hampisoftware.com/index.php/2015/09/09/advanced-map-reduce-program-patient-citation/) tutorial.

### Steps

1. SSH into your Hortonworks Sandbox
```bash
$ ssh root@127.0.0.1 -p 2222
```
2. login as `hdfs` on your Sandbox
```bash
$ su -l hdfs
```
3. clone this repository and build the project
```bash
$ git clone git@github.com:adambelak/bigdata-learn.git
$ cd bigdata-learn
$ mvn clean package
$ mkdir target
$ cp mapreduce/patent-scala/target/patent-scala-0.0.1-SNAPHOT.jar target/patent-scala.jar 
```
4. enter the `target` folder and download [acite75_99.zip](http://nber.org/patents/acite75_99.zip) file
```bash
$ cd target
$ wget http://nber.org/patents/acite75_99.zip
```
5. unzip acite75_99.zip
```bash
$ unzip acite75_99.zip
```
6. create HDFS working directory and upload the unzipped file
```bash
$ hadoop fs -mkdir -p /tmp/learn/mapreduce/patent/input
$ hadoop fs -put cite75_99.txt /tmp/learn/mapreduce/patent/input
```
7. run the MapReduce program
```bash
$ yarn jar patent-scala.jar /tmp/learn/mapreduce/patent/input /tmp/learn/mapreduce/patent/scala-output  
```
The program doesn't run if your output directory exists. Choose a non-existing folder or remove the `scala-output` folder
```bash
$ hadoop fs -rmdir /tmp/learn/mapreduce/patent/scala-output
```
8. if you want, you can check the status of your MapReduce program 
http://127.0.0.1:8088/cluster
9. if your program finished, you can check the result
First list the output files
```bash
$ hadoop fs -ls /tmp/learn/mapreduce/patent/scala-output
```
You'll see two entries. One of these the `part-r-00000` file (or something similar) which contains the result. Copy it to the local filesystem
```bash
$ mkdir output
$ hadoop fs -get /tmp/learn/mapreduce/patent/scala-output/part-r-00000 output/
```
Now you can open it
```bash
$ vi output/part-r-00000
```

