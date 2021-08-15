import requests

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    user_input = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()

    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/UK/GBP/en-US/{user_input[3]}/{user_input[2]}/{user_input[4]}"
    print (url)
    querystring = {"inboundpartialdate":user_input[5]}

    headers = {
        'x-rapidapi-key': "c5793d7cafmshf6f023ddc0f0f5ep11116cjsndb8f319ec001",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

readFile('flightData.txt')






