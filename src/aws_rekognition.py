## This code utilizes the boto3 rekognition packages to analyze IMAGES ONLY.
import boto3
import logging

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
            'DEFAULT',
        ]
    )
    return response

if __name__ == "__main__":
    output = detect_faces('testing-aws-rekognition', 'KingInTheNorth.png')
    print(output)