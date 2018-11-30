#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response=client.describe_images(ImageIds=['ami-0fa931e70104cf960'])
print(response)
