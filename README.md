# BFS and Hadoop Implementation for Finding Shortest Path in a Graph

## Overview

This project involves implementing the Breadth-First Search (BFS) algorithm to find the shortest path between nodes in a graph, both using regular Python and Hadoop MapReduce. The task is divided into two parts:

1. **Task 1:** Implement BFS using regular Python.
2. **Task 2:** Implement BFS using Hadoop MapReduce.

## Dataset

The dataset used is the LiveJournal social network graph, which can be downloaded from [here](https://snap.stanford.edu/data/soc-LiveJournal1.html). The dataset consists of user IDs and their friends.

## Task 1: BFS Implementation with Python

### Objectives

- Read the graph data.
- Map each ID with its friend nodes.
- Find the shortest path from nodes X (2000), Y (2010), and Z (1900) to all other nodes.
- Generate CSV files containing the paths from X, Y, and Z to all other nodes.

### Steps

1. **Reading the Graph:**
   - Use the `read_graph` function to read the graph data from the input file and store it in a dictionary format.

2. **Implementing BFS Algorithm:**
   - Use the `shortest_path` function to implement the BFS algorithm and find the shortest path between two nodes.

3. **Breadth-First Search:**
   - Explore all neighboring nodes of the current node before moving to the next level.

4. **Path Finding:**
   - Keep track of previous nodes to avoid revisiting them and maintain a list of paths to explore.

### Functions

- `read_graph(fp)`: Reads the graph data from a file and returns a dictionary of nodes and their edges.
- `shortest_path(graph, node1, node2)`: Takes a graph, starting node, and ending node as input and returns the shortest path between them.

### Challenges

- Handling large graphs efficiently, given the BFS algorithm's time complexity of O(V+E).

### Files

- `BDa.py`: Contains the Python implementation of the BFS algorithm.
- `Mapper and Redducer.py`: Contains the implementation for Hadoop system

### Hadoop Environment Setup

To run the Hadoop implementation, follow these steps to set up your Hadoop environment:

#### Hadoop Installation

1. **Download Hadoop:**

    ```bash
    wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
    ```

2. **Extract the tar file:**

    ```bash
    tar -xzvf hadoop-3.3.1.tar.gz
    ```

3. **Move Hadoop to `/usr/local/hadoop`:**

    ```bash
    sudo mv hadoop-3.3.1 /usr/local/hadoop
    ```

4. **Set Hadoop environment variables:**

    Add the following lines to your `~/.bashrc` file:

    ```bash
    export HADOOP_HOME=/usr/local/hadoop
    export HADOOP_INSTALL=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export YARN_HOME=$HADOOP_HOME
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
    export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
    export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
    ```

    Apply the changes:

    ```bash
    source ~/.bashrc
    ```

#### Hadoop Configuration

Edit the Hadoop configuration files located in `$HADOOP_HOME/etc/hadoop` directory:

- `core-site.xml`:

    ```xml
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://localhost:9000</value>
        </property>
    </configuration>
    ```

- `hdfs-site.xml`:

    ```xml
    <configuration>
        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
        <property>
            <name>dfs.name.dir</name>
            <value>file:///usr/local/hadoop/hadoop_data/hdfs/namenode</value>
        </property>
        <property>
            <name>dfs.data.dir</name>
            <value>file:///usr/local/hadoop/hadoop_data/hdfs/datanode</value>
        </property>
    </configuration>
    ```

- `mapred-site.xml`:

    ```xml
    <configuration>
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration>
    ```

- `yarn-site.xml`:

    ```xml
    <configuration>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
    </configuration>
    ```

#### Formatting the Hadoop Filesystem

1. **Format the namenode:**

    ```bash
    hdfs namenode -format
    ```
