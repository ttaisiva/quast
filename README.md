# Quast

quast.py is a command line-based program that makes it easier and faster to do quick calculations related to astronomy.

Capabilities include:
- intuitive user experience (easy to comprehend commands, in-depth help message and clear start and end to the app)
- unit conversion including common units* as well as additional advanced units used in astronomy
- quick access to constants, including solar constants and others used in astronomy and physics
    - sun constants listed all at once
    - others can be looked up by symbol or name with various spellings
- instant sphere properties calculation (surface area and volume)

How to run:
Both files, quast.py and data.py, are necessary in the execution directory.
Run "py quast.py" to begin executing Quast.
Type "quit" into the Quast interface to quit the program.

Unit conversion notes:
Common unit conversion (time in s/min/h, distance in m/km/etc, and others) provided with an imported library found here:
https://pypi.org/project/unit-converter/
Additional units common in astronomy (erg, pc, and others) implemented separately.

Other sources:
Astronomy: A Physical Perspective by Marc L. Kutner
AST 203 slides: radiation