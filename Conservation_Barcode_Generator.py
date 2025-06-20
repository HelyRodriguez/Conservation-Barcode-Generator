import os

os.system('python -m pip install pandas')
os.system('python -m pip install matplotlib')


import pandas as pd
import csv
import matplotlib
import matplotlib.pyplot as plt

from tkinter.filedialog import askopenfilename
my_consurf_file = askopenfilename()
my_consurf_pdb = ''

def get_text_after_last_slash(text):
    # Split the text by the forward slash and return the last part
    global my_consurf_pdb
    my_consurf_pdb = text.split('/')[-1]

get_text_after_last_slash(my_consurf_file)

my_consurf_csv = my_consurf_pdb[:-3] + "csv"
conservation_scores = []

with open(my_consurf_file) as fin, open(my_consurf_csv, 'w') as fout:
    o=csv.writer(fout)
    lines = fin.readlines()
    #count for index distance of current line from line with "MODEL        1" in it
    x = 1
    o.writerow('abcdefxyzjk\n')
    for i in range(len(lines)):
        if "MODEL        1"  in lines[i-x]:
            for j in range(len(lines[i])):
                if "O1-" in lines[i]:
                    lines[i] = lines[i].replace("O1-", "O1n")
                if lines[i][j] == "-" and lines[i][j-1] != " ":
                    lines[i] = lines[i].replace(lines[i][j], " -")
                    #print(lines[i])

            if "A1" in lines[i]:
                lines[i] = lines[i].replace("A1", "A 1")
            if "A2" in lines[i]:
                lines[i] = lines[i].replace("A2", "A 2")
            if "A3" in lines[i]:
                lines[i] = lines[i].replace("A3", "A 3")
            if "A4" in lines[i]:
                lines[i] = lines[i].replace("A4", "A 4")
            if "A5" in lines[i]:
                lines[i] = lines[i].replace("A5", "A 5")
            if "A6" in lines[i]:
                lines[i] = lines[i].replace("A6", "A 6")
            if "A7" in lines[i]:
                lines[i] = lines[i].replace("A7", "A 7")
            if "A8" in lines[i]:
                lines[i] = lines[i].replace("A8", "A 8")
            if "A9" in lines[i]:
                lines[i] = lines[i].replace("A9", "A 9")

            o.writerow(lines[i].split())
            x+=1

fin.close()
fout.close()

def remove_blank_and_dup_rows(input_filepath, output_filepath):
    """
    Removes blank and duplicate rows from the consurf CSV file.

    Args:
        input_filepath (str): Path to the input CSV file.
        output_filepath (str): Path to the output CSV file (cleaned).
    """
    with open(input_filepath, 'r', newline='') as infile, \
            open(output_filepath, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        coordinates = ['0', '0', '0']
        for row in reader:
            if row[6:9] != coordinates and any(field.strip() for field in row):
                writer.writerow(row)
                coordinates = row[6:9]

# Example usage of remove_blank_rows(input_filepath, output_filepath)
input_csv_path = my_consurf_csv
output_csv_path = 'INPUT_' + my_consurf_csv
remove_blank_and_dup_rows(input_csv_path, output_csv_path)
os.remove(my_consurf_csv)


float_string_conservation_scores = []
#parse through .csv above and extract conservation scores into a list
df = pd.read_csv(output_csv_path)
for index, row in df.iterrows():
    if row["c"] == "CA":
        float_string_conservation_scores.append(row["k"])
#clean up conservation score list
for i in range(len(float_string_conservation_scores)):
    #print(i)
    float_string_conservation_scores[i] = str(float_string_conservation_scores[i])
    if '*' in float_string_conservation_scores[i]:
        float_string_conservation_scores[i] = float_string_conservation_scores[i].replace('*', '')
        
print(float_string_conservation_scores)
print(len(float_string_conservation_scores))
conservation_scores = [str(int(float(num))) for num in float_string_conservation_scores]
print(conservation_scores)
print(len(conservation_scores))

x = 0
y = 50

#create a new python script to execute plotting of colored rectangles/conservation "barcode"
#a new script called colored_rectangles.py will appear in your directory after executing this script
#run that script and adjust the y and x axes to find your plotted conservation barcode
#save as an .svg file to edit in Illustrator
with open("colored_rectangles.py", "w") as file:
    file.write("import matplotlib\n")
    file.write("import matplotlib.pyplot as plt\n")
    file.write("fig = plt.figure()\n")
    file.write("ax = fig.add_subplot(111)\n")
    file.write("ax.set_xlim([-100, " + str(len(conservation_scores)+100) + "])\n")
    file.write("ax.set_ylim([0, 200])\n")
    
    for i in range(len(conservation_scores)):
        if conservation_scores[i] == '1':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.039215686, 0.490196078, 0.509803922))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '2':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.294117647, 0.68627451, 0.745098039))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '3':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.647058824, 0.862745098, 0.901960784))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '4':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.843137255, 0.941176471, 0.941176471))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '5':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(1, 1, 1))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '6':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.980392157, 0.921568627, 0.960784314))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '7':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.980392157, 0.784313725, 0.862745098))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '8':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.941176471, 0.490196078, 0.666666667))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        if conservation_scores[i] == '9':
            file.write("rect" + str(i+1) + " = matplotlib.patches.Rectangle((" + str(x) + "," + str(y) + "), 1, 100, color=(0.62745098, 0.156862745, 0.37254902))\n")
            file.write("ax.add_patch(rect" + str(i+1) + ")\n")
        x+=1
    file.write("plt.show()")

print("A new file called colored_rectangles.py was created in this working directory.")
print("Run colored_rectangles.py to view your 2D consurf map. Save as an .svg file for use in illustrator.")
