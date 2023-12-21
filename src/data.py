import math

help_msg = '>>> Available commands:\n\
          -> help: prints all available commands\n\
          -> unit <val1> <unit1> <unit2>: convert between units\n\
          -> const <arg>: retrieve constant value by name or symbol\n\
          -> sun: list of sun constants\n\
          -> sphere <R> <unit>: get sphere surface area and volume by radius\n\
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
    'power': ['erg/s', 'W'],
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

alt_units = {
        'C': '°C',
        'F': '°F'
}

# possible ways to refer to constants stored due to case sensitivity of symbols
c_names = ['c', 'light', 'speed of light', 'light speed', 'light velocity', 'speed light']
G_names = ['G', 'gravitational constant', 'gravitational', 'gravity constant']
h_names = ['h', 'Planck', "Planck's constant", "Planck's", 'planck']
k_names = ['k', 'Boltzmann', "Boltzmann's", "Boltzmann's constant", 'boltzmann']
sb_names = ['σ', 'sigma', 'Stefan Boltzmann', 'Stefan-Boltzmann', "Stefan-Boltzmann's", "Stefan Boltzmann's",\
            'stefan boltzmann', 'stefan-boltzmann', 's-b', 'sb', 'SB', 'S-B']
pm_names = ['proton mass', 'mass of proton']
nm_names = ['neutron mass', 'mass of neutron']
em_names = ['electron mass', 'mass of electron']
AU_names = ['AU', 'au', 'astronomical unit']

names = [c_names, G_names, h_names, k_names, sb_names, pm_names, nm_names, em_names, AU_names]
# cgs units followed by mostly si units
constants = {
    'c': '3e10 cm/s \t 3e8 m/s',
    'G': '6.67e-8 cm^3/(g*s^2) \t 6.67e-11 N*m^2/kg^2',
    'h': '6.63e-27 erg*s \t 6.63e-34 J/Hz',
    'k': '1.38e-16 erg/K \t 1.38e-23 J/K',
    'σ': '5.67e-5 erg/(cm^2*s*K^4) \t 5.67e-8 W/(m^2*K^4)',
    'proton mass': '1.6726e-24 g \t 1.6726e-27 kg',
    'neutron mass': '1.6749e-24 g \t 1.6749e-27 kg',
    'electron mass': '9.1096e-28 g \t 9.1096e-31 kg',
    'AU': '1.4959789e13 cm \t 1.4959789e8 km'
}