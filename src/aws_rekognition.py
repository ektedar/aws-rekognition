## This code utilizes the boto3 rekognition packages to analyze IMAGES ONLY.
import boto3
import logging
import argparse

def detect_faces(bucketname, image):
    """
    Provided a bucketname and an image within that bucket, return the detected_faces
    """
    client = boto3.client('rekognition')
    response = client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucketname,
                'Name': image
            }
        },
        Attributes=[
            'ALL',
        ]
    )
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''
        This python file will return an dict for the facial detection that was run over the provided image. This is assuming your data exists in the provided S3 Bucket. 
        This will print an dict with the facial results if called directly. Refer to boto3 AWS Rekognition for more info.
        '''
    )

    parser.add_argument(
        '-f',
        '--filename',
        required=True,
        help='This is the filename of the object that you are trying execute facial detection on.'
    )

    parser.add_argument(
        '-b',
        '--bucketname',
        required=True,
        help='This is the bucket name of the S3 bucket where the file is residing'
    )
    args = parser.parse_args()
    output = detect_faces(args.bucketname, args.filename)
    print(output)