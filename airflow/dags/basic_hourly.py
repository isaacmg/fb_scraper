from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime
import os
import sys

args = {
  'owner': 'airflow'
  , 'start_date': datetime(2017, 1, 27)
  , 'provide_context': True
}
d = datetime(2017, 3, 25, 3, 15,00)


dag = DAG('run_facebook', start_date = d, schedule_interval = '10 * * * *', default_args = args)

t_main = BashOperator(
    task_id = 'fb_scrape'
  , dag = dag
  , bash_command = 'python /Users/isaac/Documents/Tech/fb_scraper/airflow/example.py ' + '/Users/isaac/Documents/Tech/fb_scraper/'
  )
