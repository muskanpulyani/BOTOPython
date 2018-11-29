#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response = client.describe_instances();
for x in response['Reservations']:
	for  y in  x['Instances']:
		z='VpcId'
		#if  len(z) != 0:
		#	print("th"the instance in  ec2-vpc",y['InstanceId'e instance in  ec2-vpc",y['InstanceId'])
		#else :
		#	continue		
		if z in y :
			print("the instance in  ec2-vpc",y['InstanceId'])
		else:
			continue;
