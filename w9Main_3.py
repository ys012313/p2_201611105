def home():
 	import turtle
 	wn=turtle.Screen()	
 	me=set(['TV','cellphone','camera','refrigerator','oven','radio','sofa','lamp','computer','air conditioner'])
 	friend=set(['TV','radio','camera','massager','water purifier','computer','desk','sofa','washer','refrigerator'])
 	print me
 	print "mine"
 	print friend
 	print "friends"
 	both= me&friend
 	all= me.union(friend)
 	print "allmachine"
 	print all
 	print "both"
 	print both
 	print "only mine"
 	print me-both
 	print "only friends"
 	print friend-both
 	wn.exitonclick()

home()