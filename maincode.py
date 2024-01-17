from ai4bharat.transliteration import XlitEngine
from gtts import gTTS 
import os
def process(intext,lang):
    e = XlitEngine(lang, beam_width=10)
    out = e.translit_sentence(intext)
    print(out)
    mytext1 = list(out.values())
    print("mytext1==",mytext1)
    mytext=str(mytext1)
    language = lang
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    # Playing the converted file 
    os.system("welcome.mp3")
    return mytext
