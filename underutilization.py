#!/usr/bin/python
import boto3
import datetime
from  datetime  import  datetime
from datetime  import   timedelta
data=[]
count=0
sum=0
client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-0a7d61087afd16519'
        },
    ],
    StartTime=datetime.now()-timedelta(days=7),
    EndTime=datetime.now(),
    Period=43200,
    Statistics=['Average'],
1    Unit='Percent')
print(response['Datapoints'])
for x in response['Datapoints']:
	data.append(x['Average'])
	sum=sum+x['Average']
	count=count+1
print(data)
print(count)
print(sum/count)

   # EndTime=datetime(2015, 1, 1),
    #Period=123,
    #Statistics=[
     #   'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum',
    #]
