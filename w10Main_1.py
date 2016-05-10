def Milk():
    allData=[ 
 	    ["Coffee","Water","Milk","Icecream"], 
 	    ["Espresso","No","No","No"], 
 	    ["Long Black","Yes","No","No"], 
 	    ["Flat White","No","Yes","No"], 
 	    ["Cappuccino","No","Yes","No"], 
 	    ["Affogatto","No","No","Yes"] 
 	] 
    Data = allData[1:]
    milkcount=0
    for i in Data:
        if i[2].upper()=='YES':
            milkcount=milkcount+1
    print "The percent of milk is",(float(milkcount)/float(len(Data)))*100,"%"

Milk()