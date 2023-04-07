import PyPDF2 as pdf
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Open the PDF file
with open('pdf reader\CA 2 Marks Unit II.pdf', 'rb') as pdf_file:
    pdf_reader = pdf.PdfFileReader(pdf_file,strict=False)

    # Loop through all the pages in the PDF file
    for page in pdf_reader.pages:
        # Extract text from the page
        page_text = page.extractText()

        # Convert the text to an audio file using Google Text-to-Speech
        tts = gTTS(text=page_text, lang='en')
        tts.save('page_audio.mp3')

        # Load the audio file and play it
        audio_file = AudioSegment.from_mp3('page_audio.mp3')
        play(audio_file)
