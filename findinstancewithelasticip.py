#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response1=client.describe_instances()
data=[]
for y  in  response1['Reservations']:
	for  z  in y['Instances']:
		data.append(z['InstanceId'])
response=client.describe_addresses()
for x in  response['Addresses']:
	if  'AssociationId' in  x:
		for  i  in  data:
			if i == x['InstanceId']:
				print('this  instance is  connetced  with elastic  ip :',x['InstanceId'])			
			else:
				continue
	else :
		continue;
