https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html

Resources
Overview
Resources represent an object-oriented interface to Amazon Web Services (AWS). They provide a higher-level abstraction than the raw, low-level calls made by service clients. To use resources, you invoke the resource() method of a Session and pass in a service name:

# Get resources from the default session
sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')
Every resource instance has a number of attributes and methods. These can conceptually be split up into identifiers, attributes, actions, references, sub-resources, and collections. Each of these is described in further detail below and in the following section.

Resources themselves can also be conceptually split into service resources (like sqs, s3, ec2, etc) and individual resources (like sqs.Queue or s3.Bucket). Service resources do not have identifiers or attributes. The two share the same components otherwise.

Session
Overview
A session manages state about a particular configuration. By default, a session is created for you when needed. However, it's possible and recommended that in some scenarios you maintain your own session. Sessions typically store the following:

Credentials
AWS Region
Other configurations related to your profile
Default session
Boto3 acts as a proxy to the default session. This is created automatically when you create a low-level client or resource client:

import boto3

# Using the default session
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')
Custom session
You can also manage your own session and create low-level clients or resource clients from it:

import boto3
import boto3.session

# Create your own session
my_session = boto3.session.Session()

# Now we can create low-level clients or resource clients from our custom session
sqs = my_session.client('sqs')
s3 = my_session.resource('s3')
Session configurations
You can configure each session with specific credentials, AWS Region information, or profiles. The most common configurations you might use are:

aws_access_key_id - A specific AWS access key ID.
aws_secret_access_key - A specific AWS secret access key.
region_name - The AWS Region where you want to create new connections.
profile_name - The profile to use when creating your session.