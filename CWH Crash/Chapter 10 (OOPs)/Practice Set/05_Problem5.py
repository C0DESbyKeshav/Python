# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of trains running under Indian Railways.
from random import randint


class Train:
    interests_cost = 0
    gst = 0
    food_cost = "Free"
        
    def __init__(self, name, age, gender, interests, address, destination):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests
        self.address = address
        self.destination = destination
        print(f"Train is booked in train number: {randint(2461, 5906)} from {address} to {destination}")
    
    @staticmethod
    def greet():
        print("Welcome to Keshav Railways!")
        print("Service like never before")
        print("Get your seats confirmed right beside the opposite gender person sharing the same interests as you :)")
        
    def status(self, no_of_seats):
        print(f"Current status:\n{no_of_seats} seats available")
        
    def get_fare(self, fare):
        print(f"Total Cost:\nTravel Fare: {fare}\nInterest Matching cost: {self.interests_cost}\nG.S.T: {self.gst}\nFood cost: {self.food_cost}\nAb toh aa jaao...")

        
customer1 = Train("Keshav", 18, "male", "cute", "Interests", "Love")
customer1.greet()
customer1.status(2)
customer1.get_fare(500)
