import argparse
import boto3
import logging

# Route Logging information
logging.basicConfig(level=logging.INFO)

def upload_to_s3(bucket_name, file_name):
    """
    Upload a file into a S3 Bucket provided with the proper credentials
    """
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)
    logging.info('{} has been uploaded into the bucket {}'.format(file_name, bucket_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This python file will upload a specified document into an AWS s3 bucket'
    )

    parser.add_argument(
        '-f',
        '--filename',
        required=True,
        help='This is the filename of the object that you are trying to upload to your S3 Bucket'
    )

    parser.add_argument(
        '-b',
        '--bucketname',
        required=True,
        help='This is the bucket name of the S3 bucket where the file will be uplaoded'
    )
    args = parser.parse_args()


    ## Calling the main function to do the upload
    upload_to_s3(args.bucketname, args.filename)