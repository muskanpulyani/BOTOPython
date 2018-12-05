#Find EBS snapshot using python boto
#!/usr/bin/python
import boto3
client=boto3.client('ec2')
response = client.describe_volumes()
data={}
for x in  response['Volumes']:
	#print(x['VolumeId'])
	#print(x['SnapshotId'])
	if x['SnapshotId']=='':
		continue
		#data[x['VolumeId']]=x['SnapshotId']
	else:
		data[x['VolumeId']]=x['SnapshotId']

print(data)	
