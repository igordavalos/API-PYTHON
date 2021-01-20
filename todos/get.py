import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

<<<<<<< HEAD
    # create a response for get method
=======
    # create a response for get method in new-feature-one
>>>>>>> 94b70924803d969c63bb8f08341bcb8d8c13a461
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
