import boto3

print(boto3.__version__)

def number_buckets(num):
    client = boto3.client('s3')
    buckets = client.list_buckets()
    count = 0
    for bucket in buckets['Buckets']:
        print(f"Processing bucket number-[{count}]")
        if count < num:
            print(f"Bucket name is {bucket['Name']}")
            count += 1
        else:
            return
    
number_buckets(2)