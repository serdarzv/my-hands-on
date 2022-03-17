import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0dc44caa43a2748d2').stop()