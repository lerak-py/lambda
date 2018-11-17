import json
import requests
print('In the function')
def lambda_handler(event, context):
    # TODO implement
    r = requests.get("https://google.com")
    print(r.url)
    print(r.text)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
