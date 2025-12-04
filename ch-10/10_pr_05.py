'''write a class train which has method to book a ticket,get status[no.of seats]
and get fair information of trains running under indian railways'''

class Train:
    def __init__(self,name,fare,seats) :
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("********")
        print(f"the name of the train is:{self.name}")
        print(f"the number of seats availabke in the train is: {self.seats}")
        print("**********")
    
    def fareinfo(self):
        print(f"the price of the ticket is :Rs.{self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! and your seat number is{self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry!the train is already full")
    def cancelTickets(self,seatNo):
      pass

intercity=Train("intercity express:14561",70,100)
intercity.getStatus()
intercity.bookTicket()#book the ticket first time:make available seats(total seats-1)
intercity.bookTicket()#book the ticket second time then make no of seat availabel (total seats(i.e.100)-2)
intercity.getStatus()