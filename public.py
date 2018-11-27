#!/usr/bin/python
import boto3
client=boto3.client('s3')
response=client.list_buckets()
var=response['Buckets']
#print(var)
data=[]
i=0
print("the number of buckets are:", len(var));
for  i in range(5):
         var2=var[i];
         data.append(var2['Name'])      
print("the  buckets  in s3 are :" , data)
for x in data:
	response1=client.get_bucket_acl(Bucket=x)		               
	var=response1['Grants']
	n=len(var)
        for i in range(n) :
		var2=var[i]
		var3=var2['Grantee']
		if var3['Type'] == "Group":
			print("The given  bucket",x,"public")
                        break	
		else:
			continue
