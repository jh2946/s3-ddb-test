import boto3
import os
from dotenv import load_dotenv
load_dotenv

s3 = boto3.client('s3')
bucket_name = os.environ.get('S3_BUCKET')
s3.upload_file('test.txt', bucket_name, 'test.txt')

ddb = boto3.client('dynamodb')
table_name = os.environ.get('DDB_TABLE')
item = {
    'id': { 'S': 'my-first-item' },
    'message': { 'S': 'hello world!' },
    'number': { 'N': '1' }
}
ddb.put_item(TableName=table_name, Item=item)
