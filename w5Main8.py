height=input ("input user height (cm): ")
weight=input ("input user weight (kg): ")
print "%.1f" %height, "%.1f" %weight
BMI=weight*10000/(height*height)
print "%.1f" %BMI
if BMI<=18.5:
    print 'Low weight'
elif 18.5< BMI <25:
    print 'Normal weight'
elif 25<= BMI <30:
    print 'Over weight'
else:
    print 'Obesity'