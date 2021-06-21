import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
ec2.start_instances(InstanceIds= ['i-0a0529d30539aca88'])


