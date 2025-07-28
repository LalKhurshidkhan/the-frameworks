class rectangle:
    def __init__(self, color , height , weight):
        self.color = color
        self.height = height
        self.weight = weight

red_rectangle = rectangle("red", 10, 20)
print("color:",red_rectangle.color)
print("height:",red_rectangle.height)
print("weight:",red_rectangle.weight)