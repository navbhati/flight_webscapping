import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/GBP/en-US/LHR/DEL/2021-08-15"

querystring = {"inboundpartialdate":"2021-08-28"}

headers = {
    'x-rapidapi-key': "c5793d7cafmshf6f023ddc0f0f5ep11116cjsndb8f319ec001",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)