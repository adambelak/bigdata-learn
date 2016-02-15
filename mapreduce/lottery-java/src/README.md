## patent-java
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
$ cp mapreduce/lottery-java/target/lottery-java-0.0.1-SNAPHOT.jar target/lottery-java.jar 
```
4. enter the `target` folder and download [otos.csv](http://www.szerencsejatek.hu/xls/otos.csv) file
```bash
$ cd target
$ wget http://www.szerencsejatek.hu/xls/otos.csv
```
5. create HDFS working directory and upload the unzipped file
```bash
$ hadoop fs -mkdir -p /tmp/learn/mapreduce/lottery/input
$ hadoop fs -put otos.csv /tmp/learn/mapreduce/lottery/input
```
6. run the MapReduce program
```bash
$ yarn jar lottery-java.jar /tmp/learn/mapreduce/lottery/input /tmp/learn/mapreduce/lottery/java-output  
```
The program doesn't run if your output directory exists. Choose a non-existing folder or remove the `java-output` folder
```bash
$ hadoop fs -rm -R /tmp/learn/mapreduce/lottery/java-output
```
7. if you want, you can check the status of your MapReduce program 
http://127.0.0.1:8088/cluster
8. if your program finished, you can check the result
First list the output files
```bash
$ hadoop fs -ls /tmp/learn/mapreduce/lottery/java-output
```
You'll see two entries. One of these the `part-r-00000` file (or something similar) which contains the result. Copy it to the local filesystem
```bash
$ mkdir output
$ hadoop fs -get /tmp/learn/mapreduce/lottery/java-output/part-r-00000 output/
```
Now you can open it
```bash
$ vi output/part-r-00000
```