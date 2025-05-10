class Vehicle:
    def __init__(self, plate):
        self.set_plate(plate)
    
    def get_plate(self):
        return self.__plate
    
    def set_plate(self, plate):
        if self.check_plate(plate):
            self.__plate = plate.upper()
        else:
            raise ValueError("Invalid plate format")
    
    def check_plate(self, plate):
        if not plate or not isinstance(plate, str):
            return False
        
        plate = plate.strip().upper()
        
        if len(plate) not in [7, 8]:
            return False
            
        if plate[3] != '-':
            return False
        
        if not plate[0:3].isalpha():
            return False
            
        if not plate[4:].isdigit():
            return False
            
        return True
    
    def get_last_digit(self):
        return self.__plate.split('-')[1][-1]

