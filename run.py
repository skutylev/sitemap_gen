# -*- coding: utf-8 -*-
import celery
import requests
import datetime
import time
from sitemap_gen import gen_sitemap
from upload_to_s3 import upload

@celery.task(name='sitemap_gen_run')
def main(type_addr):

    page_size = 1
    page = 1
    days = 365

    params = {
        'api_url': 'https://api.naviaddress.com/api/v1',
        'type': type_addr,
        'page_size': page_size,
        'page': page,
        'last_update': time.mktime((datetime.datetime.now() - datetime.timedelta(days=days)).timetuple())
    }

    request_headers = {
        'accept': 'application/json',
        'platform': 'web',
        'app-version': '1.0.0',
        'auth-token': '1cb7e1cd8e8254f549145691e37be987'
    }

    request_url = '{}/sitemap/{}?page_size={}&page={}&last_update={}'.format(params.get('api_url'),
                                                                             params.get('type'),
                                                                             params.get('page_size'),
                                                                             params.get('page'),
                                                                             params.get('last_update'))

    response = requests.get(url=request_url, headers=request_headers).json()
    navi_addresses_count = int(response.get('navi_addresses_count'))

    print(navi_addresses_count)

    gen_sitemap(response=response)


main(type_addr='naviaddresses')