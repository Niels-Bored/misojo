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

def convert_book(name):
    file = open(name, 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages

    for i in range (2101, totalpages, 50):
        if i+49<totalpages:
            readPages(name, i, i+49)
        else: 
            readPages(name, i, totalpages)

#convert_book("EYM 4001-5000.pdf")
