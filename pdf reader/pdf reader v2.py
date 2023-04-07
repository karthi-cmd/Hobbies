from PyPDF2 import PdfFileReader
import pyttsx3
reader = PdfFileReader("pdf reader\CA 2 Marks Unit II.pdf",strict=False)
engine = pyttsx3.init()# Create a pyttsx3 engine
voices = engine.getProperty('voices')# set the voice
engine.setProperty('voice', voices[1].id)  #Female
engine.setProperty('rate', 150)# set the speed/rate of speech
engine.setProperty('volume',.75)# set the volume
for i in range(reader.numPages):
    page = reader.pages[i]
    text = page.extractText()
    # for j in range(reader.numPages):
    engine.save_to_file(text,'output.mp3')