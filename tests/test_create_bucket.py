## Unit test for testing creating a bucket
import pytest
import boto3
from src.create_bucket import create_bucket
from moto import mock_s3

@mock_s3
def test_create_bucket():
    bucketname = 'test-bucket-ektedar'
    create_bucket(bucketname, 'private')
    s3_client = boto3.client('s3', region_name='us-east-1')
    response = s3_client.list_buckets()
    # Output the bucket names
    print(response)
    assert response['Buckets'][0]['Name'] ==bucketname