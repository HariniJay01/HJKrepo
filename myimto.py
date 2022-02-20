from PIL import Image
from gtts import gTTS
import os
from pytesseract import image_to_string
def clean(text):
    text=' '.join(text.split('\n'))
    return text
def to_text(image):
    var=image_to_string(Image.open("oneimage.png"))
    res=clean(var)
    return res
def to_sound(text):
    etc=gTTS(text, lang='en')
    etc.save('one.mp3')

def image_to_sound(image):
    ntext=to_text("oneimage.png")
    to_sound(ntext)
    
os.startfile("one.mp3")
