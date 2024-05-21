import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
        print(f'Bucket {bucket_name} created successfully.')
    except ClientError as e:
        print(f'Error occurred: {e}')
        return False
    return True

if __name__ == "__main__":
    bucket_name = 'paarthiban-paul-chamy'
    region = 'us-west-1'  # Specify the region, e.g., 'us-west-1', 'us-east-1', etc.
    create_s3_bucket(bucket_name, region)