import pyttsx3
import pdfplumber
import PyPDF2

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def readPages(title, initial_page, final_page):
    # Read the file
    content = ""
    for i in range(initial_page, final_page):
        with pdfplumber.open(title) as temp:
            text = temp.pages[i]
            content = content + text.extract_text()
        # Control the rate. Higher rate = more speed
    title = title.replace(".pdf", "")    
    output_file = f"{title} {initial_page}-{final_page}.mp3"
    audio = content.replace ("\n", "")
    print(audio)
    engine.save_to_file(audio, output_file)
    engine.runAndWait()

file = open('1001-2000.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(file)
totalpages = readpdf.numPages

for i in range (1, totalpages, 50):
    if i+49<totalpages:
        #print(str(i) + ' ' +str(i+49))
        readPages('1001-2000.pdf', i, i+49)
    else: 
        #print(str(i) + ' ' +str(totalpages))
        readPages('1001-2000.pdf', i, totalpages)