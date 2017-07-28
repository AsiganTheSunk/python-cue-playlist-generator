#!/usr/bin/python

import time
import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.wavpack import WavPack

print ('PLAYLIST .CUE GENERATOR')
#filename = raw_input('Name your new .cue playlist: ')
#filename = filename + '.cue'
filename = 'newplaylist.cue'

# raw_input('Write the Path to the Songs')
print ('Openning the file...')
target = open(filename, 'w')

#line1 = raw_input('line 1:')



audio_file = mutagen.File('besitos.mp3')
audio_length = str(time.strftime("%M:%S:00", time.gmtime(audio_file.info.length)))
band_name = audio_file.get(key='TPE1')
band_album_name = audio_file.get(key='TALB')
song_name = audio_file.get(key='TIT2')
song_genre = audio_file.get(key='TCON')



print ('Creating Cue PlayList...')
target.write('TITLE \"' + str(band_album_name) + '\"\n')
target.write('PERFORMER \"' + str(band_name) + '\"\n')
target.write('FILE \"' +  str(audio_file.filename) + '\" MP3\n')
target.write('TRACK 01 AUDIO\n')
target.write('TITLE \"' +str(song_name) + '\"\n')
target.write('PERFORMER \"' + str(band_name) + '\"\n')
target.write('INDEX 01 ' + audio_length + '\n')
target.close()



