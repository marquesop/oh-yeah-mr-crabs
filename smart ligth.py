class SmartLight:
    def __init__(self,room):
        self.room = room
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"The smart light in {self.room} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"The smart light in {self.room} is now OFF.")

    def status(self):
        print(f'{self.room}: {self.is_on}')