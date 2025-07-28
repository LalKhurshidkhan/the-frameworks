# class circle:
#     def __inint__(self,radius,color):
#         self.radius = radius
#         self.coloe = color

# red_circle = circle(5,'red')    
# print("Radius:", red_circle.radius)
# print("Color:", red_circle.color)


class Circle:
    def __init__(self, radius, color):  # Correct constructor
        self.radius = radius
        self.color = color

# Now creating an instance of Circle
# red_circle = Circle(5, 'red')
red_circle = Circle(5, 'red')

# Print the values to confirm it worked
print("Radius:", red_circle.radius)
print("Color:", red_circle.color)
