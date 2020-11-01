import boto3
import logging
import pprint
import os
from botocore.exceptions import ClientError

#define the connection
ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    # revive them
    print('start ec2')
    revive_ec2(env)

def revive_ec2(env):

    # you can put instance id you want to start instead of $instance_id.
    targetEC2Instances = ['${instance_id}']

    print (targetEC2Instances)
    try

        # start instance only stopped status.
        for instanceId in targetEC2Instances:
            print(instanceId)

            filters = [{
                'Name': 'instance-id',
                'Values': [instanceId]
            }]
            result = ec2.describe_instances(Filters=filters)
            instanceStatus = result['Reservations'][0]['Instances'][0]['State']['Name']
            if instanceStatus == 'stopped':
                PowerOn = ec2.start_instances(
                    InstanceIds=[
                        instanceId,
                    ],
                )
            else:
                print (instanceId + ' is not stopped status')
    except ClientError as e:
        print('exceptin: %s' % e)