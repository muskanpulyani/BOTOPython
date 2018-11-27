#!/usr/bin/python
import boto3
client=boto3.client('s3')
response=client.list_buckets()
var=response['Buckets']
i=0
data=[]
print("the number of buckets are:", len(var));
for  i in range(5):
         var2=var[i];
         data.append(var2['Name'])      
print("the  buvkets  in s3 are :" , data)
for x in data:
	response1=client.list_objects(Bucket=x)
	print(response1)
