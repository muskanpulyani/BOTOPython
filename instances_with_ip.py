#. Script which will list all the Instances and associated IP Address,Provid  private  ip  if  instance is  stopped
#!/usr/bin/python
import  boto3
client = boto3.client('ec2')
data1={}
response=client.describe_instances()
for x  in  response['Reservations']:
	for  y in  x['Instances']:
		  z=y['State']
		  print(z['Name'])				
		  if z['Name']=='running':
			data1[y['InstanceId']]=y['PublicIpAddress']
		  else:
			data1[y['InstanceId']]=y['PrivateIpAddress']
print(data1)
