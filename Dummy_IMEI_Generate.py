import json
import random
import requests

url = "*******************"

# Function to generate dummy IMEI
# This code was based on Script from lazyzhu.com, i have modified the code so that all IMEI generated will have the first 6 digits fixed as 991808
def imei_gen():
    # Generate the first 14 digits randomly
    imei_digits = "991808"
    last_imei_digits = ''.join(str(random.randint(0, 9)) for _ in range(8))
    imei_digits += last_imei_digits

    # Calculate the Luhn checksum
    checksum = 0
    for i, digit in enumerate(imei_digits):
        if i % 2 == 0:
            checksum += int(digit)
        else:
            checksum += sum(int(x) for x in str(int(digit) * 2))
    
    # Find the smallest number to make the checksum a multiple of 10
    if checksum % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (checksum % 10)
    
    # Return the IMEI
    imei = imei_digits + str(last_digit)
    return imei
    
    

def lambda_handler(event, context):
    
    imei = imei_gen()
    
    data = json.dumps({
        "imei" : imei
        })
    response = requests.post(url=url, data=data)
    # if the dummy imei is duplicated, it will generated another
    if response.status_code == 200:
        while response.json()["body"]["IsDuplicate"] == "YES":
            imei = imei_gen()
            data = json.dumps({
                "imei" : imei
                })
            response = requests.post(url=url, data=data)
       
    
    return {
        'statusCode': 200,
        'dummy_imei': imei
    }

