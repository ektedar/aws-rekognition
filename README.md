# AWS With Boto3

This repo uses the python package boto3 to upload a video into an S3 bucket and run Amazon Rekognition on it to get facial detection. 

## Dependencies

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

