# Conservation-Barcode-Generator
This repository houses a script for generating a 2D linear conservation map, or conservation barcode, using any Consurf PDB file generated from the Consurf web server as the input file. 

Usage:
This script is written with Python 3.9 and relies on the pandas and matplotlib libraries. If they are not installed, this script will automatically install them for you.

1. Run Conservation_Barcode_Generator.py with Python 3.9
2. Upon being prompted, select your consurf.pdb
3. After running, check your working directory for a new file called "colored_rectangles.py"
4. Run colored_rectangles.py to display your figure.
5. Save the figure in the desired file format (.svg best for figure preparation)

Please use the following DOI to cite this repository: https://doi.org/10.5281/zenodo.15652924
