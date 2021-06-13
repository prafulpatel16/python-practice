import boto3

iam = boto3.client('iam')

response = boto3.client.create_policy(
    PolicyName='string',
    Path='string',
    PolicyDocument='string',
    Description='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)