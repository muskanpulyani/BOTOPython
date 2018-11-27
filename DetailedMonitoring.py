#!/usr/bin/python
import boto3
data=[]
finaldata={}
client = boto3.client('ec2')
data={}
response=client.describe_instances()
print(response)
#for x in  response['Reservations']:
#	for  y in  x['Instances']:
#		print(y)
#		z=y['Monitoring']
#		print(z)
#		var=y['InstanceId']
#		data[var]=z['State']		
#print(data)
