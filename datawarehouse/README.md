# Data Engineering Nano Degree Cloud Project.
## _Project Overview_
### Understand working with AWS cloud S3 and EC2, and be able to perform an ETL process on cloud.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project is aimed at understanding cloud functions and deploying an ETL process on cloud.
## Requirements.
- AWS cloud
- SQL understanding
- Version Control
- Python

## Installation.

Install required python packages.

```sh
pip3 install psycopg2
```
## Configuration.
_Edit the config file in the root project._
_File name is dwh.cfg._
_Add the following parameters._

- KEY=
- SECRET=
- HOST=

[CLUSTER]
HOST=
DB_NAME=dwh
DB_USER=dwhuser
DB_PASSWORD=Passw0rd
DB_PORT=5439
DWH_IAM_ROLE_NAME=dwhRole
DWH_CLUSTER_IDENTIFIER=dwhCluster

[IAM_ROLE]
ARN='arn:aws:iam::477677659833:role/dwhRole'

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'

[AWS]
KEY=
SECRET=

[DWH] 
DWH_CLUSTER_TYPE=multi-node
DWH_NUM_NODES=4
DWH_NODE_TYPE=dc2.large
DWH_IAM_ROLE_NAME=dwhRole
CLUSTER=dwhCluster


