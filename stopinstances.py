# Import the Boto3 library
import boto3

# Initialize the EC2 client with your AWS access key ID and secret access key
ec2 = boto3.client(
    'ec2',
    aws_access_key_id="AKIA36UNSCEHB7C2MUAO",
    aws_secret_access_key="utW/LjVGI9GFGYsIvx2hd9pbx3s54q5LwdeWk5UC"
)

# Specify the list of EC2 instance IDs that you want to stop
instance_ids = [
    'i-0786ec37366800c48',
    'i-08f16cef0d7f789ae',
    'i-0698085b4407efa85'
]

# Use the `stop_instances` method to stop the specified EC2 instances
response = ec2.stop_instances(InstanceIds=instance_ids)

# Print the response from the AWS API (optional)
print("Response from AWS:", response)
