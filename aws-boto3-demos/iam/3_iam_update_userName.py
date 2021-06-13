import boto3

iam = boto3.client('iam')

iam.update_user(
    UserName = 'testboto3user',
    NewUserName = 'newboto3updatedUser'
    
)