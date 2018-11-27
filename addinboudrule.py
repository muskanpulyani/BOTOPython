#!/usr/bin/python
import boto3
ec2 = boto3.resource('ec2')
security_group = ec2.SecurityGroup('sg-0317b686155d56b07')
response = security_group.authorize_ingress(IpProtocol="tcp",CidrIp="0.0.0.0/0",FromPort=3306,ToPort=3306)
print(response)
