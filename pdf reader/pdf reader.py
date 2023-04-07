import pyttsx3
import PyPDF2
book=open("pdf reader\CA 2 Marks Unit II.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(book,strict=False)
pages=pdfReader.numPages
speaker=pyttsx3.init()
for num in range(100,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()

