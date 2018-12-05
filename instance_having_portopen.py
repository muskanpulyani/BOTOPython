#Script to list all the Instances having port 22 open for all IP [ 0.0.0.0/0 ]
#!/usr/bin/python
import boto3
client=boto3.client('ec2')
data=[]
response=client.describe_instances()
for x in response['Reservations']:
	for y in  x['Instances']:
		for  z in y['SecurityGroups']:
			var=z['GroupId']
			response = client.describe_security_groups(GroupIds=[var])
			#print(response.keys())			
			for i in response['SecurityGroups']:
				for j in i['IpPermissions']:
					if j['FromPort']==22:
						for z in  j['IpRanges']:
							if z['CidrIp']=='0.0.0.0/0':
								data.append(y['InstanceId'])						
					else:
						continue
print("Instances  having  port 22  open  for  all",data)
                                      
