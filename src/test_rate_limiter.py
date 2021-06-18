from random import shuffle
import requests
from threading import Thread
from helpers.names import get_nickname
import time


# Threaded function snippet
def threaded(fn):
    """ 
    To use as decorator to make a function call threaded.
    Needs import
    from threading import Thread"""
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper



# domains = []
# for i in range(99):
#     domains.append(get_nickname())

# domains = domains * 7
# shuffle(domains)



# cnt = 0


proxy = {
    'http':'http://awseb-AWSEB-S2CV7JPAFO1E-455819108.eu-west-3.elb.amazonaws.com'
}



pending_requests = []

@threaded
def f():
    global pending_requests
    #print('Firing')
    pending_requests.append(1)
    response = requests.post('http://dummy.site',proxies=proxy, headers={'X_CRAWLER_THREAD_DOMAIN': 'dummy.site'})
    pending_requests.pop()
    print(str(response.status_code) + response.text)

requests_arr = []




while True:
    input()
    f()
    print('Pending requests: ' + str(len(pending_requests)))


