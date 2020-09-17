## Unit test for testing creating a bucket
import pytest
import boto3
from src.create_bucket import create_bucket
from src.upload_to_s3 import upload_to_s3
from moto import mock_s3


@mock_s3
def test_upload_to_s3():
    bucketname = "test-bucket-ektedar"
    filename = "./images/Rekognition_face_example.PNG"

    create_bucket(bucketname, "private")
    s3_client = boto3.client("s3", region_name="us-east-1")
    response = s3_client.list_buckets()
    upload_to_s3(bucketname, filename)
    file = s3_client.list_objects(Bucket=bucketname)

    assert response["Buckets"][0]["Name"] == bucketname
    assert file["Contents"][0]["Key"] == filename
