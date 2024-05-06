class cars:
    def __init__(self,year,speed) -> None:
        self.year=year
        self.speed=speed
    def getSpeed(self):
        print("maximum speed is",self.speed)
    def getInvent(self):
        print("this car was invented in",self.year)        
BMW=cars(2017,155)
TATA=cars(2014,120)
cars.getInvent(BMW)
cars.getSpeed(BMW)
TATA.getSpeed()
TATA.getInvent()        