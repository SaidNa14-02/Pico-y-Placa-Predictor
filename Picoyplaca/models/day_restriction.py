import calendar
from datetime import datetime
from models.schedule import Schedule
from models.vehicle import Vehicle

class DayRestriction:
    RESTRICTION_DAYS = {
        "Monday": [1, 2],
        "Tuesday": [3, 4],
        "Wednesday": [5, 6],
        "Thursday": [7, 8],
        "Friday": [9, 0]
    }

    def __init__(self):
        self.schedule = Schedule()

    def get_day_of_week(self, date: str):
        if not self.schedule.check_date(date):
            raise ValueError("Invalid date format")
        
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        weekday = date_obj.weekday()
        return calendar.day_name[weekday]

    def check_day_restriction(self, input_date: str, plate: str):
        if not self.schedule.check_date(input_date):
            raise ValueError("Invalid date format")

        temp_vehicle = Vehicle(plate)
        if not temp_vehicle.check_plate(plate):
            raise ValueError("Invalid plate format")

        day_name = self.get_day_of_week(input_date)
        last_digit = int(plate[-1])
        
        return last_digit in self.RESTRICTION_DAYS[day_name]