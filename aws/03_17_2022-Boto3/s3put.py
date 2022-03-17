import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('test.txt', 'rb')
s3.Bucket('serdar-boto3-bucket').put_object(Key='test.txt', Body=data)
# Check the "xxxxxxxxx-boto3-bucket", if your script works fine, you should be able to see your test file in your bucket.