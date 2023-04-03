# python script.py create
# python script.py start --instance-id i-0123456789abcdef0
# python script.py stop --instance-id i-0123456789abcdef0
# python script.py terminate --instance-id i-0123456789abcdef0
#
#
#
#

import boto3
import argparse

# Initialize the client to work with EC2
ec2 = boto3.client('ec2')


def create_instance():
    # Creating new EC2 instance
    instances = ec2.run_instances(
        ImageId='ami-0c94855ba95c71c99', # AMI (Amazon Machine Image) 
        InstanceType='t2.micro', # Instance type
        MinCount=1,
        MaxCount=1,
        KeyName='mykey', # key-pair name
        SecurityGroups=['default'] # Security Group name for instance
    )

    # Getting IDS for created instances 
    instance_ids = [instance['InstanceId'] for instance in instances['Instances']]
    print(f"Instance created with IDs: {instance_ids}")


def stop_instance(instance_id):
    # Stopping EC2 Instance
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} stopped")


def start_instance(instance_id):
    # Starting EC2 Instance
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} started")


def terminate_instance(instance_id):
    # Terminatting EC2 Instance
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} terminated")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EC2 Instance Management')
    parser.add_argument('action', choices=['create', 'start', 'stop', 'terminate'], help='Action to perform')
    parser.add_argument('--instance-id', help='Instance ID to perform action on')

    args = parser.parse_args()

    if args.action == 'create':
        create_instance()
    elif args.action == 'start':
        start_instance(args.instance_id)
    elif args.action == 'stop':
        stop_instance(args.instance_id)
    elif args.action == 'terminate':
        terminate_instance(args.instance_id)