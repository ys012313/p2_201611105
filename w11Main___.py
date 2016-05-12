def satisfaction(): 
     x=list() 
     x2=list() 
     x=[["very good","little good","little bad","very bad"],  
     [13.1,37.1,8.7,1.5],   
     [10.6,34.6,13.4,1.9],   
     [27.1,40.0,2.9,1.5],   
     [16.2,37.8 ,6.8,0.8],   
     [11.4,29.8,14.8 , 4.9],   
     [12.2,  26.5  , 14.9 , 4.4],   
     [13.5,  29.7,  11.1,  2.4],   
     [13.7,  37.6 , 4.1   ,1.2]] 
 
 
     x2=x[1:] 
     verygood=0 
     littlegood=0 
     littlebad=0 
     verybad=0 
     for i in range(len(x2)-1): 
         verygood+=x2[i][0] 
         littlegood+=x2[i][1] 
         littlebad+=x2[i][2] 
         verybad=x2[i][3] 
     goodaverage=(verygood+littlegood)/len(x2) 
     badaverage=(littlebad+verybad)/len(x2) 
      
      
     print "good average" 
     print goodaverage 
     print "bad average" 
     print badaverage 

satisfaction()




speech=["ABOUT to undertake the arduous duties that I have been appointed to perform by the choice of a free people, I avail myself of this customary and solemn occasion to express the gratitude which their confidence inspires and to acknowledge the accountability which my situation enjoins. While the magnitude of their interests convinces me that no thanks can be adequate to the honor they have conferred, it admonishes me that the best return I can make is the zealous dedication of my humble abilities to their service and their good."

"As the instrument of the Federal Constitution it will devolve on me for a stated period to execute the laws of the United States, to superintend their foreign and their confederate relations, to manage their revenue, to command their forces, and, by communications to the Legislature, to watch over and to promote their interests generally. And the principles of action by which I shall endeavor to accomplish this circle of duties it is now proper for me briefly to explain."

"In administering the laws of Congress I shall keep steadily in view the limitations as well as the extent of the Executive power, trusting thereby to discharge the functions of my office without transcending its authority. With foreign nations it will be my study to preserve peace and to cultivate friendship on fair and honorable terms, and in the adjustment of any differences that may exist or arise to exhibit the forbearance becoming a powerful nation rather than the sensibility belonging to a gallant people." 

"In such measures as I may be called on to pursue in regard to the rights of the separate States I hope to be animated by a proper respect for those sovereign members of our Union, taking care not to confound the powers they have reserved to themselves with those they have granted to the Confederacy." 

"The management of the public revenue - that searching operation in all governments - is among the most delicate and important trusts in ours, and it will, of course, demand no inconsiderable share of my official solicitude. Under every aspect in which it can be considered it would appear that advantage must result from the observance of a strict and faithful economy. This I shall aim at the more anxiously both because it will facilitate the extinguishment of the national debt, the unnecessary duration of which is incompatible with real independence, and because it will counteract that tendency to public and private profligacy which a profuse expenditure of money by the Government is but too apt to engender. Powerful auxiliaries to the attainment of this desirable end are to be found in the regulations provided by the wisdom of Congress for the specific appropriation of public money and the prompt accountability of public officers."

"With regard to a proper selection of the subjects of impost with a view to revenue, it would seem to me that the spirit of equity, caution, and compromise in which the Constitution was formed requires that the great interests of agriculture, commerce, and manufactures should be equally favored, and that perhaps the only exception to this rule should consist in the peculiar encouragement of any products of either of them that may be found essential to our national independence."

"Internal improvement and the diffusion of knowledge, so far as they can be promoted by the constitutional acts of the Federal Government, are of high importance." 

"Considering standing armies as dangerous to free governments in time of peace, I shall not seek to enlarge our present establishment, nor disregard that salutary lesson of political experience which teaches that the military should be held subordinate to the civil power. The gradual increase of our Navy, whose flag has displayed in distant climes our skill in navigation and our fame in arms; the preservation of our forts, arsenals, and dockyards, and the introduction of progressive improvements in the discipline and science of both branches of our military service are so plainly prescribed by prudence that I should be excused for omitting their mention sooner than for enlarging on their importance. But the bulwark of our defense is the national militia, which in the present state of our intelligence and population must render us invincible. As long as our Government is administered for the good of the people, and is regulated by their will; as long as it secures to us the rights of person and of property, liberty of conscience and of the press, it will be worth defending; and so long as it is worth defending a patriotic militia will cover it with an impenetrable aegis. Partial injuries and occasional mortifications we may be subjected to, but a million of armed freemen, possessed of the means of war, can never be conquered by a foreign foe. To any just system, therefore, calculated to strengthen this natural safeguard of the country I shall cheerfully lend all the aid in my power." 

"It will be my sincere and constant desire to observe toward the Indian tribes within our limits a just and liberal policy, and to give that humane and considerate attention to their rights and their wants which is consistent with the habits of our Government and the feelings of our people." 

"The recent demonstration of public sentiment inscribes on the list of Executive duties, in characters too legible to be overlooked, the task of reform, which will require particularly the correction of those abuses that have brought the patronage of the Federal Government into conflict with the freedom of elections, and the counteraction of those causes which have disturbed the rightful course of appointment and have placed or continued power in unfaithful or incompetent hands." 

"In the performance of a task thus generally delineated I shall endeavor to select men whose diligence and talents will insure in their respective stations able and faithful cooperation, depending for the advancement of the public service more on the integrity and zeal of the public officers than on their numbers."

"A diffidence, perhaps too just, in my own qualifications will teach me to look with reverence to the examples of public virtue left by my illustrious predecessors, and with veneration to the lights that flow from the mind that founded and the mind that reformed our system. The same diffidence induces me to hope for instruction and aid from the coordinate branches of the Government, and for the indulgence and support of my fellow-citizens generally. And a firm reliance on the goodness of that Power whose providence mercifully protected our national infancy, and has since upheld our liberties in various vicissitudes, encourages me to offer up my ardent supplications that He will continue to make our beloved country the object of His divine care and gracious benediction."]

 
def countWords1(): 
        d = {}
        for sentence in speech: 
             words=sentence.split() 
        for word in words: 
                if word in d: 
                    d[word]+=1 
                else: 
                    d[word]=1 
        return d 
def MostMentionedWords1(c,d): 
        a=list() 
        for i in d: 
            if d[i]>c: 
                a.append(i) 
        return a 
word=countWords1() 
mmwords1=MostMentionedWords1(12,word) 
print "Andrew Jackson's speech most mentioned words:", mmwords1




speech=["At this last presidential inauguration of the 20th century, let us lift our eyes toward the challenges that await us in the next century. It is our great good fortune that time and chance have put us not only at the edge of a new century, in a new millennium, but on the edge of a bright new prospect in human affairs - a moment that will define our course, and our character, for decades to come. We must keep our old democracy forever young. Guided by the ancient vision of a promised land, let us set our sights upon a land of new promise." 

"The promise of America was born in the 18th century out of the bold conviction that we are all created equal. It was extended and preserved in the 19th century, when our nation spread across the continent, saved the union, and abolished the awful scourge of slavery." 

"Then, in turmoil and triumph, that promise exploded onto the world stage to make this the American Century." 

"And what a century it has been. America became the world's mightiest industrial power; saved the world from tyranny in two world wars and a long cold war; and time and again, reached out across the globe to millions who, like us, longed for the blessings of liberty." 

"Along the way, Americans produced a great middle class and security in old age; built unrivaled centers of learning and opened public schools to all; split the atom and explored the heavens; invented the computer and the microchip; and deepened the wellspring of justice by making a revolution in civil rights for African Americans and all minorities, and extending the circle of citizenship, opportunity and dignity to women." 

"Now, for the third time, a new century is upon us, and another time to choose. We began the 19th century with a choice, to spread our nation from coast to coast. We began the 20th century with a choice, to harness the Industrial Revolution to our values of free enterprise, conservation, and human decency. Those choices made all the difference. At the dawn of the 21st century a free people must now choose to shape the forces of the Information Age and the global society, to unleash the limitless potential of all our people, and, yes, to form a more perfect union." 

"When last we gathered, our march to this new future seemed less certain than it does today. We vowed then to set a clear course to renew our nation."

"In these four years, we have been touched by tragedy, exhilarated by challenge, strengthened by achievement. America stands alone as the world's indispensable nation. Once again, our economy is the strongest on Earth. Once again, we are building stronger families, thriving communities, better educational opportunities, a cleaner environment. Problems that once seemed destined to deepen now bend to our efforts: our streets are safer and record numbers of our fellow citizens have moved from welfare to work." 

"And once again, we have resolved for our time a great debate over the role of government. Today we can declare: Government is not the problem, and government is not the solution. We - the American people - we are the solution. Our founders understood that well and gave us a democracy strong enough to endure for centuries, flexible enough to face our common challenges and advance our common dreams in each new day."

"As times change, so government must change. We need a new government for a new century - humble enough not to try to solve all our problems for us, but strong enough to give us the tools to solve our problems for ourselves; a government that is smaller, lives within its means, and does more with less. Yet where it can stand up for our values and interests in the world, and where it can give Americans the power to make a real difference in their everyday lives, government should do more, not less. The preeminent mission of our new government is to give all Americans an opportunity - not a guarantee, but a real opportunity - to build better lives." 

"Beyond that, my fellow citizens, the future is up to us. Our founders taught us that the preservation of our liberty and our union depends upon responsible citizenship. And we need a new sense of responsibility for a new century. There is work to do, work that government alone cannot do: teaching children to read; hiring people off welfare rolls; coming out from behind locked doors and shuttered windows to help reclaim our streets from drugs and gangs and crime; taking time out of our own lives to serve others." 

"Each and every one of us, in our own way, must assume personal responsibility - not only for ourselves and our families, but for our neighbors and our nation. Our greatest responsibility is to embrace a new spirit of community for a new century. For any one of us to succeed, we must succeed as one America." 

"The challenge of our past remains the challenge of our future - will we be one nation, one people, with one common destiny, or not? Will we all come together, or come apart?" 

"The divide of race has been America's constant curse. And each new wave of immigrants gives new targets to old prejudices. Prejudice and contempt, cloaked in the pretense of religious or political conviction are no different. These forces have nearly destroyed our nation in the past. They plague us still. They fuel the fanaticism of terror. And they torment the lives of millions in fractured nations all around the world."

"These obsessions cripple both those who hate and, of course, those who are hated, robbing both of what they might become. We cannot, we will not, succumb to the dark impulses that lurk in the far regions of the soul everywhere. We shall overcome them. And we shall replace them with the generous spirit of a people who feel at home with one another." 

"Our rich texture of racial, religious and political diversity will be a Godsend in the 21st century. Great rewards will come to those who can live together, learn together, work together, forge new ties that bind together." 

"As this new era approaches we can already see its broad outlines. Ten years ago, the Internet was the mystical province of physicists; today, it is a commonplace encyclopedia for millions of schoolchildren. Scientists now are decoding the blueprint of human life. Cures for our most feared illnesses seem close at hand." 

"The world is no longer divided into two hostile camps. Instead, now we are building bonds with nations that once were our adversaries. Growing connections of commerce and culture give us a chance to lift the fortunes and spirits of people the world over. And for the very first time in all of history, more people on this planet live under democracy than dictatorship."

"My fellow Americans, as we look back at this remarkable century, we may ask, can we hope not just to follow, but even to surpass the achievements of the 20th century in America and to avoid the awful bloodshed that stained its legacy? To that question, every American here and every American in our land today must answer a resounding “Yes.” "

"This is the heart of our task. With a new vision of government, a new sense of responsibility, a new spirit of community, we will sustain America's journey. The promise we sought in a new land we will find again in a land of new promise." 

"In this new land, education will be every citizen's most prized possession. Our schools will have the highest standards in the world, igniting the spark of possibility in the eyes of every girl and every boy. And the doors of higher education will be open to all. The knowledge and power of the Information Age will be within reach not just of the few, but of every classroom, every library, every child. Parents and children will have time not only to work, but to read and play together. And the plans they make at their kitchen table will be those of a better home, a better job, the certain chance to go to college." 

"Our streets will echo again with the laughter of our children, because no one will try to shoot them or sell them drugs anymore. Everyone who can work, will work, with today's permanent under class part of tomorrow's growing middle class. New miracles of medicine at last will reach not only those who can claim care now, but the children and hardworking families too long denied."

"We will stand mighty for peace and freedom, and maintain a strong defense against terror and destruction. Our children will sleep free from the threat of nuclear, chemical or biological weapons. Ports and airports, farms and factories will thrive with trade and innovation and ideas. And the world's greatest democracy will lead a whole world of democracies."

"Our land of new promise will be a nation that meets its obligations - a nation that balances its budget, but never loses the balance of its values. A nation where our grandparents have secure retirement and health care, and their grandchildren know we have made the reforms necessary to sustain those benefits for their time. A nation that fortifies the world's most productive economy even as it protects the great natural bounty of our water, air, and majestic land." 

"And in this land of new promise, we will have reformed our politics so that the voice of the people will always speak louder than the din of narrow interests - regaining the participation and deserving the trust of all Americans." 

"Fellow citizens, let us build that America, a nation ever moving forward toward realizing the full potential of all its citizens. Prosperity and power - yes, they are important, and we must maintain them. But let us never forget: The greatest progress we have made, and the greatest progress we have yet to make, is in the human heart. In the end, all the world's wealth and a thousand armies are no match for the strength and decency of the human spirit." 

"Thirty-four years ago, the man whose life we celebrate today spoke to us down there, at the other end of this Mall, in words that moved the conscience of a nation. Like a prophet of old, he told of his dream that one day America would rise up and treat all its citizens as equals before the law and in the heart. Martin Luther King's dream was the American Dream. His quest is our quest: the ceaseless striving to live out our true creed. Our history has been built on such dreams and labors. And by our dreams and labors we will redeem the promise of America in the 21st century."

"To that effort I pledge all my strength and every power of my office. I ask the members of Congress here to join in that pledge. The American people returned to office a President of one party and a Congress of another. Surely, they did not do this to advance the politics of petty bickering and extreme partisanship they plainly deplore. No, they call on us instead to be repairers of the breach, and to move on with America's mission."

"America demands and deserves big things from us - and nothing big ever came from being small. Let us remember the timeless wisdom of Cardinal Bernardin, when facing the end of his own life. He said: “It is wrong to waste the precious gift of time, on acrimony and division.” "

"Fellow citizens, we must not waste the precious gift of this time. For all of us are on that same journey of our lives, and our journey, too, will come to an end. But the journey of our America must go on."

"And so, my fellow Americans, we must be strong, for there is much to dare. The demands of our time are great and they are different. Let us meet them with faith and courage, with patience and a grateful and happy heart. Let us shape the hope of this day into the noblest chapter in our history. Yes, let us build our bridge. A bridge wide enough and strong enough for every American to cross over to a blessed land of new promise."

"May those generations whose faces we cannot yet see, whose names we may never know, say of us here that we led our beloved land into a new century with the American Dream alive for all her children; with the American promise of a more perfect union a reality for all her people; with America's bright flame of freedom spreading throughout all the world." 

"From the height of this place and the summit of this century, let us go forth. May God strengthen our hands for the good work ahead - and always, always bless our America." 
]
def countWords2(): 
        d = {}
        for sentence in speech: 
             words=sentence.split() 
        for word in words: 
                if word in d: 
                    d[word]+=1 
                else: 
                    d[word]=1 
        return d 
def MostMentionedWords2(b,d): 
        q=list() 
        for i in d: 
            if d[i]>b: 
                q.append(i) 
        return q 
word=countWords2() 
mmwords2=MostMentionedWords2(26,word) 
print "Bill Clinton's speech most mentioned words:", mmwords2 
 
