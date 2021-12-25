import requests
import  json
import smtplib, ssl
def readFile(fileName):
    
    with open(fileName) as f:
        d = json.load(f)
        print(d)
    
   
    trip =  d['trip']
    source = d['source']
    destination = d['destination']
    departureDate = d['departureDate']
    seatType = d['seatType']
    

    
    # fileObj = open(fileName, "r") #opens the file in read mode
    # user_input = fileObj.read().splitlines() #puts the file into an array
    # fileObj.close()

    url = f"https://api.flightapi.io/{trip}/61b49a3b13b15b74ee7b99e5/{source}/{destination}/{departureDate}/2/0/1/{seatType}/GBP"


    print(url)
    print('https://api.flightapi.io/onewaytrip/61b49a3b13b15b74ee7b99e5/LHR/LAX/2022-10-11/2/0/1/Economy/USD')
    response = requests.get(url)
    print(response)
    the_info = response.json()
    return response
    
    #print("the_info ********")
    #print(the_info)
    #print(the_info['legs'])
    #print(the_info['Quotes'][0]["MinPrice"])
    '''
    
    
    
    
    
    i=0
    #print(int(user_input[8]))
    for i in range(len(the_info['Quotes'])):
        if int(user_input[8]) >= int(the_info['Quotes'][i]["MinPrice"]):
            print(int(the_info['Quotes'][i]['MinPrice']))            
        i+=1
    '''    
# readFile('flightData.json')








