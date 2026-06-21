import json
import boto3
from datetime import datetime

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('ImageRecognitionData')

def lambda_handler(event, context):

    try:
        # Get S3 info
        bucket = event['Records'][0]['s3']['bucket']['name']
        image = event['Records'][0]['s3']['object']['key']

        print("Bucket:", bucket)
        print("Image:", image)

        # Detect labels
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': image
                }
            },
            MaxLabels=10,
            MinConfidence=75
        )

        labels = []

        print("Detected Labels:")

        for label in response['Labels']:
            print(label['Name'], label['Confidence'])

            labels.append(label['Name'])

        # Store in DynamoDB
        table.put_item(
            Item={
                'image_name': image,
                'bucket_name': bucket,
                'labels': labels,
                'upload_time': str(datetime.now())
            }
        )

        print("SUCCESS: Data stored in DynamoDB")

        return {
            'statusCode': 200,
            'body': json.dumps('Stored Successfully')
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
