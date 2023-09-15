import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']
REGION = os.environ['REGION']

ec2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    
    init_script = """#!/bin/bash
                yum update -y
                yum install -y httpd
                service httpd start
                """

    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        InstanceInitiatedShutdownBehavior='terminate', 
        UserData=init_script
    )

    instance_id = instance['Instances'][0]['InstanceId']
    print ("You have Launched EC2 :",instance_id)

    return instance_id
