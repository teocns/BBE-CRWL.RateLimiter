import uuid
import json
import time
from handle_request import handle_proxy_request
#from handle_request import forward_request
from helpers.uwsgi_headers_parser import parse_uwsgi_request_headers
from redis_cluster import RedisCluster
from redis_cluster.functions import register_domain_hit, reset_domain_hits
import requests


def handle_health_check(env, start_response):
    if env['REQUEST_METHOD'] == "GET":
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [b"OK"]


def application(env, start_response):

    health_check = handle_health_check(env, start_response)
    if health_check:
        return health_check`
    time.sleep(60)
    response = requests.get('https://api.ipify.org?format=json')

    start_response('200 OK', [('Content-Type', 'application/json')])
    return [response.text.encode('utf-8')]
    return handle_proxy_request(env, start_response)
