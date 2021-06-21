from os import read
from typing_extensions import runtime
import boto3
import botocore
import sys
import logging

def create_lambda(name):
    try:
        client = boto3.client('lmabda')
        filepath = "./4_ec2_startec2instance.rar"

        client.create_function(
            functionaName=name,
            Runtime='python3.8',
            Role="arn:aws:iam::821419042007:role/service-role/prafulcloud-web-role-n5a7ekmt",
            Handler='{}.lambda_handler'.format('create_lambda'),
            code={'Zipfile': open(filepath,'rb').read(),},
        )
    except botocore.exception.ClientError as error:
        raise error
    except botocore.exception.ResourceConflictExeception as conflict:
        print(conflict)
    except botocore.exception.ParamValidationError as e:
        logging.exception('Parameter Validation: %' & e)

    name = sys.argv[1]

    if __name__ == '__main__':
        create_lambda(name)




      

