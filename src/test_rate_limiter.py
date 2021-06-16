from random import shuffle
import requests
from threading import Thread
from helpers.names import get_nickname



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
    'http':'http://awseb-AWSEB-K70LI46IDYR7-c04855a25aeb5c69.elb.eu-west-3.amazonaws.com'
}
@threaded
def f():
    print('Firing')
    response = requests.get('http://dummy.site',proxies=proxy, headers={'X_CRAWLER_THREAD_DOMAIN': 'dummy.site'},timeout=1)
    print(str(response.status_code) + response.text)

for i in range(3):
    f()
