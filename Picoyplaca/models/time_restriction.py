from datetime import datetime
from models.schedule import Schedule

class TimeRestriction:
    RESTRICTION_HOURS = {
        "Morning": (datetime.strptime("07:00", "%H:%M").time(), datetime.strptime("09:00", "%H:%M").time()),
        "Afternoon": (datetime.strptime("16:00", "%H:%M").time(), datetime.strptime("19:30", "%H:%M").time()),
    }
    def __init__(self):
        self.schedule = Schedule()

    #This method verifies if the input time is or is not in the restriction hours
    def check_time_restriction(self, input_time): 
        if not self.schedule.check_time(input_time):
            raise ValueError("Invalid time format")
        
        input_time = datetime.strptime(input_time, "%H:%M").time()

        for value in self.RESTRICTION_HOURS.values():
            if value[0] <= input_time <= value[1]:
                return True
        return False



