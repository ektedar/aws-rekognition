# AWS With Boto3

This repo uses the python package boto3 to upload a video into an S3 bucket and run Amazon Rekognition on it to get facial detection. 

## Dependencies

You will need Python 3.5 or above. To use the library you will require the `boto3` python package. 

```
pip install boto3
```

## AWS

To be able to connect to the AWS Resources you will need to connect to your AWS Account with your secret Access Keys IDS:

### Windows

Create a `C:\Users\USERNAME\.aws\credentials` directory and with the following information

```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
region = your_aws_region
```

### MacOS

From your shell do the following:

```bash
cd ~
mkdir .aws
touch .aws/credentials
```

Open the `credentials` file and insert the information as necessary:

```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
region = your_aws_region
```

## How to Run


### Uploading a video file to be used

To upload a file into your S3 Bucket, provide the `filename` and the `bucketname` directly from the command line like so.

```cmd
python src/upload_to_s3.py --filename JonSnow.mp4 --bucketname your-bucket
```

If successful, you should see the following in the command line output:

```cmd
INFO:botocore.credentials:Found credentials in shared credentials file: ~/.aws/credentials
INFO:root:JonSnow.mp4 has been uploaded into the bucket your-bucket
```

NOTE: If you specify a directory for the `filename` argument, S3 will follow the same directory structure in the bucket. i.e. if you enter `data/JonSnow.mp4` as the argument for `filename`, There will be a folder in S3 called `data` with `JonSnow.mp4` inside it. 