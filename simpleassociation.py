#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.associate_address( PublicIp='13.232.85.216',
                InstanceId='i-0a7d61087afd16519',AllowReassociation=True)
print(response)

