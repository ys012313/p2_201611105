﻿lyrics=['When I find myself in times of trouble', 
         'Mother Mary comes to me', 
         'Speaking words of wisdom let it be', 
         'And in my hour of darkness She is standing right in front of me', 
         'Speaking words of wisdom let it be', 
         'Let it be let it be Let it be let it be', 
         'Whisper words of wisdom let it be', 
         'And when the broken hearted people', 
         'Living in the world agree There will be an answer let it be', 
         'For though they may be parted There is still a chance', 
         'that they will see There will be an answer let it be', 
         'Let it be let it be Let it be let it be', 
         'Yeah there will be an answer let it be', 
         'Let it be let it be Let it be let it be', 
         'Whisper words of wisdom let it be', 
         'Let it be let it be Ah let it be yeah let it be', 
         'Whisper words of wisdom let it be', 
         'And when the night is cloudy There is still a light that shines on me', 
         'Shine on until tomorrow let it be', 
         'I wake up to the sound of music', 
         'Mother Mary comes to me Speaking words of wisdom let it be', 
         'Yeah let it be let it be Let it be', 
         'yeah let it be Oh there will be an answer let it be', 
         'Let it be let it be Let it be yeah let it be', 
         'Oh there will be an answer let it be', 
         'Let it be let it be Ah let it be yeah let it be', 
         'Whisper words of wisdom let it be'] 
 
 
d = dict() 
for i in range(0,len(lyrics)): 
     for c in lyrics[i].split(): 
         if c not in d: 
             d[c]=1 
         else: 
             d[c]+=1 
for i in d: 
     if d[i]>20: 
         print i, d[i] 
