import boto3
import json
from dotenv import load_dotenv
import os

load_dotenv()
try:
    region = os.getenv('REGION')
    access_key = os.getenv('AWS_ACCESS_KEY_ID')  # should have .env where access key and secret key stored
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')


    session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
    )    
    rds_client = session.client('rds',region)
    response = rds_client.describe_db_instances(
    MaxRecords=100,
    Marker='string'
    )

    print (json.dumps(response,indent=4,default=str))

except Exception as e:
    print(f"Unexpected error: {e}")    