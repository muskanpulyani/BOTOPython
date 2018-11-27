#!/usr/bin/python
import boto3
ec2 = boto3.resource('ec2')
security_group = ec2.SecurityGroup('sg-0317b686155d56b07')
tag = security_group.create_tags(
   Tags=[
        {
            'Key': 'name',
            'Value': 'muskan'
        }
    ]
)
print(tag)
