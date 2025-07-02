class Ride:
    def __init__(self, pickup_location, drop_location, distance):
        self.pickup = pickup_location
        self.drop = drop_location
        self.distance = distance

    def calculate_fare(self):
        fare = self.distance * 10
        print("Pickup:", self.pickup)
        print("Drop:", self.drop)
        print("Distance:", self.distance, "km")
        print("Fare: ₹", fare)

# Object banaya
ride1 = Ride("Andheri", "Bandra", 12)

# Method call kiya
ride1.calculate_fare()
