import math

help_msg = '>>> Available commands:\n\
          -> help: prints all available commands\n\
          -> unit <val1> <unit1> <unit2>: convert between units\n\
          -> const <arg>: retrieve constant value by name or symbol\n\
          -> sun: list of sun constants\n\
          -> sphere <R> <unit>: get sphere surface area and volume by radius\n\
          -> prefix: list of unit prefixes and corresponding orders of 10 for quick conversion\n\
          -> quit: quit Quast'

# sun constants to be printed
sun_info = '>>> Solar constants:\n\
    Mass: 1.9891e33 g \t 1.9891e30 kg\n\
    Luminosity: 3.83e33 erg/s \t 3.846e26 W\n\
    Radius: 6.9598e10 cm \t 6.9598e8 m \t 6.9598e5 km\n\
    Distance from galactic center: 8.5 kpc'

# currently acceptable units for conversion
units = {
    'force': ['dyn', 'N'],
    'energy': ['erg', 'J'],
    'power': ['erg*s^-1', 'W'],
    'angle': ['rad', 'deg'],
    'distance': ['km', 'pc']
}

def list_to_str(list):
    str = ''
    for e in list:
        str += e
    return str

# corresponds to units above; smaller units come first in array
conversion_factors = {
    list_to_str(units['force']): 1e5,
    list_to_str(units['energy']): 1e7,
    list_to_str(units['power']): 1e7,
    list_to_str(units['angle']): math.pi/180,
    list_to_str(units['distance']): 3.086e13
}