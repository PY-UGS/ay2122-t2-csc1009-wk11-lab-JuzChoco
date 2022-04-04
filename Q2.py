#Defines a class called clockTime
class clockTime:
    def __init__(self):
        hours = 0
        minutes = 0
        seconds = 0

    #Sets the hour
    def setHours(self, hour):
        self.hours = hour
    
    #Sets the minutes
    def setMinutes(self, minute):
        self.minutes = minute

    #Sets the seconds
    def setSeconds(self, second):
        self.seconds = second

    #Sets the time
    def setTime(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    #Returns the time
    def showTime(self):
        actual_time = str(self.hours + ":" + self.minutes + ":" + self.seconds)
        return actual_time

#Instantiate an instance of the class clockTime()
clock = clockTime()

#Obtaining the inputs from the user
hour = input("Please enter the hour value: ")
minute = input("Please enter the minutes value: ")
second = input("Please enter the seconds value: ")

print("\n")

#Sets the values based on the user's inputs accordingly
clock.setHours(hour)
clock.setMinutes(minute)
clock.setSeconds(second)

#Creates a variable to obtain the clock time
clock_time = clock.showTime()

#Prints the cucrent clock time
print("The current time is: " + clock_time)