class New_park():
    def __init__(self):
        self.area = 0;
        self.things  = []

    def adding(self,item):
        self.things.append(item)

    def deleting_named(self,item):
        if item in self.things:
            self.things.remove(item)

    def count_things(self):
        return len(self.things)

    def last_item(self):
        return self.things.pop()

    def deleting_last(self):
        if self.things != []:
            self.things.pop()

def count_sum_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        if digit % 3 == 0:
            sum += digit
        n //= 10
    return sum