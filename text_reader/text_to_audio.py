import pyttsx3
import pdfplumber
import PyPDF2
import os

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def readPages(pdf_path, title, initial_page, final_page, user_id):
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
    if(audio==''):
        audio='No hay contenido para leer en esta página'
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(pdf_path)))
    os.makedirs(os.path.join(root_path, 'static', 'audios', f'{user_id}'), exist_ok=True)
    output_path = os.path.join(root_path, 'static', 'audios', f'{user_id}', output_file)
    print(output_path)
    engine.save_to_file(audio, output_path)
    engine.runAndWait()

def convert_book(pdf_path, name, page, user_id):
    file = open(pdf_path, 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages

    if(page<totalpages):
        readPages(pdf_path, name, page, page+1, user_id)
    else:
        audio = 'Usted ha concluido el contenido'
        root_path = os.path.dirname(os.path.dirname(pdf_path))
        output_file = f"{name} {page}-{page+1}.mp3"
        os.makedirs(os.path.join(root_path, 'static', 'audios', f'{user_id}'), exist_ok=True)
        output_path = os.path.join(root_path, 'static', 'audios', f'{user_id}', output_file)
        engine.save_to_file(audio, output_path)
        engine.runAndWait()
