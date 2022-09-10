# pibic-dags
Repositório destinado para desenvolver o processo de ELT da pipeline do PIBIC, utilizando Apache Airflow
## Passo à passo:
### Instalar Apache Airflow:
```
pip install apache-airflow
```
### Rodar Airflow:
1. Para isso é preciso criar uma variável de ambiente chamda `AIRFLOW_HOME`, e setá-la para o diretório atual. Caso isso não seja feito, o airflow será instalado em `~/airflow/`.
```
export AIRFLOW_HOME = "$(pwd)"
```
2. Feito isso, vamos iniciar o banco de dados:
```
airflow db init
```
3. Antes de iniciar o web server, vamos criar um usuário com permissões de administrador:
```
airflow users create \
-u <NOME-USUARIO> \
-p <SENHA> \
-e <EMAIL> \
-f <PRIMEIRO-NOME> \
-l <ULTIMO-NOME> \
-r Admin
```
4. Agora vamos iniciar o web server:  
```
airflow webserver --port 8080
```
5. [localhost:8080](http://localhost:8080/)
### Inserindo a Dag:
1. No arquivo `$AIRFLOW_HOME/airflow.cfg`, altere `dags_folder` para a pasta `dags` do repositório.
2. Agora, atualize a UI e você deve ver a DAG.
