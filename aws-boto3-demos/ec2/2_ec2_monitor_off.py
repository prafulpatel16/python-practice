import sys
import boto3

ec2 = boto3.client('ec2')

if sys.argv[1] == 'ON':
    response = ec2.monitor_instance(InstaceIds=['INSTANCE_ID'])
else:
    response = ec2.monitor_instance(InstaceIds=['INSTANCE_ID'])
print (response)
