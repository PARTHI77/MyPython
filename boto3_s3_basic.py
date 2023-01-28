import boto3
#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#	print(bucket.name)
client = boto3.client('s3')
bucket_name=str(input('please input bucket name: '))
print("Before delete the bucket we need to check it if is empty...")
objects = client.list_objects_v2(Bucket=bucket_name)
fileCount = objects['KeyCount']
if fileCount == 0:
	response = client.delete_bucket(Bucket=bucket_name)
	print("{} has been deleted successfully".format(bucket_name))