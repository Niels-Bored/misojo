import pyttsx3
import pdfplumber
import PyPDF2
import os

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def readPages(pdf_path, title, initial_page, final_page):
    # Read the file
    content = ""
    for i in range(initial_page, final_page):
        with pdfplumber.open(pdf_path) as temp:
            text = temp.pages[i]
            content = content + text.extract_text()
        # Control the rate. Higher rate = more speed
    title = title.replace(".pdf", "")    
    output_file = f"{title} {initial_page}-{final_page}.mp3"
    audio = content.replace ("\n", "")
    print(audio)
    root_path = os.path.dirname(os.path.dirname(pdf_path))
    output_path = os.path.join(root_path, 'static', 'audios', output_file)
    engine.save_to_file(audio, output_path)
    engine.runAndWait()

def convert_book(pdf_path, name, page):
    file = open(pdf_path, 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages

    if(page<totalpages):
        readPages(pdf_path, name, page, page+1)
    else:
        audio = 'Usted ha concluido el contenido'
        root_path = os.path.dirname(os.path.dirname(pdf_path))
        output_file = f"{name} final.mp3"
        output_path = os.path.join(root_path, 'static', 'audios', output_file)
        engine.save_to_file(audio, output_path)
        engine.runAndWait()
