# Airflow-Docker

Running airflow on Windows using WSL2

```
https://docs.microsoft.com/en-us/windows/wsl/install
```

# [Airflow Settings](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-yaml) 

```
cd airflow-docker/
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
mkdir ./dags ./plugins ./logs
echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up
```
