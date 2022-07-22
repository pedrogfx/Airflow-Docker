from datetime import datetime
import sys
import os
from airflow.models.variable import Variable
from os.path import join
import yaml
from airflow import DAG

DAG_VARS = Variable.get("DAG_KAFKA_AVRO", deserialize_json=True)
PATH_IMPORT = Variable.get("IMPORT_PATH")
APIKEY = DAG_VARS['APIKEY']
APISECRET = DAG_VARS['APISECRET']
BOOTSTRAP_SERVER = DAG_VARS['BOOTSTRAP_SERVER']





sys.path.append(PATH_IMPORT)
with open(join(PATH_IMPORT, 'config', 'dag_kafka_avro.yml'), 'r') as file:
    cfg_ingestion = yaml.safe_load(file.read())


def get_values():
    return True

default_args = {
    'start_date': datetime(2022, 7, 20, 0, 0),
    "owner": "de-pedro",
}

dag = DAG(
    "dag_kafka_avro",
    default_args=default_args,
    schedule_interval='*/120 * * * *',
    tags=['KAFKA','PYSPARK', 'STREAMING'])