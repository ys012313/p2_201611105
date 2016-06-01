def lab14():
    class Dog(object):
        def talk(self):
            print "wal! wal!"
            
    class ShihtzuDog(Dog):
        def talk(self):
            print "si~ si~"
            
    class Maltese(Dog):
        def talk(self):
            print "mal~? mal!!"
    
    mydog=Dog()
    mydogShihtzu=ShihtzuDog()
    mydogMaltese=Maltese()
    mydog.talk()
    mydogShihtzu.talk()
    mydogMaltese.talk()
    
lab14()