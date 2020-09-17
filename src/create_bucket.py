import logging
import boto3
import argparse
from botocore.exceptions import ClientError


def create_bucket(bucket_name, permission, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name, 
                                    ACL='private')
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location,
                                    ACL=permission)
    
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This python file will upload a specified document into an AWS s3 bucket'
    )

    parser.add_argument(
        '-r',
        '--region',
        required=False,
        help='Region name of where the bucket will be created'
    )

    parser.add_argument(
        '-p',
        '--permission',
        default='authenticated-read',
        required=False,
        help='The permission of the bucket. The bucket is private by default. The following values can be used "private"|"public-read"|"public-read-write"|"authenticated-read"'
    )

    parser.add_argument(
        '-b',
        '--bucketname',
        required=True,
        help='This is the bucket name of the S3 bucket'
    )
    args = parser.parse_args()


    ## Calling the main function to do the upload
    create_bucket(args.bucketname, args.permission, args.region)