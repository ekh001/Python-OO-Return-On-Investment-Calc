# nums = [1, 3, 5, 7]
# x = [x*2 - 1 for x in nums[-2::]]
# print(x)

# def fib(n):
#     if n == 1:
#         return n
#     else: 
#         return fib(n-1) - fib(n-2)
# fib(3)

# class Toy():
#     kind = 'Car'

#     def __init__(self, rooftop, horn, wheels):
#         self.rooftop = rooftop
#         self.horn = horn
#         self.wheels = wheels

# hotwheels_car = Toy(1,1,3)
# print(hotwheels_car.rooftop)
# hotwheels_car.rooftop = 0
# print(hotwheels_car.rooftop)

class Parent(object):
    def __init__(self):
        self.value = 4
    def get_value(self):
        return self.value
class Child(Parent):
    def get_value(self):
        return self.value + 1
c = Child()
print(c.get_value())