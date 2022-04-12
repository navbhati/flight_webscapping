class FlightFare:
    price_amount = None
    handoff_url = ""
    
    def __init__(self, price_amount, handoff_url):
        self.price_amount = price_amount
        self.handoff_url = handoff_url

    
    def get_flight_price(self):
        return str(self.price_amount) +  " " + self.handoff_url