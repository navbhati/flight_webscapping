import requests
import  json
import smtplib, ssl
def getFlightData(inputData):
    
   
    trip =  inputData['ticketType']
    source = inputData['origin']
    destination = inputData['destination']
    departureDate = inputData['departureDate']
    seatType = inputData['class']
    budget = inputData['budget']
    

    
    # fileObj = open(fileName, "r") #opens the file in read mode
    # user_input = fileObj.read().splitlines() #puts the file into an array
    # fileObj.close()

    url = f"https://api.flightapi.io/{trip}/61b49a3b13b15b74ee7b99e5/{source}/{destination}/{departureDate}/2/0/1/{seatType}/GBP"


   

    response = requests.get(url)
  
    the_info = response.json()
    
    options = the_info['fares']
    
    
    results = ""
    for option in options:
        
        if int(budget) >= option['price']['amount']:
            results += option['providerCode'] + " " + str(option['price']['amount']) + " "
            return results

    return "Prices not found"

    '''
    
    
    
    
    
    i=0
    #print(int(user_input[8]))
    for i in range(len(the_info['Quotes'])):
        if int(user_input[8]) >= int(the_info['Quotes'][i]["MinPrice"]):
            print(int(the_info['Quotes'][i]['MinPrice']))            
        i+=1
    '''    
# readFile('flightData.json')








