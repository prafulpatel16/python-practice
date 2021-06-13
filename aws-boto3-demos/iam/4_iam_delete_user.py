import boto3

iam = boto3.client('iam')

iam.delete_user(
    UserName = 'newboto3updatedUser'
)

response = client.list_server_certificates(
    PathPrefix='string',
    Marker='string',
    MaxItems=123
)