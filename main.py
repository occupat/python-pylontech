import pylontech

p = pylontech.Pylontech(serial_port='COM3', baudrate=9600)
print(p.get_values())