#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.describe_security_groups()
data={}
data1=[]
for x in response['SecurityGroups']:
	for y in  x['IpPermissions'] :
		var=x['GroupId']
		for  z in  y['IpRanges'] :
			if z['CidrIp'] == '0.0.0.0/0':
				data1.append(y['FromPort']);
				print(data1)
			else:
				continue			
        data[var]=data1
	data1=[]
print(data)		
