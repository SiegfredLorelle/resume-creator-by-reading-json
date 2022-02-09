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


# lagay ko lng references and guide ko para madali ko mabalikan: 
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html#line-breaks-and-colors
# https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f
# https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/


#1st try, d pa tapos, tinesting lng ung fpdf na module 
#2nd try, pinalitan ng mm ung in kase anlaki masyado ng spacing between txt, tinapos ung contacts, personal info, at ginawang two columns, dinagdagan at inayos ung nasa json, added auto open ng pdf
#3rd try, tinapos ung education at skills and interests, nilakihan ung fonts


import json
import os
from fpdf import FPDF 

# Opening JSON file
JSON_file = open('JSON3.json')
 
# returns JSON object as a dictionary
resume_details = json.load(JSON_file)
contacts = resume_details["contacts"]
personal_info = resume_details["personal info"]
educ_bg = resume_details["educational background"]
skills = resume_details["interests and skills"]

#Start to write in PDF
class PDF(FPDF):
    pass

#PDF formats    
pdf = PDF (orientation = "p",
          unit = "mm",
          format = "Letter")
pdf.set_margins(10,20,10)

pdf.add_page()


pdf.set_font("Arial", "B", size = 18)

#need para maging 2 columns
top = pdf.y
offset = pdf.x + 108

#Name
pdf.multi_cell (w=75, h=0, txt= contacts["Full Name"],   align = "C")

pdf.set_font("Arial", size = 15)
pdf.multi_cell (w=75, h=20, txt= contacts["Occupation"], align = "C")

# Contact details
pdf.set_font("Arial", "B", size = 15)
pdf.multi_cell (w=108, h=10, txt= "Contact Details", align = "L")

pdf.set_font("Arial", size = 13)
pdf.multi_cell (w=108, h=7, txt= "Address:  " + contacts["Address"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Email:  " + contacts["Email"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Facebook:  " + contacts["Facebook"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Number:  " + contacts["Number"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Github:  " + contacts["Github"], align = "L")

# No text, for extra space lang
pdf.multi_cell (w=108, h=7, txt= "  ", align = "L")

# Personal Information
pdf.set_font("Arial", "B", size = 15)
pdf.multi_cell (w=108, h=10, txt= "Personal Information", align = "L")

pdf.set_font("Arial", size = 13)
pdf.multi_cell (w=108, h=7, txt= "Age:  " + personal_info["Age"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Date of Birth:  " + personal_info["Date of Birth"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Sex:  " + personal_info["Sex"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Civil Status:  " + personal_info["Civil Status"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Nationality:  " + personal_info["Nationality"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Religion:  " + personal_info["Religion"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Mother's Name:  " + personal_info["Mother's Name"], align = "L")
pdf.multi_cell (w=108, h=7, txt= "Father's Name:  " + personal_info["Father's Name"], align = "L")

#need para maging 2 columns
#Start ng right column
#Lahat ng nasa right column need ng pdf.x = offset 
pdf.y = top
pdf.x = offset

# Educational Background
pdf.set_font("Arial", "B", size = 15)
pdf.multi_cell (w=108, h=10, txt= "Educational Background", align = "L")

pdf.x = offset
pdf.set_font("Arial", size = 13)
pdf.multi_cell (w=90, h=7, txt= "Tertiary School: " + educ_bg["Tertiary School"],    align = "L")
pdf.x = offset
pdf.multi_cell (w=90, h=7, txt= "- " + educ_bg["Tertiary School Currently"],    align = "R")

pdf.set_font("Arial", size = 13)
pdf.x = offset
# No text, for extra space lang
pdf.multi_cell (w=90, h=5, txt= "  ", align = "L")
pdf.x = offset
pdf.multi_cell (w=90, h=7, txt= "Secondary Senior High School: " + educ_bg["Secondary Senior High School"],    align = "L")
# No text, for extra space lang
pdf.multi_cell (w=90, h=5, txt= "  ", align = "L")
pdf.x = offset
pdf.multi_cell (w=90, h=7, txt= "Secondary Junior High School: " + educ_bg["Secondary Junior High School"],    align = "L")
# No text, for extra space lang
pdf.multi_cell (w=90, h=5, txt= "  ", align = "L")
pdf.x = offset
pdf.multi_cell (w=90, h=7, txt= "Primary Elementary School: " + educ_bg["Primary Elementary School"],    align = "L")


# No text, for extra space lang
pdf.multi_cell (w=108, h=7, txt= "  ", align = "L")



# interests and skills
pdf.set_font("Arial", "B", size = 15)
pdf.x = offset
pdf.multi_cell (w=108, h=10, txt= "Skills & Interests", align = "L")

pdf.set_font("Arial", size = 13)
pdf.x = offset
pdf.multi_cell (w=90, h=7, txt= "Hobbies: " + skills["hobbies"],    align = "L")
pdf.x = offset
# No text, for extra space lang
pdf.multi_cell (w=100, h=3, txt= "  ", align = "L")
pdf.x = offset
pdf.multi_cell (w=100, h=7, txt= "Skills: " + skills["skills"],    align = "L")








print ("working")

pdf.output('test3.pdf', "F")



# Closing file
JSON_file.close()

os.startfile('test3.pdf')

