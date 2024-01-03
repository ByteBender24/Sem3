'''
The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. 
The pattern encapsulates state-specific behaviors into separate classes and delegates the responsibility of managing state 
transitions to a context class. 
This promotes cleaner code, reduces conditional statements, and improves maintainability.
'''

from abc import ABC, abstractmethod

# State Interface


class State(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete States


class OnState(State):
    def turn_on(self):
        print("Light is already ON.")

    def turn_off(self):
        print("Turning OFF the light.")
        return OffState()


class OffState(State):
    def turn_on(self):
        print("Turning ON the light.")
        return OnState()

    def turn_off(self):
        print("Light is already OFF.")

# Context


class LightSwitch:
    def __init__(self):
        self._state = OffState()

    def turn_on(self):
        self._state = self._state.turn_on()

    def turn_off(self):
        self._state = self._state.turn_off()


# Client Code
light_switch = LightSwitch()

light_switch.turn_on()  # Turning ON the light.
light_switch.turn_off()  # Turning OFF the light.
light_switch.turn_off()  # Light is already OFF.
light_switch.turn_on()  # Turning ON the light.
light_switch.turn_on()  # Light is already ON.
