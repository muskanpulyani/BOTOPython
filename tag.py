#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.describe_instances()
data=[]
for  x in  response['Reservations']:
	for  y in  x['Instances']:
		for z in  y['Tags']:
#			print(z['Value'])
			if z['Value'] == 'Env':
#				print(y['InstanceId'])
				data.append(y['InstanceId'])
			else: 
				continue
print("instances having tag  env ",data)
