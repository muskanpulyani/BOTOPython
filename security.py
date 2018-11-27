#!/usr/bin/python
import  boto3
client=boto3.client('ec2')
response = client.update_security_group_rule_descriptions_ingress(
    GroupId='sg-0317b686155d56b07',
    IpPermissions=[
        {
            'FromPort': 8080,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': "this can be changed"
                },
            ],
	'ToPort': 8080
	}
	]
)
print(response)
