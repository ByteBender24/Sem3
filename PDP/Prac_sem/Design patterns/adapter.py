'''
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.'''

# Target


class Local_socket:

    def local_voltage(self):
        print("Voltage is 220v")

    def local_power(self):
        print("power consumed is 5 units")

    def local_energy(self):
        print("Low energy consumption")

# Adaptee


class Foreign_socket:

    def foreign_voltage(self):
        print("Voltage is 110v")

    def foreign_energy(self):
        print("High energy consumption")

    def foreign_power(self):
        print("power consumed is 10 units")

# Adapter


class ForeignSocket_adapter(Local_socket):

    def __init__(self, foreign_adapter):
        self.foreign_adapter = foreign_adapter

    def local_voltage(self):
        self.foreign_adapter.foreign_voltage()

    def local_energy(self):
        self.foreign_adapter.foreign_energy()


ls = Local_socket()
fs = Foreign_socket()
fsa = ForeignSocket_adapter(fs)

ls.local_voltage()
ls.local_energy()

fsa.local_voltage()
fsa.local_energy()

# -------------------------------------------------------------------------------------------------
print("\n\n")


# Target interface
class CelsiusTemperature:
    def get_temperature(self):
        pass

# Adaptee (the class with the incompatible interface)


class FahrenheitTemperature:
    def get_temperature_in_fahrenheit(self):
        return 100.0

# Adapter


class FahrenheitToCelsiusAdapter(CelsiusTemperature):
    def __init__(self, fahrenheit_temperature):
        self.fahrenheit_temperature = fahrenheit_temperature

    def get_temperature(self):
        # Convert Fahrenheit to Celsius
        return (self.fahrenheit_temperature.get_temperature_in_fahrenheit() - 32) * 5.0/9.0

# Client code


def print_temperature(temperature_object):
    print(f'Temperature: {temperature_object.get_temperature()}°C')


# Using the Adapter pattern
fahrenheit_temperature = FahrenheitTemperature()
adapter = FahrenheitToCelsiusAdapter(fahrenheit_temperature)
print_temperature(adapter)
