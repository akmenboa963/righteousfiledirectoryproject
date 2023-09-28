#Create a Standard SQS Queue using Python


import boto3  

# Create an SQS resource object
sqs = boto3.resource('sqs')

# Define a unique queue name for your project
queue_name = 'ApexHolisticHealthOrdersSQS'

# Create the queue with the specified name
queue = sqs.create_queue(QueueName=queue_name)

# Print a success message along with the URL of the created queue
print(f"Successfully created the '{queue_name}' queue with URL: {queue.url}")# Import the Boto3 library

#send a Message to the SQS Queue.

import boto3
from datetime import datetime
import json

# Get the current date & time
current_datetime = datetime.now()

# Create a customized message with the current date & time
message_body = "This is a unique message. The current date and time is: " + current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Initialize the SQS client
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    # Send the message to the specific SQS queue (Replace with your queue URL)
    queue_url = 'https://sqs.us-east-1.amazonaws.com/821709377806/ApexHolisticHealthOrdersSQS'  # Replace with your queue URL
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        success_message = "Message sent successfully to the SQS queue."
    else:
        success_message = "Failed to send the message to the SQS queue."

    return {
        'statusCode': 200,
        'body': json.dumps(success_message)

  # SNS Email topic creation 

  import boto3

# Initialize SNS client
sns_client = boto3.client('sns')

# Specify the email address to subscribe
email_address = 'apexholistichealth@gmail.com'

# Step 1: Create an SNS topic
topic_name = 'ApexHolisticHealthSNS'  # Replace with your desired topic name
try:
    response = sns_client.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print("SNS topic created with ARN:", topic_arn)
except Exception as e:
    print("Error creating SNS topic:", str(e))
    exit(1)

# Step 2: Subscribe the email address to the SNS topic
try:
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',  # Communication protocol
        Endpoint=email_address
    )

    # Get the subscription ARN from the response
    subscription_arn = response['SubscriptionArn']

    print("Subscribed email address:", email_address)
    print("Subscription ARN:", subscription_arn)
    print("Subscription successful.")
except Exception as e:
    print("Error subscribing email address:", str(e))
