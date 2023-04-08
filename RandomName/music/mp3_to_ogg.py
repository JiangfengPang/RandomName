from pydub import AudioSegment


sound = AudioSegment.from_mp3('bg.mp3')
sound.export('bg.wav', format='wav')

