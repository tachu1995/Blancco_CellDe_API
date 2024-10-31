import requests
import json
# import two packages to help us with dates and date formatting
from time import gmtime, strftime




#API Calling Address
url = "Quote_Confirm_Complete"

#API Header
headers = {
*************************************
}


def lambda_handler(event, context):
    
    
    PO_ID = event["PO_ID"] #checked
    PO_number = event["PO_number"] #checked
    imei = event["imei"] #checked
    SKU = event["SKU"]
    product_name = event["model"] #checked
    device_color = event["color"] #checked
    device_grade = event["combine_grade"]
    start_time = event["time"]
    
    if imei == "":
        return {
            # Code 205, empty IMEI string
            'statusCode': 205
            }
    
    
    payload = {
    "POdetails": [
        {
        "IsQuantityDisable": "true", 
        "DeviceCondition": "Working Old Device",
        "ProductDescription": product_name,
        "SKUID": SKU,
        "DeviceQuantity": 1,
        "DeviceColor": device_color,
        "DeviceCombineGrade": device_grade,
        "UnitPrice": 10, #unchange price as Owen will price PO by himself
        "UnitTax": 0,
        "TotalTax": 0,
        "TotalPrice": 10, #unchange price as Owen will price PO by himself
        "BasePrice": 10,
        "IsUpdate": "NO",
        "IMEI": imei,
        "CatalogPartnerPricingID": 353961,
        "DeviceCategoryID": 1,
        "IsHardResetChecked": "true",
        }
    ],
    "EnterprisePartnerID": 5,
    "StoreID": 7,
    "UserID": 15898,
    "LocationID": 1,
    "PurchaseOrderID": PO_ID,
    "PurchaseOrderNumber": f"PO-{PO_number}",
    "PricingProfileID": 2,
    "SumOfDeviceQuantity": 1,
    "SumOfPrice": 10, #unchange price as Owen will price PO by himself
    "SumOfTotalTax": 0,
    "SumOfTotalPrice": 10 #unchange price as Owen will price PO by himself
    }


    data = json.dumps(payload)
    # DO NOT RUN UNTIL WE ARE SURE THAT THE PARAMETER IS CORRECT
    response = requests.post(url=url, data=data, headers=headers)

    json_response=response.json()
    # Check status code to be 200
    if response.status_code != 200:
        return {
            'statusCode': 201
            }
    # adding device failed
    if json_response[0]==None:
        return {
            'statusCode': 202
            }
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'OrderStatus':json_response[0]["OrderStatus"],
        "time": start_time
        }
