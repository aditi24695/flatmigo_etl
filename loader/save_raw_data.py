import boto3

s3 = boto3.client('s3')
bucket_name = 'your-bucket-name'
file_path = 'local_file.txt'
s3_key = 'folder_name_in_s3/file_name.txt'

s3.upload_file(file_path, bucket_name, s3_key)