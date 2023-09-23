# Import the Boto3 library
import boto3

# Initialize the EC2 client with your AWS access key ID and secret access key
ec2 = boto3.client(
    'ec2',
    aws_access_key_id="",
    aws_secret_access_key=""
)

# Specify the list of EC2 instance IDs that you want to stop
instance_ids = [
    '',
    '',
    ''
]

# Use the `stop_instances` method to stop the specified EC2 instances
response = ec2.stop_instances(InstanceIds=instance_ids)

# Print the response from the AWS API (optional)
print("Response from AWS:", response)
