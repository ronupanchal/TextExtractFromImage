from gtts import gTTS
import os
tts = gTTS(text='Good morning,  A measure of central tendency is a descriptive statistic that describes the average, or typical value of a set of scores', lang='en')
tts.save("good.mp3")
#os.system("mpg321 good.mp3")
