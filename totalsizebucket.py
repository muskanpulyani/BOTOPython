#!/usr/bin/python
import boto3
client=boto3.client('s3')
response=client.list_buckets()
var=response['Buckets']
i=0
data=[]
total=0
print("the number of buckets are:", len(var));
for  i in range(1,5):
         var2=var[i];
         data.append(var2['Name'])      
print("the  buvkets  in s3 are :" , data)
for x in  data:
	response1=client.list_objects(Bucket=x)
	#print(response1.keys())
	var3=response1['Contents']
	n=len(var3)
	#print(n)
	for i in range(n):
		var4=var3[i]
		total=var4['Size'] + total
	print("The  Size of the  bucket",x,"is",total)
	total=0
