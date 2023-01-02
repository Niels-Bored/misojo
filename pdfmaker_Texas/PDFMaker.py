import os
import random
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import white, black
from PyPDF2 import PdfFileMerger


def generatePDF(plate, year, make, issue_date, expiration_date, vin, major_color, minor_color, body, model, owner, address, city, state, zip_code):
	#plate = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + chr(random.randint(65, 90)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

	# File paths and fonts
	current_folder = os.path.dirname (__file__)
	parent_folder = os.path.dirname (current_folder)
	files_folder = os.path.join (parent_folder, "files")
	new_pdf_path = os.path.join (files_folder, f"{plate} newfile.pdf")
	new_pdf2_path = os.path.join (files_folder, f"{plate} newfile2.pdf")

	# Fonts with epeciufic path
	pdfmetrics.registerFont(TTFont('sawarabi', os.path.join (current_folder, 'SawarabiGothic-Regular.ttf')))
	pdfmetrics.registerFont(TTFont('oswald', os.path.join (current_folder, 'Oswald-Regular.ttf')))
	pdfmetrics.registerFont(TTFont('oswald-semibold', os.path.join (current_folder, 'Oswald-SemiBold.ttf')))
	pdfmetrics.registerFont(TTFont('oswald-bold', os.path.join (current_folder, 'Oswald-Bold.ttf')))
	pdfmetrics.registerFont(TTFont('orion', os.path.join (current_folder, 'ORIOND.ttf')))
	pdfmetrics.registerFont(TTFont('yantramanav', os.path.join (current_folder, 'Yantramanav-Regular.ttf')))
	pdfmetrics.registerFont(TTFont('yantramanav-medium', os.path.join (current_folder, 'Yantramanav-Medium.ttf')))
	pdfmetrics.registerFont(TTFont('yantramanav-bold', os.path.join (current_folder, 'Yantramanav-Bold.ttf')))
	pdfmetrics.registerFont(TTFont('yantramanav-black', os.path.join (current_folder, 'Yantramanav-Black.ttf')))
	pdfmetrics.registerFont(TTFont('clearsans-medium', os.path.join (current_folder, 'ClearSans-Medium.ttf')))
	pdfmetrics.registerFont(TTFont('clearsans-bold', os.path.join (current_folder, 'ClearSans-Bold.ttf')))
	pdfmetrics.registerFont(TTFont('texgy', os.path.join (current_folder, 'texgyreheros-bold.ttf')))
	pdfmetrics.registerFont(TTFont('texgycn', os.path.join (current_folder, 'texgyreheroscn-bold.ttf')))
	pdfmetrics.registerFont(TTFont('bierstadt', os.path.join (current_folder, 'Bierstadt.ttf')))
	pdfmetrics.registerFont(TTFont('MS', os.path.join (current_folder, 'ms-reference-sans-serif.ttf')))
	pdfmetrics.registerFont(TTFont('MSbd', os.path.join (current_folder, 'ms-reference-sans-serif-bold.ttf')))
	pdfmetrics.registerFont(TTFont('times', os.path.join (current_folder, 'times.ttf')))
	pdfmetrics.registerFont(TTFont('timesbd', os.path.join (current_folder, 'timesbd.ttf')))	
	
	c = canvas.Canvas(new_pdf_path, landscape(letter))
	c.drawImage(os.path.join (current_folder, 'fondo.png'), 0, 0, 792, 612)
	c.setFont('texgycn', 75)
	c.drawString(195, 370, expiration_date)

	tagtype = 'BUYERS TAG'
	status_code = '11A3'
	dba = 'ROYAL MOTORS'
	name_code = 'UDM COMPANY, LLC'
	gdn = 'P142054'

	data = f"https://plate-information.onrender.com/?tagno={plate}&tagtype={tagtype}&effective-timestamp={issue_date}&verification-code={status_code}&create-timestamp={issue_date}&end-timestamp={expiration_date}&status-code=ACTIVE8&vin={vin}&year={year}&make={make}&body={body}&color={major_color}&gdn={gdn}&name={name_code}&dba={dba}&address={address}"
	img = qrcode.make(data)
	img.save(os.path.join(current_folder, 'QRCode.png'))

	c.drawImage(os.path.join (current_folder, 'QRCode.png'), 605, 340, 110, 110)

	c.setFont('orion', 160)
	c.drawString(35, 225, plate)

	c.setFont('texgycn', 34)
	c.drawString(35, 192, year)
	c.drawString(35, 160, make)

	c.setFont('orion', 22)
	c.drawString(475, 188, vin)
	c.drawString(533, 168, dba)

	c.setFillColor(white)
	c.setFont('texgycn', 24)

	distance = 438
	for n in range(10):
		if(n !=8):
			c.drawString(753.5, distance, str(random.randint(0, 9)))
		else:
			c.drawString(753.5, distance, chr(random.randint(65, 90)))	
		distance -= 30

	c.setFillColor(black)
	
	c.showPage()
	c.save()

	c = canvas.Canvas(new_pdf2_path, letter)
	c.drawImage(os.path.join (current_folder, 'logo_Tx.png'), 60, 205, 485.25, 486.75)
	c.setFont('times', 16)
	c.drawString(154, 732, "BUYER'S TAG RECEIPT - BUYER'S COPY")
	c.setFont('times', 16)
	c.drawString(154, 732, "BUYER'S TAG RECEIPT - BUYER'S COPY")
	c.setFont('times', 12)
	x = 36
	y = 727
	c.line(x, y, x + 535, y)
	c.drawString(50, 708, "Tag Number: ")
	c.drawString(50, 670, "Issue Date:")
	c.drawString(50, 653, "VIN:")
	c.drawString(50, 637, "Year:")
	c.drawString(50, 621, "Make:")
	c.drawString(50, 606, "Major Color:")
	c.setFont('MS', 10)
	c.drawString(178, 708, plate)
	c.drawString(178, 670, issue_date)
	c.drawString(178, 653, vin)
	c.drawString(178, 637, year)
	c.drawString(178, 621, make)
	c.drawString(178, 606, major_color)
	c.setFont('times', 12)
	c.drawString(308, 708, "Date of Sale: ")
	c.drawString(308, 692, "Expiration Date:")
	c.drawString(308, 637, "Body Style:")
	c.drawString(308, 621, "Model:")
	c.drawString(308, 606, "Minor Color:")
	c.setFont('MS', 10)
	c.drawString(438, 708, issue_date)
	c.drawString(438, 692, expiration_date)
	c.drawString(438, 637, body)
	c.drawString(438, 621, model)
	c.drawString(438, 606, minor_color)
	c.setFont('times', 12)
	c.drawString(92, 569, "Remarks:")
	c.setFont('MS', 10)
	c.drawString(92, 555, "ACTUAL MILEAGE")
	c.drawString(92, 542, "CCO ISSUED:  [04/22/2019]")
	c.drawString(92, 527, "PAPER TITLE")
	c.drawString(92, 512, "E-REMINDER & PAPER RENEWAL NOTICE")
	c.setFont('times', 12)
	c.drawString(92, 482, "Issuing Dealer:")
	c.drawString(92, 465, "Dealer Number:")
	c.drawString(92, 434, "Purchaser")
	c.drawString(92, 418, "Name 1:")
	c.drawString(92, 403, "Address:")
	c.drawString(127, 312, "BUYER is required to keep this receipt in the vehicle until vehicle is")
	c.drawString(127, 294, "registered and metal plates are placed on the vehicle.")
	c.setFont('MS', 10)
	c.drawString(308, 482, "FIESTA MOTORS INC")
	c.drawString(308, 465, "594870R")
	c.drawString(308, 418, owner)
	c.drawString(308, 403, address)
	c.drawString(308, 388, city+", "+state)
	c.drawString(308, 373, zip_code)
	c.setFont('times', 16)
	c.drawString(249, 258, "BUYER'S COPY")
	c.save()
	
	pdfs = [new_pdf_path, new_pdf2_path]

	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(pdf)

	plate_path = os.path.join (files_folder, plate+".pdf")
	merger.write(plate_path)
	merger.close()

	os.remove (new_pdf_path)
	os.remove (new_pdf2_path)

if __name__=='__main__':
	generatePDF("2179W46", "2019", "CHEVROLET", "DEC 02, 2020", "FEB 20, 2023", "1GCUYDED8KZ135075", "RED", "GREEN", "TRUCK", "FORD", "Someone", "Someplace", "City", "State", "20000")