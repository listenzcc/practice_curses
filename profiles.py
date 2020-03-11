# Profiles

import os
import random
import urllib
import hashlib
import logging
from keywords import mykey

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(asctime)s %(message)s',
                    filename=os.path.join('logging.log'))


class Logger():
    def __init__(self):
        pass

    def error(self, message):
        print(f'ERROR: {message}')
        logging.error(message)

    def info(self, message):
        print(f'INFO: {message}')
        logging.info(message)

    def warning(self, message):
        print(f'WARNING: {message}')
        logging.warning(message)


class RequestStuff():
    def __init__(self):
        self.address_url = 'api.fanyi.baidu.com'
        self.api_url = '/api/trans/vip/translate'
        self.fromLang = 'auto'
        self.toLang = 'zh'
        self.appid = mykey['appid']
        self.secretKey = mykey['secretKey']

    def mk_salt(self):
        return str(random.randint(32768, 65536))

    def mk_url(self, q):
        salt = self.mk_salt()
        sign = self.appid + q + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        return ''.join([self.api_url,
                        '?appid=' + self.appid,
                        '&q=' + urllib.parse.quote(q),
                        '&from=' + self.fromLang,
                        '&to=' + self.toLang,
                        '&salt=' + salt,
                        '&sign=' + sign])
