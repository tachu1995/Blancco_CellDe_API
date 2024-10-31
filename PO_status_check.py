import json
import requests
# import the AWS SDK (for Python the package name is boto3)



def lambda_handler(event, context):
    PO_number = event['PO_number']
    url = "GetPODetailsByPONumber"

    headers = {
      *********************************
    }

    payload = {
    "PurchaseOrderNumber": PO_number
    }

    data = json.dumps(payload)

    response = requests.post(url=url, data=data, headers=headers)

    if response.status_code == 200:
        code = 200
        json_response=response.json()
        data = {
            "PO_state" : json_response['Table1'][0]['POStatus'],
            "PO_ID" : json_response['Table1'][0]['PurchaseOrderID'],
            "PO_AM" : json_response['Table1'][0]['AccountManager']
            
        }

    
    return {
        'statusCode': code,
        'body': data
        }


