import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages


for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()