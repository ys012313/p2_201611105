﻿userA=raw_input('userA input rock, sicssors, paper : ')
userB=raw_input('userB input rock, sicssors, paper : ')
if userA!=userB:
    if userA=='paper' and userB=='rock':
       print 'UserA win'
    elif userA=='rock' and userB=='scissors':
       print 'UserA win'
    elif userA=='sicssors' and userB=='rock':
       print 'UserA win'
    else:
       print 'UserB win'
elif userA==userB:
            print "Draw"