import boto3
import time
"""
#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#	print(bucket.name)
#Create S3 Bucket
"""

client =boto3.client('s3')
bucket_name=str(input('Enter the bucket name to be created: '))
response1 = client.create_bucket(
	ACL='private',
	Bucket=bucket_name
)

tag_resp=str(input('Enter "y" if you want to tag your bucket?: '))

if tag_resp == 'y':
	tag_key=str(input("Please enter key for the tag: "))
	tag_value = str(input("Please enter value of the tag: "))
	response2 = client.put_bucket_tagging(
	Bucket=bucket_name,
	Tagging={
		'TagSet': [
			{
				'Key': tag_key,
				'Value': tag_value
		}
	]
})
time.sleep(60)
#
#Delete S3 Bucket
#
client = boto3.client('s3')
bucket_name=str(input('please input bucket name to be deleted: '))
print("Before delete the bucket we need to check it if is empty...")
objects = client.list_objects_v2(Bucket=bucket_name)
fileCount = objects['KeyCount']
if fileCount == 0:
	response = client.delete_bucket(Bucket=bucket_name)
	print("{} has been deleted successfully".format(bucket_name))
