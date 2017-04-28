from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import os
def init_es():
    host = os.environ['ES_HOST']
    if os.environ['ES_USE_AWS'] = 1:
        awsauth = AWS4Auth(os.environ['AWS_ES_ID'], os.environ['AWS_SECRET_ES'], ['AWS_ES_REGION'], 'es')
    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    return es
def index_res(es, index_name, status_id, status_data):
    es.index(index=index_name, doc_type='fb_post', id=status_id, body=status_data)
