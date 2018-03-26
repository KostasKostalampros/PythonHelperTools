"""
This python script converts xml file content into oneliner and stores the output
 in a txt file .

Args:
    inputFilepath: The filepath of the xml file to convert
	outputFilepath: the output filepath of the oneliner converted xml content. 

Returns:
    Text file including the converted oneliner xml content.
 
Example:
        $ python XMLstringToSingleLineConverter.py --inputFilepath inputFile.xml --outputFilepath outputFile.txt
"""


import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputFilepath', help='Type the filepath of the input file to convert to oneliner')
parser.add_argument('--outputFilepath', help='Type the filepath of the output file to be generated')
args = parser.parse_args()

with open(args.inputFilepath, 'r') as opened_file:
    lines = opened_file.readlines()
    oneliner = ''.join([line.strip() for line in lines])

with open(args.outputFilepath, 'w', newline="") as opened_file:
    opened_file.write(oneliner)

print("File succesfully converted into oneliner and saved in the specified output filepath!")


