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

# picture
# https://www.reddit.com/r/VinlandSaga/comments/kutmsi/manga_which_chapter_thorfinn_first_appear_as_a/


#1st try, d pa tapos, tinesting lng ung fpdf na module 
#2nd try, pinalitan ng mm ung in kase anlaki masyado ng spacing between txt, tinapos ung contacts, personal info, at ginawang two columns, dinagdagan at inayos ung nasa json, added auto open ng pdf
#3rd try, tinapos ung education at skills and interests, nilakihan ung fonts
#4th try, added underline to titles, capitalize and uderline words na need ng emphasis, added pic, nagdagdag ng details sa json, added comments, nilagay sa def func

#aayusin file names

import json
from fpdf import FPDF 
import os

def main():
	# Opening JSON file
	JSON_file = open('JSON4.json')
	
	# save objects from json file to a variable
	resume_details = json.load(JSON_file)

	# save details to variables para mas madali maaccess kapag ginagawa na ung pdf
	resume_details = resume_details["resume details"]
	contacts = resume_details["contacts"]
	personal_info = resume_details["personal info"]
	profile = resume_details ["profile"]
	educ_bg = resume_details["educational background"]
	tertiary = educ_bg ["Tertiary"]
	secondary = educ_bg ["Secondary"]
	primary = educ_bg ["Primary"]
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

	#need para maging 2 columns
	top = pdf.y
	offset = pdf.x + 108

	#Pic
	pdf.set_font("Arial")						
	pdf.cell(40)
	pdf.image("Thorfinn Pic.jpg", 35, 20, 40, type = "JPG")

	#Name
	pdf.set_font("Arial", "B", size = 18)
	pdf.multi_cell (w=108, h=50, txt= "  ", align = "L")
	pdf.multi_cell (w=100, h=0, txt= contacts["Full Name"].upper(),   align = "L")

	#Occupation
	pdf.set_font("Arial", size = 15)
	pdf.multi_cell (w=90, h=20, txt= contacts["Occupation"].upper(), align = "C")

	# Contacts Title
	pdf.set_font("Arial", "B", size = 18)
	pdf.multi_cell (w=108, h=10, txt= "Contact Details".upper(), align = "L")
	# Line under it
	pdf.line(10, 98, 73, 98)

	# Contacts Details 
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=108, h=7, txt= "Address:  " + contacts["Address"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Email:  " + contacts["Email"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Facebook:  " + contacts["Facebook"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Number:  " + contacts["Number"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Github:  " + contacts["Github"], align = "L")

	# No text, for extra space lang
	pdf.multi_cell (w=108, h=7, txt= "  ")

	# Personal Information Title
	pdf.set_font("Arial", "B", size = 18)
	pdf.multi_cell (w=108, h=10, txt= "Personal Information".upper(), align = "L")
	# Line under it
	pdf.line(10, 150, 94, 150)

	# Personal Information Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=108, h=7, txt= "Age:  " + personal_info["Age"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Date of Birth:  " + personal_info["Date of Birth"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Sex:  " + personal_info["Sex"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Civil Status:  " + personal_info["Civil Status"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Nationality:  " + personal_info["Nationality"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Religion:  " + personal_info["Religion"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Mother's Name:  " + personal_info["Mother's Name"], align = "L")
	pdf.multi_cell (w=108, h=7, txt= "Father's Name:  " + personal_info["Father's Name"], align = "L")

	# No text, for extra space lang
	pdf.multi_cell (w=108, h=7, txt= "  ")

	# Profile Title 
	pdf.set_font("Arial", "B", size = 18)
	pdf.multi_cell (w=108, h=10, txt= "Profile".upper(), align = "L")
	# Line under it
	pdf.line(10, 223, 40, 223)

	# Profile Details 
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=108, h=7, txt= profile["Profile"], align = "L")


	#Start ng right column
	#Every line na nasa right column need ng pdf.x = offset 
	pdf.y = top
	pdf.x = offset

	# Educational Background Title
	pdf.set_font("Arial", "B", size = 17)
	pdf.multi_cell (w=108, h=0, txt= "Educational Background".upper(), align = "L")
	pdf.x = offset
	# Line under it
	pdf.line(118, 23, 209, 23)

	#space
	pdf.multi_cell (w=90, h=5, txt= "  ")
	pdf.x = offset

	#Tertiary Title
	pdf.set_font("Arial", "B", size = 17)
	pdf.multi_cell (w=90, h=7, txt= "Tertiary School",    align = "L")
	pdf.x = offset
	#Tertiary School
	pdf.set_font("Arial", "U", size = 13)
	pdf.multi_cell (w=90, h=7, txt= tertiary["School"],    align = "L")
	pdf.x = offset
	#Tertiary Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=90, h=7, txt= tertiary["Year"],    align = "R")
	pdf.x = offset
	pdf.multi_cell (w=90, h=7, txt= "- " + tertiary["Currently"],    align = "R")
	pdf.x = offset

	#space 
	pdf.multi_cell (w=90, h=5, txt= "  ")
	pdf.x = offset

	#Secondary Senior Title
	pdf.set_font("Arial", "B", size = 17)
	pdf.multi_cell (w=90, h=7, txt= "Secondary Senior High School:  ",    align = "L")
	pdf.x = offset
	#Secondary Senior School
	pdf.set_font("Arial", "U", size = 13)
	pdf.multi_cell (w=90, h=7, txt= secondary ["Senior"] ["School"],    align = "L")
	pdf.x = offset
	#Secondary Senior Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=90, h=7, txt= secondary["Senior"] ["Year"],    align = "R")
	pdf.x = offset
	pdf.multi_cell (w=90, h=7, txt= "- Strand:  " + secondary ["Senior"] ["Strand"],    align = "R")
	pdf.x = offset
	pdf.multi_cell (w=90, h=7, txt= "- " + secondary ["Senior"] ["Awards"],    align = "R")
	pdf.x = offset

	#space
	pdf.multi_cell (w=90, h=5, txt= "  ")
	pdf.x = offset

	#Secondary Junior Title
	pdf.set_font("Arial", "B", size = 17)
	pdf.multi_cell (w=90, h=7, txt= "Secondary Junior High School:  ",    align = "L")
	pdf.x = offset
	#Secondary Junior School
	pdf.set_font("Arial", "U", size = 13)
	pdf.multi_cell (w=90, h=7, txt= secondary ["Junior"] ["School"],    align = "L")
	pdf.x = offset
	#Secondary Junior Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=90, h=7, txt= secondary["Junior"] ["Year"],    align = "R")
	pdf.x = offset
	pdf.multi_cell (w=90, h=7, txt= "- " + secondary ["Junior"] ["Awards"],    align = "R")
	pdf.x = offset

	#space
	pdf.multi_cell (w=90, h=5, txt= "  ")
	pdf.x = offset

	#Primary Title
	pdf.set_font("Arial", "B", size = 17)
	pdf.multi_cell (w=90, h=7, txt= "Primary Elementary School:  ",    align = "L")
	pdf.x = offset
	#Primary School
	pdf.set_font("Arial", "U", size = 13)
	pdf.multi_cell (w=90, h=7, txt= primary ["School"],    align = "L")
	pdf.x = offset
	#Primary Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=90, h=7, txt= primary ["Year"],    align = "R")
	pdf.x = offset
	pdf.multi_cell (w=90, h=7, txt= "- " + primary["Awards"],    align = "R")
	pdf.x = offset

	pdf.multi_cell (w=108, h=7, txt= "  ", align = "L")
	pdf.x = offset


	# Interests & Skills Title
	pdf.set_font("Arial", "B", size = 18)
	pdf.x = offset
	pdf.multi_cell (w=108, h=10, txt= "Skills & Interests".upper(), align = "L")
	pdf.x = offset
	# Line under it
	pdf.line(118, 209, 186, 209)

	# Hobbies Title
	pdf.set_font("Arial", "B",size = 13)
	pdf.multi_cell (w=90, h=7, txt= "Hobbies:  \n",    align = "L")
	pdf.x = offset
	# Hobbies Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=90, h=7, txt= skills["hobbies"],    align = "L")
	pdf.x = offset

	# No text, for extra space lang
	pdf.multi_cell (w=100, h=3, txt= "  ", align = "L")
	pdf.x = offset

	# Skills Title
	pdf.set_font("Arial", "B",size = 13)
	pdf.multi_cell (w=100, h=7, txt= "Skills:  \n" ,    align = "L")
	pdf.x = offset
	# Skills Details
	pdf.set_font("Arial", size = 13)
	pdf.multi_cell (w=100, h=7, txt=  skills["skills"],    align = "L")


	# Msg to users
	print ("\nWORKING...")
	print("In cases where the file did not open automatically, try to open it manually, \nit should be saved in the same directory as this and the json file with the file name 'test4.pdf'.\n")

	pdf.output('test4.pdf',"F")

	# Close file para maiwasan errors
	JSON_file.close()

	# automatic open ng pdf
	os.startfile('test4.pdf')


if __name__ == "__main__":
	main()