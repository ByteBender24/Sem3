from abc import ABC, abstractmethod

class Lightstate(ABC):
    def switch(self, bulb):
        pass
        
class Onstate(Lightstate):
    def switch(self, bulb):
        bulb.state = OffState()
        print("Light is off")
        
class OffState(Lightstate):
    def switch(self, bulb):
        bulb.state = Onstate()
        print("Light is On")
       
class Bulb:
    def __init__(self):
        self.state = OffState()
       
    def switch_state(self):
        self.state.switch(self)
        
if __name__ == "__main__":
    bulb = Bulb()
    bulb.switch_state()
    bulb.switch_state()
    bulb.switch_state()
    bulb.switch_state()


