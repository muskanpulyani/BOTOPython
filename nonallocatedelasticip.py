#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.describe_addresses()
data={}
data1=[]
print(response.keys())
for  x in  response['Addresses']:
	 if 'AssociationId' in x:
		data[x['InstanceId']]=x['PublicIp']
	 else:
		data1.append(x['PublicIp'])
print("Used elastic ip",data)
print("un allocated  elastic ip",data1)			
