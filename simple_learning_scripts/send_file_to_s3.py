'''
ABOUT: THIS IS A PYTHON SCRIPT THAT CAN BE USED TO SEND FILES FROM A LOCAL SOURCE TO S3 BUCKET
       IT CAN BE USED IN CICD PIPELINES OR EVEN ANY PROCESS
       JUST HELPS AUTOMATE THE PROCESS
'''
import boto3
import os

# Function to send a file to S3 bucket
def send_to_do_s3():
  space_access_key = os.environ.get('SPACE_ACCESS_KEY')
  space_access_secret= os.environ.get('SPACE_ACCESS_SECRET')

  session = boto3.session.Session()
  client = session.client('s3',
                          region_name=f'{s3_region}', # region of s3 bucket
                          endpoint_url=f'{s3_url}', # endpoint url of s3 bucket
                          aws_access_key_id=f'{s3_access_key}', # s3 access key
                          aws_secret_access_key=f'{s3_access_secret}') # s3 access secret

  client.upload_file(f'{src_file}',  # Path to file in local 
                    f'{bucket_name}',  # Name of s3 bucket
                    f'{dst_file}')  # Name for file as to be stored in s3 bucket

send_to_do_s3()
