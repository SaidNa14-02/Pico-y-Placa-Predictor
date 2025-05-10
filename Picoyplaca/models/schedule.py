from datetime import datetime

class Schedule:
    def __init__(self):
        self.__time = datetime.now().time()
        self.__date = datetime.now().date()
    
    def get_time(self):
        return self.__time
    
    def get_date(self):
        return self.__date

    def set_date(self, date):
        if self.check_date(date):
            self.__date = datetime.strptime(date, "%d/%m/%Y").date()
        else:
            raise ValueError("Invalid date format")

    def set_time(self, time):
        if self.check_time(time):
            self.__time = datetime.strptime(time, "%H:%M").time()
        else:
            raise ValueError("Invalid time format")
    
    def check_date(self, input_date):
        if not input_date or not isinstance(input_date, str):
            return False
        try:
            datetime.strptime(input_date, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def check_time(self, input_time):

        if not input_time or not isinstance(input_time, str):
            return False
        
        if len(input_time) != 5 or input_time[2] != ':':
            return False
        
        hours, minutes = input_time.split(':')
        if len(hours) != 2 or len(minutes) != 2:
            return False
            
        try:
            datetime.strptime(input_time, "%H:%M")
            return True
        except ValueError:
            return False

