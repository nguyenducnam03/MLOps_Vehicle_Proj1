'''
Study how to upload/download file from S3 bucket
'''
import os
from dotenv import load_dotenv

import boto3
# Load variables from .env file
load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION")


# # Create boto3 session using loaded credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# compare resource and client
s3 = session.resource('s3')
s3_client = session.client('s3')

# ✅ Using resource (high-level)
# bucket = s3.Bucket('testbucker1namven')
# bucket.upload_file('local_file.txt', 's3_file.txt')  # U

# ✅ Using client (low-level)
# s3_client.upload_file('projectflow.txt', 'testbucker1namven', 'uploads/projectflow.txt')  # Upload file to S3 bucket

# ✅ Using resource
# bucket = s3.Bucket('your-bucket-name')
# bucket.download_file('s3_file.txt', 'downloaded_file.txt')

# ✅ Using client
# s3_client.download_file('your-bucket-name', 's3_file.txt', 'downloaded_file.txt')

















# Command prev
# s3 = session.resource('s3')
# # Get bucket
# bucket = s3.Bucket('testbucker1namven')


# Upload files to S3 bucket
# bucket.upload_file('projectflow.txt', 'uploads/projectflow.txt')

# Print all obj in bucket
# for obj in bucket.objects.all():
#     print(obj.key)

# Download files from S3 bucket
# bucket.download_file('uploads/projectjflow.txt', 'local_file.txt')

# Delete obj
# obj = s3.Object('testbucker1namven', 'uploads')
# obj.delete()

# Delete all objects that start with 'uploads/'
# for obj in bucket.objects.filter(Prefix='uploads/'):
#     print(f"Deleting: {obj.key}")
#     obj.delete()

# Create a folder in S3 bucket
# bucket.put_object(Key='my_folder_name/')

# Check or modify object permissions (ACLs)
# obj = s3.Object('my-model-mlopsproj-nam', 'uploads/local_file.txt')
# obj.Acl().put(ACL='public-read')  # or 'private', etc.