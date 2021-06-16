from os import path
from pydub import AudioSegment

# files                                                                         
src = "nish.m4a"
dst = "lukshika.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_file(src)
sound.export(dst, format="wav")
