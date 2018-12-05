#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response1=client.describe_instances()
data=[]
data1={}
for y  in  response1['Reservations']:
        for  z  in y['Instances']:
                data.append(z['InstanceId'])
response=client.describe_addresses()
for x in  response['Addresses']:
        if  'AssociationId' in  x:
                for  i  in  data:
                        if i == x['InstanceId']:
				data1[i]=x['PublicIp']
                                print('this  instance is  connetced  with elastic  ip :',x['InstanceId'])
                        else:
                                continue
        else :
                continue;
print(data1)
for  x in data1:
	if data1[x]=='13.233.69.89':
		print("this is  attached  with correct  elastic ip")
	else:
		print("this is not  elastic ip")
		response = client.disassociate_address(
      		          PublicIp=data1[x])
		print(response)
		response=client.associate_address( InstanceId=x,
                PublicIp='13.233.69.89')
		print(response)
