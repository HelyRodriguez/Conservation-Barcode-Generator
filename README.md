# Conservation-Barcode-Generator
This repository houses a script for generating a 2D linear conservation map, or conservation barcode, using any Consurf PDB file generated from the Consurf web server as the input file. 

First Time Usage:
This script is written with Python 3.9 and relies on the pandas and matplotlib libraries. If you have just downloaded Python 3.9 and these libraries are not installed, or you are not sure if you have them installed, uncomment the following lines in the script by removing the two lines above and below them containing 3 single-quote characters. These lines will then be executed upon running the script and will install the pandas and matplotlib libraries if not already installed.

'''

os.system('python -m pip install pandas')

os.system('python -m pip install matplotlib')

'''

1. Place your consurf.pdb in the same working directory as Conservation_Barcoder.py
2. Run the script with Python 3.9
3. Upon being prompted, enter your consurf.pdb filename
4. After running, check your working directory for a new file called "colored_rectangles.py"
5. Run colored_rectangles.py to display your figure.
6. Save the figure in the desired file format (.svg best for later use in illustrator)
