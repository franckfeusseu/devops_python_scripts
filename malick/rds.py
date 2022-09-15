"""
  All About RDS. This will help to start ,list, stop rds instances without the need to go in aws console
  or aws cli.
"""

import  boto3

rds = boto3.client('rds')

"""
  Start one or a list of rds instances
"""
def start():
    pass

def stop(instance):
    res= rds.stop_db_instance(
        DBInstanceIdentifier=instance
    )
    return res

"""
  Give the status your rds's fleet
"""
def status():
    pass
