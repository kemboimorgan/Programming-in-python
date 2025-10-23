class SimpleInterest:
    def __init__(self, principle, rate, time):
        self.principle = principle
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        self.simple_interest = (self.principle * self.rate * self.time) / 100
        return self.simple_interest

    def calculate_compound_interest(self):
        amount = self.principle * ((1 + self.rate / 100) ** self.time)
        self.compound_interest = amount - self.principle
        return self.compound_interest

my_interest = SimpleInterest(1000, 10, 5)

simple_result = my_interest.calculate_simple_interest()
compound_result = my_interest.calculate_compound_interest()

print("Simple interest:", simple_result)
print("Compound interest:", compound_result)