import time
import json
import http.client
from profiles import Logger, RequestStuff

rs = RequestStuff()
logger = Logger()

# Init [httpClient]
try:
    httpClient = http.client.HTTPConnection(rs.address_url)
except Exception as e:
    logger.error(e)
    raise Exception(e)

def checkout(q):
    """ Check out [q] online """
    # Set [retry] option
    retry = True
    # Try to check out
    while retry:
        # Reset [retry] option
        retry = False
        # Sending 'GET' request
        httpClient.request('GET', rs.mk_url(q))
        # Get and parse response from server
        response = httpClient.getresponse()
        result_all = response.read().decode('utf-8')
        result = json.loads(result_all)
        # Error code of 54003 refers 'Invalid Access Limit'
        if result.get('error_code', '0') == '54003':
            # Set [retry] option
            retry = True
            # Wait 1 second
            time.sleep(1)
    # Return result
    return result

qs = ['apple', 'banana', 'orange']

try:
    while True:
        q = input('>> ')
        if q == 'q':
            break
        print (checkout(q))

except Exception as e:
    print (e)
finally:
    httpClient.close()