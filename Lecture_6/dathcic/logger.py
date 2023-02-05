from datetime import datetime as dt

def temperature_login(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; temperature;{}\n'
                   .format(time,data))

def pressure_login(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; pressure;{}\n'
                   .format(time,data))
        
def wind_speed(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; wind_speed;{}\n'
                   .format(time,data))