import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')

def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    item = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
   
    # use translate lambda method to get translated text
    translateClient = boto3.client('translate')
    result = translateClient.translate_text(
        Text=item['Item']["text"],
        SourceLanguageCode='auto',
        TargetLanguageCode=event['pathParameters']['language']
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result["TranslatedText"], ensure_ascii=False).encode('utf8')
    }

    return response
