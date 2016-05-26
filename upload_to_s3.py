import os
import yaml
import boto3
from boto3.session import Session

with open("config.yml", 'r') as conf_file:
    config = yaml.load(conf_file)


session = Session(aws_access_key_id=config.get('aws').get('AWS_ACCESS_KEY_ID'),
                  aws_secret_access_key=config.get('aws').get('AWS_SECRET_ACCESS_KEY'))
s3 = session.resource('s3')


def upload(file_path):

    bucket = s3.Bucket(config.get('aws').get('S3_BUCKET_NAME'))
    data = open(file_path, 'rb')
    s3.Object('test.py').put(key='test.py', body=data)

upload('run.py')
