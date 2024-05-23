import boto3
import os
from dotenv import load_dotenv
load_dotenv()

region = os.environ.get('AWS_REGION')
boto3.setup_default_session(region_name=region)

s3 = boto3.client('s3')
bucket_name = os.environ.get('S3_BUCKET')
s3.upload_file('test.txt', bucket_name, 'test.txt')

ddb = boto3.client('dynamodb')
table_name = os.environ.get('DDB_TABLE')
item = {
    'id': { 'S': 'my-first-item' },
    'message': { 'S': 'write successful!' },
    'number': { 'N': '1' }
}
ddb.put_item(TableName=table_name, Item=item)
