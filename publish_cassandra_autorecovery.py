#!/usr/bin/python
import boto3
import socket
import sys
from time import gmtime, strftime
import os

host_name = socket.gethostname()
date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
#sns_message_file = sys.argv[1]

#AWS Credential
REGION = ''
ACCESS_KEY = ''
SECRET_KEY = ''
ARN = 'arn:aws:sns:us-east-1:633834615594:svmc-dba'

#Message contents
SUBJECT = "[SPPbot][DBA] Autorecovery Script Started on " + host_name + " / " + date_time
#SNS message - get from file
#if os.path.exists(sns_message_file):
#	file = open(sns_message_file,"r")
#	MESSAGE = file.read()
#	os.remove(sns_message_file)
#else:
#	MESSAGE = sns_message_file + " does not existed. Please check :("
MESSAGE = str(sys.argv)

#Send message
client = boto3.client(
	'sns',
	aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY,
	region_name = 'us-east-1'
)

response = client.publish(
		TopicArn = ARN,
		Message = MESSAGE,
		Subject = SUBJECT
)

print("Response: {}".format(response))
