"""
  All About Ec2. This will help to start ,list, stop ec2 instances without the need to go in aws console
  or aws cli.
"""

import boto3

ec2 = boto3.client('ec2')


def instances_id(tags=None, state=None) ->list:
    """
     Get the instances IDs based on the filter
    """
    result = []
    response = ec2.describe_instances()
    instances = response['Reservations'][0]['Instances']

    for i in instances:
       result.append(i['InstanceId'])
    return result

def start_instances(ids, **kwargs):
    """
      Start the given instances
    """
    #start instances
    ec2.start_instances(InstanceIds=ids)


def stop_instances(ids, **kwargs):
    """
       Stop the given Instances
    """
    ec2.stop_instances(InstanceIds=ids)


def status():
    """
    Get the status of given instances
    """
    pass