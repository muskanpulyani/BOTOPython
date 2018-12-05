#
#!/usr/bin/python
import boto3
import  re
import datetime
from  datetime  import datetime 
from  datetime  import  date
from datetime import timedelta
client=boto3.client('iam')
#response = client.list_access_keys()
#print(response)
data={}
response=client.list_users()
for  x in response['Users']:
	
        var=x['CreateDate']
	var1=datetime.strftime(var,'%Y-%m-%d %H:%M:%S')
	var2=datetime.strptime(var1,'%Y-%m-%d %H:%M:%S')
	#print(var2)
	#print(var1)
	currenttime=datetime.now()
	#print(currenttime)
	diffrence=(currenttime-var2).days
	#print(diffrence)
	if  diffrence > 35:
		data[x['UserName']]=diffrence	
	else:
		continue
print("the user  having 35 days  older access  keys",data)
