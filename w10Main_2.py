def Grade(): 
     score = [ 
 ["English", 100], 
 ["Math", 200], 
 ["English", 200], 
 ["Math", 200], 
 ["English", 100], 
 ["Math", 300] 
 ] 
     EnScore = 0 
     MaScore = 0 
     for i in range(0,len(score)): 
         if score[i][0]=="English": 
             EnScore=EnScore+score[i][1] 
     for i in range(0,len(score)): 
         if score[i][0]=="Math": 
             MaScore=MaScore+score[i][1] 
 
 
     print "The EnglishScore Sum is", EnScore,"and The MathScore Sum is", MaScore 
     print "The EnglishScore Average is about",EnScore/3,"and The MathScore Average is about",MaScore/3 

Grade()