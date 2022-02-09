"""Assignment 9

PDF Resume Creator
	- Create a python program that will create your personal resume in PDF format
	- All personal details are stored in a JSON file
	- Your program should read the JSON file and write the details in the PDF
	- The output file should be: LASTNAME_FIRSTNAME.pdf

Note:
	- Search for available PDF library that you can use
	- Search how data is structured using JSON format
	- Search how to read JSON file
	- You will create the JSON file manually
	- Your code should be in github before Feb12"""
 

#1st try, d pa tapos, tinesting lng ung fpdf na module 


import json
from fpdf import FPDF 

# Opening JSON file
JSON_file = open('JSON1.json')
 
# returns JSON object as a dictionary
resume_details = json.load(JSON_file)



 
class PDF(FPDF):
    pass

#PDF formats    
pdf = PDF (orientation = "p",
          unit="in",
          format= "Letter")

pdf.add_page()


pdf.set_font("Arial", "B", size = 15)
pdf.cell (w=3, h=1, txt= "FULL NAME:  " + resume_details["Full_Name"], ln = 1,  align = "C")


pdf.set_font("Arial", size = 15)
pdf.cell (w=3, h=1, txt= "FULL NAME:  " + resume_details["occupation"] , align = "C")


print (resume_details["Full_Name"])

pdf.output('test1.pdf',"F")



# Closing file
JSON_file.close()

