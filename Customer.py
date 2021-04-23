# Python Class

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer created")

    def update_memmbership(self, new_membership):
        self.membership_type = new_membership
           


C = Customer('William', "Gold")

print(C.name, C.membership_type)
