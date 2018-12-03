#!/usr/bin/python
import boto3
import datetime
from datetime  import datetime
from datetime  import  date
from datetime import timedelta
import re
client = boto3.client('ec2')
response=client.describe_instances()
data={}
for x in  response['Reservations']:
	for  y in  x['Instances']:
		z=y['State']
		if  z['Name']=='stopped':
			
			var=y['StateTransitionReason']
	                var1=re.findall("\((.*)\)",var)
			#print(var1)
			starttime=datetime.now()
			#starttime=date.strftime(starttime,"%Y-%m-%d %H:%M:%S")	  	
                        #print(starttime)
		        for i  in range(len(var1)):
				endtime=datetime.strptime(var1[i],'%Y-%m-%d %H:%M:%S GMT')
				print(endtime)
				olddays=(starttime-endtime).days
				print(olddays)
		 		if  olddays > 1:
					print("the  instance is stopped  for more than  one day",y['InstanceId']) 

				else :
					continue	

		else:
			continue	

#startdate=datetime.now().days
#print(startdate)
