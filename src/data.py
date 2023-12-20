valid_commands = ['help', 'unit', 'const', 'sun', 'sphere', 'mainseq', 'quit']

help_msg = '>>> Available commands:\n\
          -> help: prints all available commands\n\
          -> unit <unit1> <val1> <unit2>: convert between units\n\
          -> const <arg>: retrieve constant value by name or symbol\n\
          -> sun: list of sun constants\n\
          -> sphere <R> <unit>: get sphere surface area and volume by radius\n\
          -> mainseq <L/T/M> <val>: predict main sequence star attributes based on \
luminosity (W), temperature (K), or mass (kg)\n\
          -> quit: quit Quast'

sun_info = '>>> Solar constants:\n\
    Mass: 1.9891e33 g \t 1.9891e30 kg\n\
    Luminosity: 3.83e33 erg/s \t 3.846e26 W\n\
    Radius: 6.9598e10 cm \t 6.9598e8 m \t 6.9598e5 km\n\
    Distance from galactic center: 8.5 kpc'