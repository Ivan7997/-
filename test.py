class Car():
    def __init__(self,speed, weight, color):
        self.speed = speed
        self.weight = weight
        self.color = color
        
    def ride(self):
        print("Я еду")
    def stop(self):
        print("Я остановился")


largus = Car(250, 1500, "silver")

print(largus.speed)
largus.ride()

corvette = Car(310, 1300, "red")

print(corvette.speed)
corvette.ride()
corvette.stop()