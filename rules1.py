#!/usr/bin/python
import boto3
client = boto3.client('ec2')
data1={}
count=0
response = client.describe_security_groups( GroupIds=['sg-07350252ce189b72f'])
for x in response['SecurityGroups']:
        for  y in  x['IpPermissions']:
		if  'IpProtocol' in y:
			count=count+1
			data1[x['GroupId']]=count
	count=0
print(data1)
