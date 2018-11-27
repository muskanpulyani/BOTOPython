#!/usr/bin/python
import boto3
client = boto3.client('ec2')
response1 = client.describe_instances()
data=[]
data2=[]
data3=[]
var=response1['Reservations']
n=len(var)
for i in range (n) :
	var2=var[i]
	for y in  var2['Instances']:
		  data.append(y['SecurityGroups'])
#print(data)
for x in  data:
	data1=x[0];
#	print(data1['GroupId'])
	data2.append(data1['GroupId'])
#print("the used  securtiy groups  are",data2)
n3=len(data2)
print("the used  security groups",n3)
response = client.describe_security_groups()
var4=response['SecurityGroups']
n=len(var4)
for i in  range(n):
	var5=var4[i]
#	print(var5['GroupId'])
	data3.append(var5['GroupId'])
#print(data3)	
print("the  total security groups",len(data3))
#now  compare data2 and  data3 to find  unused  security group
#data3 total  groupid
#data2 used  groupuid
n1=len(data2)
n2=len(data3)
for x in data2:
	data3.remove(x)
#print(data3)
n=len(data3)
print("the unused  one",n)
