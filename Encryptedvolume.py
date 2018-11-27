#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.describe_volumes()
print(response.keys())
for x in response['Volumes']:
	 if  x['Encrypted'] == 'True':
		print("the  volume is  encrpted")
	 else:	continue
