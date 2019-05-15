### -*- coding: cp936 -*-
####import random , easygui
####secret = random.randint(1,99)
####guess = 0
####for guess <= 6
####    guessnumber = easygui.enterbox("your number")
####    if guessnumber < secret
####        print("too small")
####    elseif guessnumber > secret
####        print("too large")
####        guess
####    else
####        print("yes")
####        guess = 7
##
####import random, easygui
####secret = random.randint(1, 99)
####guess = 0
####tries = 0
####easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts,
####and I have a secret!It is a number from 1 to 99. I'll give you 6 tries.""")
####while guess != secret and tries < 6:
####    guess = easygui.integerbox("What's yer guess, matey?")
####    if not guess: break
####    if guess < secret:
####        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
####    elif guess > secret:
####        easygui.msgbox(str(guess) + " is too high, landlubber!")
####    tries = tries + 1
####if guess == secret:
####    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
####else:
####    easygui.msgbox("No more guesses! The number was " + str(secret))
##
####import easygui
####F = easygui.enterbox("please enter fahrenheit temperature")
####F = float(F)
####celsius = (F - 32) * 5.0 / 9
####celsius = str(celsius)
####C = easygui.msgbox("celsius is" + celsius)
##
####import easygui
####name = easygui.enterbox("name")
####roomnumber = easygui.enterbox("room number")
####city = easygui.enterbox("city")
####easygui.msgbox(name+','+roomnumber+'\n'+city)
##
####import easygui
####correctAnswer = 1
####score = 0
####timsAnswer = easygui.integerbox("timsanswer")
####if timsAnswer == correctAnswer:
####    print "You got it right!"
####    score = score + 1
####else:
####    print "Wrong! Thanks for playing."
##    
####number = float(raw_input("enter your number please"+"\n"))
####if number > 15:
####    print ("the number is more than 15")
####elif number >5:
####    print ("the number is more than 5")
####else:
####    print ("the number is less than 5")
##
####age = int(raw_input("Plz enter your age: "+"\n"))
####grade = int(raw_input("Plz enter your grade: "+"\n"))
####if not(age <= 9 and grade >= 3):
####    print ("thank you for your attendence!")
####else:
####    print("You are accepted!")
##
####my_number = 35
####if my_number > 30 and my_number <=40:
####    print 'Under 20'
####else:
####    print '20 or over'
##
####price = float(raw_input("price of the thing : "))
##
####import easygui
####price = easygui.enterbox("price of the thing : ")
####price = float (price)
####realprice = 0
####discount = 1
####if price <= 10:
####    discount = 0.9
####else:
####    discount = 0.8
####realprice = price * discount
####print(realprice)
##
####import easygui
####gender = easygui.buttonbox("What is your gender?",choices=["male","female"])
####if gender == "female":
####    age = easygui.integerbox("What is your age?")
####    if 10 <= age <= 12:
####        print("you are accepted!")
####    else:
####        print("sorry! you are invalid!")
####else:
####    print("sorry! you are invalid!")
##
##
##
####import easygui
####size = easygui.enterbox("maximum oil you can take : ")
####remaining = easygui.enterbox("percentage of remaining oil : ")
####length = easygui.enterbox("the distance you can drive with one L : ")
####size = int(size)
####remaining = int (remaining)
####length = int (length)
####distance = size * length * remaining /100.0
####print("size of tank ",size)
####print("percent full ",remaining)
####print("km per liter ",length)
####print("You can go another ",distance)
####print("The next gas station is 200 km away ")
####if distance < 200:
####    print("You can't wait for the next station.")
####else:
####    print("You can wait for the next station.")
##    
####import easygui
####password = 123456
####pd = raw_input("please input your password:")
####pd = int(pd)
####if pd != password:
####    print("you are wrong, you cannot use the program!")
####else:
####    import easygui
####    size = easygui.enterbox("maximum oil you can take : ")
####    remaining = easygui.enterbox("percentage of remaining oil : ")
####    length = easygui.enterbox("the distance you can drive with one L : ")
####    size = int(size)
####    remaining = int (remaining)
####    length = int (length)
####    distance = size * length * remaining /100.0
####    print("size of tank ",size)
####    print("percent full ",remaining)
####    print("km per liter ",length)
####    print("You can go another ",distance)
####    print("The next gas station is 200 km away ")
####    if distance < 200:
####        print("You can't wait for the next station.")
####    else:
####        print("You can wait for the next station.")
##
####for i in range(10,1,-2):
####    print i
##
####import time
####for i in range(10,0,-1):
####    print i
####    time.sleep(0.5)
####print("time is over")
##
####for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
####    print cool_guy, "is the coolest guy ever!"
##    
##
####a = raw_input("3 jixu, qiyu quit:")
####b = a
####while b == "3":
####    b = raw_input("3 jixu, qiyu quit:")
##
####for i in range (1,6):
####    print
####    print 'i =', i,
####    print 'Hello, how',
####    if i == 3:
####        break
####    print 'are you today?'
##
####for i in range(8):
####    print(i)
##
####a = raw_input("How many?:")
####b = raw_input("How high?:")
####a=int(a)
####b=int(b)
####i=1
####print("here:")
####while i != b+1:
####    print a,'*',i,"=", a*i
####    i+=1
####
####a = raw_input("How many?:")
####b = raw_input("How high?:")
####a=int(a)
####b=int(b)
####i=1
####print("here:")
####for i in range(1,b+1):
####    print a,'*',i,"=", a*i
####    i+=1
##
##
##import pygame, sys, random
##skier_images = ["skier_down.png", "skier_right1.png",
##                "skier_right2.png", "skier_left2.png",
##                "skier_left1.png"]
##class SkierClass(pygame.sprite.Sprite):
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.image.load("skier_down.png")
##        self.rect = self.image.get_rect()
##        self.rect.center = [320, 100]
##        self.angle = 0
##    def turn(self, direction):
##        self.angle = self.angle + direction
##        if self.angle < -2: self.angle = -2
##        if self.angle > 2: self.angle = 2
##        center = self.rect.center
##        self.image = pygame.image.load(skier_images[self.angle])
##        self.rect = self.image.get_rect()
##        self.rect.center = center
##        speed = [self.angle, 6 - abs(self.angle) * 2]
##        return speed
##    def move(self, speed):
##        self.rect.centerx = self.rect.centerx + speed[0]
##        if self.rect.centerx < 20: self.rect.centerx = 20
##        if self.rect.centerx > 620: self.rect.centerx = 620
##
##class ObstacleClass(pygame.sprite.Sprite):
##    def __init__(self, image_file, location, type):
##        pygame.sprite.Sprite.__init__(self)
##        self.image_file = image_file
##        self.image = pygame.image.load(image_file)
##        self.rect = self.image.get_rect()
##        self.rect.center = location
##        self.type = type
##        self.passed = False
##    def update(self):
##        global speed
##        self.rect.centery -= speed[1]
##        if self.rect.centery < -32:
##            self.kill()
##
##def create_map():
##    global obstacles
##    locations = []
##    for i in range(10):
##        row = random.randint(0, 9)
##        col = random.randint(0, 9)
##        location = [col * 64 + 20, row * 64 + 20 + 640]
##        if not (location in locations):
##            locations.append(location)
##            type = random.choice(["tree", "flag"])
##            if type == "tree": img = "skier_tree.png"
##            elif type == "flag": img = "skier_flag.png"
##            obstacle = ObstacleClass(img, location, type)
##            obstacles.add(obstacle)
##def animate():
##    screen.fill([255, 255, 255])
##    obstacles.draw(screen)
##    screen.blit(skier.image, skier.rect)
##    screen.blit(score_text, [10, 10])
##    pygame.display.flip()
##
##pygame.init()
##screen = pygame.display.set_mode([640,640])
##clock = pygame.time.Clock()
##skier = SkierClass()
##speed = [0, 6]
##obstacles = pygame.sprite.Group()
##map_position = 0
##points = 0
##create_map()
##font = pygame.font.Font(None, 50)
##running = True
##while running:
##    
##    clock.tick(30)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                speed = skier.turn(-1)
##            elif event.key == pygame.K_RIGHT:
##                speed = skier.turn(1)
##    skier.move(speed)
##
##    map_position += speed[1]
##
##    if map_position >=640:
##        create_map()
##        map_position = 0
##    hit = pygame.sprite.spritecollide(skier, obstacles, False)
##    if hit:
##        if hit[0].type == "tree" and not hit[0].passed:
##            points = points - 100
##            skier.image = pygame.image.load("skier_crash.png")
##            animate()
##            pygame.time.delay(1000)
##            skier.image = pygame.image.load("skier_down.png")
##            skier.angle = 0
##            speed = [0, 6]
##            hit[0].passed = True
##        elif hit[0].type == "flag" and not hit[0].passed:
##            points += 10
##            hit[0].kill()
##    obstacles.update()
##    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
##    animate()
##pygame.quit()

##import random
##tries = 0
##guess = 0
##a = random.randint(1,99)
##while guess != a and tries < 6:
##    guess = raw_input("Guess the number: ")
##    guess = int(guess)
##    if guess < a:
##        print("too low")
##    elif guess > a:
##        print("too high")
##    else:
##        break
##    tries+=1
##if guess == a:
##    print "you get it, the number is",a
##else:
##    print "sorry, your tries are used up"

##import easygui
##for i in range(1,4):
##    k = easygui.integerbox("first num: ")
##    m = easygui.integerbox("to what: ")
##    for j in range(1,m+1):
##        print k,"*",j,"=",k*j
##    print


##k = raw_input("how many raws do you want? ")
##k=int(k)
##j = raw_input("how many stars do you want? ")
##j = int(j)
##for i in range (1,k+1):
##    for s in range(1,j+1):
##        print "*",
##    print

##import easygui
##i = easygui.integerbox("how many cells:")
##j = easygui.integerbox("how many raws:")
##k = easygui.integerbox("how many stars in a row:")
##for o in range(i):
##    for p in range(j):
##        for q in range(k):
##            print "*",
##        print
##    print

##for i in range(1,11):
##    for j in range(1,11):
##        for k in range(1,11):
##            if i!=j and i!=k and j!=k:
##                print i,j,k

##for i in range(1,11):
##    for j in range(1,i):
##        for k in range(1,j):
##            if i!=j and i!=k and j!=k:
##                print i,j,k            

##for i in range(2):
##    for j in range(2):
##        for k in range(2):
##            for l in range(2):
##                for m in range(2):
##                    print i,"hotdog,",j,"bread,",k,"番茄酱,",l,"芥末酱,",m,"洋葱"

##ehotdog = 140
##ebun = 120
##eketchup = 20
##emustard = 80
##eonion = 40
##count = 1
##print "num\t\thotdog\t\tbun\t\tketchup\t\tmustard\t\tonion\t\tenergy"
##for dog in [0, 1]:
##    for bun in [0, 1]:
##        for ketchup in [0, 1]:
##            for mustard in [0, 1]:
##                for onion in [0, 1]:
##                    print "#", count, "\t","\t" ,
##                    print dog, "\t","\t" , bun, "\t","\t" , ketchup, "\t","\t" ,\
##                    mustard, "\t","\t" , onion, "\t","\t" ,
##                    print ehotdog * dog + ebun * bun + eketchup * ketchup + emustard * mustard + eonion * onion
##                    count = count + 1


##for i in range(5):
##    for j in range(3):
##        print '*',
##    print
            
##import time,easygui
##times = easygui.integerbox("start from which?")
##for i in range(times,0,-1):
##    print i,
##    for j in range(i,0,-1):
##        print "*",
##    print
##    time.sleep(1)
##print "OVER"

##newlist = []
##newlist.append("ZN")
##rootlist = ["a","b",1,1]
##rootlist.append(newlist)
##print rootlist
####for i in range(4):
##print rootlist[1:2]
##print rootlist[1]
##    

##newlist = [1,2,3,3,4,"a","dog"]
##print newlist
##newlist[3] = 5
##newlist.append("zn")
##print newlist
##newlist.extend([1,2,34])
##print newlist
##newlist.pop()
##print newlist
##newlist.pop(3)
##print newlist
##del newlist[1]
##print newlist
##newlist.remove(2)
##print newlist

##import easygui
##l = ["a" , "b" , "c" , "d" , "1" , 1 , "2" , 3]
##i = easygui.enterbox("what character do you need to detect?")
##if i in l:
##    print i,"in"
##else:
##    print i,"out"

##l = ["a" , "b" , "c" , "d" , 3 , 1 , "2" , 3 , "ac" ,"z"]
##l.sort(reverse=True)
##print l

##oldlist = [1,3,2,6,7,4]
##newlist = oldlist[:]
##newlist.sort(reverse=False)
##print oldlist

##myfirsttuple = (1,2,3,"4","z")
##print myfirsttuple

##amark = [99 , 100 , 87 , 89]
##bmark = [87 , 29  , 13 , 80]
##cmark = [87 , 98  , 12 , 45]
##d = [amark , bmark ,cmark]
##print amark
##print bmark
##print cmark
##print d
##for i in d:
##    print i

##classmark = [[55,63,77,81],[65,61,67,72],[97,95,92,88]]
##print classmark [1][3]

##phone = {}
##phone ["john"] = "123456"
##phone ['nan'] = "18751209701"
##print phone

##phone = {"john" : "123456", 'nan' : "18751209701"}
##print phone

##phone = {"a" : 174049 , "b" : 170451 , "c" : 173271 , "d" :172123}
##values = phone.values()[:]
##print phone.values()
##keys = phone.keys()[:]
##print phone.keys()
##newlist = sorted(values)
##
##for i in newlist:
##    j = values.index(i)
##    print keys[j],values[j]

##dic = {"a":174029,"b":172392,"c":172302,"d":173301}
##print dic
##keys = dic.keys()[:]
##values = dic.values()[:]
##newvalues = sorted(values)
##newvalues.sort(reverse = True)
##print newvalues
##for i in newvalues:
##    j = values.index(i)
##    print keys[j],values[j]

##dic = {"a":174029,"b":172392,"c":172302,"d":173301}
##for i in sorted(dic.values()):
##    for j in dic.keys():
##        if dic[j] == i:
##            print j,i

##letter = [1,2,3,4,5,6,7]
##print letter
##letter.pop(3)
##print letter
##newletter = sorted(letter)
##newletter.pop()
##print newletter

##dic = {"a":174029,"b":172392,"c":172302,"d":173301}
##for i in sorted(dic.values()[:]):
##    print dic.keys()[dic.values().index(i)],i

##dic = {"a":174029,"b":172392,"c":172302,"d":173301}
##del dic["a"]
##print dic

##oldlist = [1,3,2,9,4,"a","dog"]
##newlist = sorted(oldlist)
##newlis = oldlist[:]
##newlis.sort()
##print oldlist
##print newlist
##print newlis

##import easygui
##list = []
##for i in range(5):
##    list.append(easygui.enterbox("enter name:"))
##for i in range(5):
##    print list[i]
##tobedelete = easygui.choicebox("which do you want \
##to delete:",choices=[list[0],list[1],list[2],list[3],list[4]])
##list[list.index(tobedelete)] = easygui.enterbox("input a new name:")
##print list

##import easygui
##dic = {"computer":"A machine that does math very fast"}
##for i in range(3):
##    j = easygui.buttonbox("Add or look up a word?",choices=["a","l"])
##    
##    if j == "a":
##        typeword = easygui.enterbox("Type the word:")
##        print "Type the word:",typeword
##        if typeword in dic:
##            print "The word has been added."
##        else:
##            typemeaning = easygui.enterbox("Type the meaning:")
##            dic[typeword] = typemeaning
##            print "Type the meaning:",dic[typeword]
##    else:
##        word = easygui.enterbox("Type the word:")
##        if word in dic:
##            print "Type the word:",word
##            print dic[word]
##        else:
##            print "Type the word:",word
##            print "The word is not in the dic yet"
        
##def printMyAddress(myname,mynum):
##    print myname
##    print "my home number is",mynum
##    print
##
##printMyAddress("dog",78)

##def calculateTax(income,percentage):
##    tax = income * percentage
##    return tax
##
##T = calculateTax(120000,0.2)
##print T

##import easygui
##
##def Tax(income,percentage):
##    print b
##    money = income * percentage
##    return money
##
##wage = easygui.enterbox("How much money do you earn each year?")
##a = Tax(int(wage),0.15)
##b = Tax(100000,0.15)
##print a 

##def myTax(income,rate):
##    taxMoney = income * rate
##    myIncome = 1000
##    print "myIncome (inside)",myIncome
##    return taxMoney
##
##myIncome = float(raw_input("your income:"))
##a = myTax(myIncome,0.06)
##print a
##print myIncome

##def zletter(i):
##    if i == 0:
##        print "Z Z Z Z Z Z",
##    if i == 1:    
##        print "        Z  ",
##    if i == 2:
##        print "      Z    ",
##    if i == 3:
##        print "    Z      ",
##    if i == 4:
##        print "  Z        ",
##    if i == 5:
##        print "Z Z Z Z Z Z",
##    
##def hletter(i):
##    if i == 0:
##        print "H         H",
##    if i == 1:    
##        print "H         H",
##    if i == 2:
##        print "HHHHHHHHHHH",
##    if i == 3:
##        print "H         H",
##    if i == 4:
##        print "H         H",
##    if i == 5:
##        print "H         H",
##
##def oletter(i):
##    if i == 0:
##        print "     O     ",
##    if i == 1:    
##        print "  O     O  ",
##    if i == 2:
##        print "O         O",
##    if i == 3:
##        print " O       O ",
##    if i == 4:
##        print "   O   O   ",
##    if i == 5:
##        print "     O     ",
##
##def uletter(i):
##    if i == 0:
##        print "U         U",
##    if i == 1:    
##        print "U         U",
##    if i == 2:
##        print "U         U",
##    if i == 3:
##        print "U         U",
##    if i == 4:
##        print "U         U",
##    if i == 5:
##        print "   U   U   ",
##
##def nletter(i):
##    if i == 5:
##        print "N         N",
##    if i == 4:    
##        print "N       N N",
##    if i == 3:
##        print "N     N   N",
##    if i == 2:
##        print "N   N     N",
##    if i == 1:
##        print "N N       N",
##    if i == 0:
##        print "N         N",
##
##def aletter(i):
##    if i == 0:
##        print "     A     ",
##    if i == 1:    
##        print "    A A    ",
##    if i == 2:
##        print "   A   A   ",
##    if i == 3:
##        print "  AAAAAAA  ",
##    if i == 4:
##        print " A       A ",
##    if i == 5:
##        print "A         A",
##
##for i in range(6):
##    zletter(i)
##    hletter(i)
##    oletter(i)
##    uletter(i)
##    nletter(i)
##    aletter(i)
##    nletter(i)
##    print


##def information(list):
##    print "name:\t\t",list[0]
##    print "adress:\t\t",list[1]
##    print "street:\t\t",list[2]
##    print "city:\t\t",list[3]
##    print "state:\t\t",list[4]
##    print "num:\t\t",list[5]
##    print "country:\t",list[6]
##
##a=["Zhounan","Shanghai","SJTU","Dongchuan Road","Jiangsu","213300","China"]
##information(a)

##def calculateTax(price, tax_rate):
##    total = price + (price * tax_rate)
##    global my_price
##    my_price = 10000
##    print "my_price (inside function) = ", my_price
##    return total
##
##my_price = float(raw_input ("Enter a price: "))
##totalPrice = calculateTax(my_price, 0.06)
##print "price = ", my_price, " Total price = ", totalPrice
##print "my_price (outside function) = ", my_price

##def total(i5,i2,i1):
##    total = i5 * 5 + i2 * 2 + i1 * 1
##    return total
##
##for i in range (1):
##    a = float(raw_input("how many 5 cents?"))
##    b = float(raw_input("how many 2 cents?"))
##    c = float(raw_input("how many 1 cents?"))
##d = total(a, b, c)
##print d

##class Ball:
##    def bounce(self):
##        if self.direction == "down":
##            self.direction = "up"
##
##myball = Ball()
##myball.direction = "down"
##myball.color = "green"
##myball.shape = "circle"
##myball.bounce()
##print "My ball's color:",myball.color
##print "My ball's shape:",myball.shape
##print "My ball's direction:",myball.direction

##class Ball:
##    def __init__(self,color,direction,size):
##        self.color = "a"
##        self.size = "b"
##        self.direction = "up"
##    def __str__(self):
##        msg = "Hi,I'm a "+ self.size + " " + self.color + " ball!"
##        return msg
##    def bounce(self):
##        if self.direction == "down":
##            self.direction = "up"
##
##myball = Ball("green","down","small")
##myball.bounce()
##print myball.direction
##print myball.color
##print myball.size
##print myball

##class hotDog:
##    def __init__(self):
##        self.cooked_level = 0
##        self.cooked_string = "raw"
##        self.condiments = []
####    def __str__(self):
####        msg = "It is a "+self.cooked_string+" cooked for "+self.cooked_level +" minutes hotdog with "+self.condiments
####        return msg
####    def cook(self,time):
####        self.cooked_level = self.cook_level + time
####    if self.cooked_level > 8:
####        self.cooked_string = "Charcoal"
####    else:
####        self.cooked_string = "Raw"
####first = hotDog("20","fully-cooked","tomato comdiment")
####print first
##mydog = hotDog()
##print mydog.cooked_string
##print mydog.cooked_level
##print mydog.condiments

##class HotDog:
##    def __init__(self):
##        self.cooked_level = 0
##        self.cooked_string = "Raw"
##        self.condiments = []
####    def cook(self, time):
####        self.cooked_level = self.cooked_level + time
####        if self.cooked_level > 8:
####            self.cooked_string = "Charcoal"
####        elif self.cooked_level > 5:
####            self.cooked_string = "Well-done"
####        elif self.cooked_level > 3:
####            self.cooked_string = "Medium"
####        else:
####            self.cooked_string = "Raw"
##myDog = HotDog()
##print myDog.cooked_level
##print myDog.cooked_string
##print myDog.condiments

##class HotDog:
##    def __init__(self):
####        global cooked_level
####        global cooked_string
####        global condiment
##        self.cooked_level = 0
##        self.cooked_string = "Raw"
##        self.condiment = ""
##    def cook(self,time):
##        self.cooked_level = self.cooked_level + time
##        if self.cooked_level > 8:
##            self.cooked_string = "Cooked too much"
##        elif self.cooked_level > 5:
##            self.cooked_string = "Quiet well cooked"
##        else:
##            self.cooked_string = "Raw"
##    def __str__(self):
##        msg = "it is a "+self.cooked_string+" hotdog cooked for "+ str(self.cooked_level) + " minutes with "+self.condiment+ " on it."
##        return msg
##mydog = HotDog()
##mydog.cook(6)
##print mydog.cooked_level
##print mydog.cooked_string
##print mydog.condiment
##print mydog

##class HotDog:
##    def __init__(self):
##        self.cooktime = 0
##        self.cooklevel = "Raw"
##        self.condiment = []
##    def cook(self,time):
##        self.cooktime = self.cooktime + time
##        if self.cooktime > 8:
##            self.cooklevel = "old"
##        elif self.cooktime > 5:
##            self.cooklevel = "well-cooked"
##        else:
##            self.cooklevel = "Raw"
##    def addcondi(self,condi):
##        self.condiment.append(condi)
##    def __str__(self):
##        msg = "it is a "+self.cooklevel+" hotdog cooked for "+str(self.cooktime)+" minutes "
##        if self.condiment != []:
##            msg = msg + "with "
##            for i in self.condiment:
##                msg =msg+ i + " on it."
##        else:
##            msg = msg + "."
##        return msg
##
##mydog = HotDog()
##mydog.cook(7)
##
##print mydog
##mydog.addcondi("tomato condiment")
##print mydog

##import easygui
##class HotDog:
##    def __init__(self):
##        self.cooktime = 0
##        self.cooklevel = "Raw"
##        self.condiment = []
##    def cook(self,time):
##        self.cooktime = self.cooktime + time
##        if self.cooktime > 8:
##            self.cooklevel = "old"
##        elif self.cooktime > 5:
##            self.cooklevel = "well-cooked"
##        else:
##            self.cooklevel = "Raw"
##    def addcondi(self):
##        condi = easygui.enterbox("enter your condiment please:")
##        self.condiment.append(condi)
##    def __str__(self):
##        msg = "it is a "+self.cooklevel+" hotdog cooked for "+str(self.cooktime)+" minutes "
##        if self.condiment != []:
##            msg = msg + "with "
##            for i in self.condiment:
##                msg =msg+ i + " on it."
##        else:
##            msg = msg + "."
##        return msg
##
##mydog = HotDog()
##mydog.cook(7)
##
##print mydog
##mydog.addcondi()
##print mydog


###多态
##class Aa:
##    def __init__(self):
##        self.size = 0
##        self.color = "green"
##class Bb:
##    def __init__(self):
##        self.size = 1
##        self.color = "red"
##
##mya = Aa()
##print mya.size
##myb = Bb()
##print myb.size


###继承
##class animal:
##    def __init__(self,name):
##        self.name = name
##
##    def size(self,daxiao):
##        self.size = daxiao
##
##class dog(animal):
##    def __init__(self,value):
##        self.value = value
##
##    def statement(self):
##        print "My dog is called "+\
##              self.name+". Its size is "+\
##              self.size+". Its price is "+ str(self.value)
##
##mydog = dog(100)
##mydog.name = "poppy"
##mydog.size("large")
##mydog.statement()

##class BankAccount(object):
##    def __init__(self):
##        self.account = ""
##        self.num = 0
##        self.remaining = 100000
##        self.indrawnum = 0
##        self.withdrawnum = 0
##    def inputaccount(self):
##        self.num = int(raw_input("Input your account number please:"))
##
##    def withdraw(self,withdrawnum):
##        if self.withdrawnum > self.remaining:
##            print "sorry, you don't have so much money"
##        else:
##            self.remaining = self.remaining - self.withdrawnum
##    def indraw(self,indrawnum):
##        self.remaining = self.remaining + indrawnum
##    def show(self):
##        print "your account number:",self.num
##        print "your remaining:",self.remaining
##
##class InterestAccount(BankAccount):
##    def __init__(self):
####        super(InterestAccount,self).__init__()
##        self.rate = 0.06
##        self.interest = 0
##        self.remaining = 100000
##        
##    def interest1(self,rate):
##        self.interest =  rate * self.remaining
####
####    def rate1(self):
####        self.interest()
####        print self.interest
##
##    def rate1(self,years):
##        for i in range(years):
##            print "No",i+1," year:"
##            rate = float(raw_input("What the interest rate of this year:"))
##            self.interest1(rate)
##            print self.interest
##            
##
##    def showinterest(self):
##        k = int(raw_input("How many years:"))
##        self.rate1(k)
##
##myaccount = InterestAccount()
##myaccount.inputaccount()
##myaccount.indraw(1000)
##myaccount.show()
##myaccount.showinterest()
####print myaccount.remaining
##myaccount.show()

##import my_module
##
##f = my_module.c_to_f(32)
##print f

##from my_module import c_to_f
##f = c_to_f(32)
##print f
##
##from time import sleep
##print 1
##sleep(2)
##print 2
##sleep(2)

##import random
##a = random.randint(1,100)
##print a

##from letter import *
##for i in range(6):
##    zletter(i)
##    hletter(i)
##    oletter(i)
##    uletter(i)
##    nletter(i)
##    aletter(i)
##    nletter(i)
##    print

##import random
##list = []
##for i in range(5):
##    j = random.randint(1,20)
##    list.append(j)
##print list

import random,time
##for i in range(10):
##    time.sleep(3)
##    print random.random()

##class Solution(object):
##    def twoSum(self,nums,target):
##        length = 0
##        list = [0,0]
##        length =len(nums)
##        for m in range(length-1):
##            for j in range(1,length-m,1):
##                if nums[m] + nums[m+j] == target:
##                    list[0] = m
##                    list[1] = m+j
##                    break          
##        return list
##
##d = Solution()
##e = d.twoSum([6,1,2],3)
##print e

##class Solution(object):
##    def isPalindrome(self, x):
##        """
##        :type x: int
##        :rtype: bool
##        """
##        list=[]
##        list1=[]
##        if x < 0:
##            return False
##        elif x == 0:
##            return True
##        else:
##            while x/10.0!=0:
##                list.append(x%10)
##                x=x/10
##            list1=list[:]
##            list1.sort(reverse = True)
##            print list
##            print list1
##            if list==list1:
##                return True
##            else:
##                return False
##
##
##a = Solution()
##d = a.isPalindrome(1121)
##print d

##class dog(object):
##    def __init__(self):
##        self.name = "gou"
##        self.size = "small"
##    def hsq(self):
##        Input_filename = "MA测试数据.xlsx"
##        Output_filename = "MA预测数据.xlsx"
##        ####################################################################
##        # 当手动输入时，仅需输入历史负荷数据到inputlist中，将自动给出未来负荷预测结果
##        a=1
##        b=1
##        self.c=a+b
##        
##mydog = dog()
##mydog.hsq()
##print mydog.a
##import pandas as pd
##inputlist = [68.36328311, 70.93213305, 64.37200147, 64.2676526, 63.414831, 63.80207824,
##                     57.80533949, 65.4501274, 66.83157485, 70.37311399, 63.22536061, 65.79053123, 68.67876519,
##                     64.11115141, 64.12082006, 68.0312243, 62.55539612, 68.38866748, 70.69765919, 70.99576139]
##n=5
##data = []
##for i in range(len(inputlist) + n):
##    if i < len(inputlist):
##        data.append([i, inputlist[i]])
##    else:
##        data.append([i, 0])
##data = pd.DataFrame(data)
##        # 输出形式除了图还有表格，数据表格将保存在Output_filename中
##test = data[-n:]
##train = data[:-n]
##print data
##print
##print test
##print
##print train
##print

##class Solution(object):
##    def divide(self,dividend,divisor):
##        self.dividend = dividend
##        self.divisor = divisor
##        if dividend == 0:
##            return 0
##        elif dividend == divisor:
##            return 1
##        elif dividend > 0:
##            if self.divisor > 0:
##                d = self.de(dividend,divisor)
##                return d[0]
##            else:
##                d = self.de(dividend,-divisor)
##                return -d[0]
##        else:
##            if self.divisor > 0:
##                d = self.de(-dividend,divisor)
##                return -d[0]
##            else:
##                d = self.de(-dividend,-divisor)
##                if d[1] != 1:
##                    return d[0]
##                else:
##                    return d[0]-1
##    def de(self,a,b):
##        self.a = a
##        self.b = b
##        i = 0
##        s = 0
##        for j in range(1000,0,-1):
##            while a - b*j >= 0:
##                a = a - b*j
##                i = i + 1*j
##            d = i
##            if a == 0:
##                s = 1
##        return [d,s]
##b = Solution()
##a = b.divide(2147483648,-1)
##print a

##class Solution(object):
####    def __init__(self,dividend=1,divisor=1):
####        pass
######        self.dividend = dividend
######        self.divisor = divisor
##    def divide(self,dividend,divisor):
####        self.dividend = dividend
####        self.divisor = divisor
##        if dividend == 0:
##            return 0
##        elif dividend == divisor:
##            return 1
##        elif dividend > 0:
##            if divisor > 0:
##                d = self.de(dividend,divisor)
##                return d[0]
##            else:
##                d = self.de(dividend,-divisor)
##                return -d[0]
##        else:
##            if divisor > 0:
##                d = self.de(-dividend,divisor)
##                return -d[0]
##            else:
##                d = self.de(-dividend,-divisor)
##                if d[1] != 1:
##                    return d[0]
##                else:
##                    return d[0]-1
##    def de(self,a,b):
##        self.a = a
##        self.b = b
##        i = 0
##        s = 0
##        for j in range(150000,0,-149999):
##            while a - b*j >= 0:
##                a = a - b*j
##                i = i + 1*j
##            d = i
##            if a == 0:
##                s = 1
##        return [d,s]
##b = Solution()
##a = b.divide(-214748,-12)
##print a

##class check(object):
##    def __init__(self,pa1=1,pa2=2):
##        pass
##        print 1
##        self.pa1 = pa1
##        self.pa2 = pa2
##    def output(self,pa1,pa2):
##        print self.pa1
##        print self.pa2
##        print pa1
##        print pa2
##    def an(self,p3):
##        print p3 - 1
##        self.output(p3,p3)
##
##print 1
##print __name__
##print __main__
##if __name__=="__main__":
##    print 2
####mmm = check()
####mmm.an(4)

##name = "dog is it "
##name.title()
##print name.title(),
##print 1
##print name.rstrip(),
##print 2

##class Mynumbers:
##    def __init__(self):
##        self.a = 1
####        return self
##    def __next__(self):
##        x = self.a
##        self.a += 1
##        return x
##
##myclass = Mynumbers()
####myclass = [1,2,3,4]
####myiter = iter(myclass)
##print myclass.__next__()
##print myclass.__next__()
##print myclass.__next__()
##print myclass.__next__()
##print myclass.__next__()

##class Dog(object):
##    def __init__(self):
##        self.i = 0
##    
##    def __iter__(self):
##        return self
##
####    def re(self):
####        while self.i < 20:
####            self.next() = self.i
####            self.i += 1
##    def next(self):
##        if self.i < 20:
####            print self.i
##            self.i += 1
##        else:
##            raise StopIteration
##        return self.i
##myDog = Dog()
##for i in myDog:
##    print i

            

##class Fib(object):
##    def __init__(self):
##        self.a, self.b = 0, 1 # 初始化两个计数器a，b
##
##    def __iter__(self):
##        return self # 实例本身就是迭代对象，故返回自己
##
##    def next(self):
##        self.a, self.b = self.b, self.a + self.b # 计算下一个值
##        print "a"
##        if self.a > 100000: # 退出循环的条件
##            print"b"
##            raise StopIteration();
##            print"c"
##        return self.a # 返回下一个值
##
##n = Fib()
##for i in n:
##    print i

##class Dog(object):
##    def __init__(self):
##        self.i = 0
##        self.k = 0
##    def __iter__(self):
##        return self
##
##    def re(self):
##        while self.i < 20:
##            self.k = self.next()
##            self.k = self.i
##            self.i += 1
##            return self.k
####    def next(self):
####        if self.i < 20:
######            print self.i
####            self.i += 1
####        else:
####            raise StopIteration
####        return self.i
##myDog = Dog()
##myDog.re()
##for i in myDog:
##    print i
##A = []
##for i in range(20):
##    it = iter(A)
##    m = it.next()
##    m = i
##    print m

##list1 = [1,2,3,4,5]
##a = iter(list1)
##while True:
##    try:
##        print a.next()
##    except StopIteration:
##        break
##
##list2 = [22,31,23,12,4]
##b = iter(list1)
##while True:
##    x = next(b,"a")
##    print x
##    if x == "a":
##        break
##

##with open("C:\Users\周楠\Desktop\shit\open_file.txt") as file_object:
##    n = file_object.readlines()
##    print n
##
##for line in n:
##    print line.strip()

##with open("C:\Users\周楠\Desktop\shit\open_file.txt") as obj:
##    n = obj.readlines()
##    k = ""
##    print n
##    for line in n:
##        print line
##        k = k + line.strip()
##print k
##print (len(k))

##with open("C:\Users\周楠\Desktop\shit\open_file.txt") as obj:
####    n = obj.read()
####    print n
##    j = obj.readlines()
##    print j
##    n = obj.readlines()
##
##    
##    s = ""    
##    for i in n:
##        s = s + i.strip()
##
##        
##    print s[:50]
##    print len(s)
##
##    if "824" in s:
##        print "y"
##    else:
##        print "n"

##class fileinput(object):
##    def __init__(self):
##        pass
##    def readfile(self,filename):
##        with open(filename) as obj:
##            n = obj.read()
##            print n
##        with open(filename) as obj:
##            for n in obj:
##                print n.strip()
##        with open(filename) as obj:
##            n = obj.readlines()
##        sss = ""
##        for i in n:
##            sss = sss + i.strip()
##        print sss
####        print type(sss)
##        if "friends" in sss:
##            ssss = sss.replace("friends","dogs")
##            print ssss
##            
##
##my = fileinput()
##my.readfile("learningpy.txt")
##        
##    
##a = "it is"
##b = a.replace("i","b")
##print a,b

##file_name = 'new_file.txt'
##with open(file_name,'w+') as file_create:
##    re = file_create.read()
##    print re
##with open(file_name,'r') as file_create:    
##    read = file_create.read()
##    print read


##filename = "new.txt"
##with open(filename,'w') as obj:
##    obj.write("Love"+"\n")
##    obj.write("You"+"\n")
##with open(filename,'r') as obj1:
##    print obj1.readlines()
##with open(filename,'r') as obj1:
##    print obj1.read()
##with open(filename,'r') as obj1:
##    for i in obj1.readlines():
##        print i.strip(),
##import easygui
##class newfile(object):
##    def __init__(self):
##        pass
##        self.filename = easygui.enterbox("PLZ enter your filename:")
##    def create(self):
##        pass
##
##        content = easygui.enterbox("PLZ enter your content:")
##        with open(self.filename,"w+") as obj:
##            obj.write(content+"\n")
##        with open(self.filename,"r") as obj:
##            t = obj.read()
##            print "your content is "+ t
##    def add(self):
##        pass
##        addcontent = easygui.enterbox("PLZ add your content:")
##        with open(self.filename,'a') as obj:
##            obj.write(addcontent)
##    def printout(self):
##        pass
##        with open(self.filename,'r') as obj:
##            print obj.read()
##
##
##A = newfile()
##A.create()
##A.add()
##A.printout()
##import easygui
##class greeting(object):
##    def __init__(self):
##        pass
##        self.filename = easygui.enterbox("which file to save your message?")
##    def clear(self):
##        with open(self.filename+".txt",'w') as obj:
##            obj.write("")
##    def inputname(self):
##        pass
##        name = easygui.enterbox("please enter your name")
##        print "Hello!" + name + ", welcome come to python world."
##        with open(self.filename+".txt",'a') as obj:
##            obj.write(name + "\n")
##
##ss = greeting()
##ss.clear()
##for i in range(3):
##    ss.inputname()

##import easygui
##class whylike(object):
##    def __init__(self):
##        pass
##        self.filename = easygui.enterbox("Input your filename:")
##        with open(self.filename+".txt",'w') as obj:
##            obj.write("")
####        self.A = []
##    def reason(self):
##        pass
##        reasons = easygui.enterbox("why do you like program?")
##        flag = self.check(reasons)
##        if flag:
##            with open(self.filename+".txt",'a') as obj:
##                obj.write(reasons + "\n")
##    def check(self,reasons):
##        with open(self.filename+".txt",'r') as obj: 
##            A = obj.readlines()
##            for i in A:
##                if i.strip() == reasons.strip():
##                    return False
##                    break
##                else:
##                    pass
##            return True
##
##myreason = whylike()
##i = 0
##while i <= 5:
##    myreason.reason()
##    i += 1

##try:
##    print 5/0
##
##except StopIteration:
##    print "No"
##except ZeroDivisionError:
##    print "something wrong"

##a , b = 1 , 2
##float(a)
##float(b)
##try:
##    answer = a / b
##except:
##    print "sth wrong"
##else:
##    print answer 

##name = "Alice,   in wonderland"
##b = name.split()
##print name,"\n",b

##'''10-6'''
##class add(object):
##    def __init__(self):
##        pass
##        self.i = 0
##    def inputnum(self):
##        while self.i <= 3:
##            try:
##                a = int(raw_input("PLZ input the first num:"))
##                b = int(raw_input("PLZ input the second num:"))
##            except ValueError:
##                print "what you typed in is not number, you have",3-self.i,"chances again"
##            else:
##                print a+b
##                break
##            self.i += 1
##
##aaaa = add()
##aaaa.inputnum()

##import easygui
##class twofiles(object):
##    def __init__(self):
##        pass
##    def create(self,j):
##        for i in range(j):
##            if i == 0:
##                with open("cats.txt","w") as obj:
##                    obj.write("")
##            else:
##                with open("dogs.txt","w") as obj:
##                    obj.write("")
##    def writein(self):
##        self.create(2)
##        for i in range(2):
##            for j in range(3):
##                if i == 0:
##                    with open("cats.txt","a") as obj:
##                         obj.write(easygui.enterbox("PLZ input cats' name")+"\n")
##                else:
##                    with open("dogs.txt","a") as obj:
##                         obj.write(easygui.enterbox("PLZ input dogs' name")+"\n")
##
##    def checkin(self,name1,name2):
##        try:
##            with open(name1+".txt","r") as obj1:
##                print obj1.readlines()   
##            with open(name2+".txt","r") as obj2:
##                print obj2.readlines()
##        except IOError:
####            print "Sorry, the files cannot be found"
##            pass
##    def checkname(self):
##        name1 = raw_input("cats' file name:")
##        name2 = raw_input("dogs' file name:")
##        self.checkin(name1,name2)
##    def whole(self):
##        self.writein()
##        self.checkname()
##test = twofiles()
##test.whole()

##import json
##number = [1,3,5,7,9]
##filename = "number.json"
##with open(filename,"w") as obj:
##    json.dump(number,obj)
##    print "a"
##with open(filename,"r") as obj:
##    numb = json.load(obj)
##print numb

##import json
##class num(object):
##    def __init__(self):
##        pass
##        self.filename = raw_input("Enter your filename please:")
##    def inp(self):
##        pass
##        a = raw_input("What is you favourite number:")
##        with open(self.filename+".json","w") as obj:
##            json.dump(a,obj)
##    def outp(self):
##        pass
##        with open(self.filename+".json","r") as obj1:
##            b = json.load(obj1)
##            print "I know your favourite number is",b
##test = num()
##test.inp()
##test.outp()

##import json
##class num(object):
##    def __init__(self):
##        self.filename = raw_input("Enter your filename please:")
##    def inp(self,filename):
##        a = raw_input("What is you favourite number:")
##        with open(self.filename+".json","w") as obj:
##            json.dump(a,obj)
##    def outp(self,filename):
##        with open(filename+".json","r") as obj1:
##            b = json.load(obj1)
##            print "I know your favourite number is",b
##    def aa(self):
##        try:
##            self.outp(self.filename)
##        except IOError:
##            print "The file cannot be found."
##            self.inp(self.filename)
##            self.outp(self.filename)
##test = num()
##test.aa()

##import pygame
##import random
##import time
##pygame.init()
##screen = pygame.display.set_mode([640,480])
##screen.fill([255,255,255])
##for i in range(10000):
##    time.sleep(0.00001)
##    left = random.randint(1,320)
##    top = random.randint(1,240)
##    right = random.randint(1,320)
##    bottom = random.randint(1,240)
##    pygame.draw.rect(screen,[random.randint(1,255),random.randint(1,255),random.randint(1,255)],\
##                     [left,top,right,bottom],random.randint(0,1))
##    pygame.display.flip()
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##pygame.quit()

####画sin曲线
##import random,sys,math,pygame
##pygame.init()
##screen = pygame.display.set_mode([640,320])
##circle = 2
##A = []
##screen.fill([255,255,255])
##for i in range(640):
##    y = 160-int(160*math.sin(float(i+1)/640*circle*2*math.pi))
##    A.append([i,y])
##for i in range(639):
##    pygame.draw.lines(screen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)],False,[A[i],A[i+1]],2)
###    time.sleep(0.01)
##    pygame.display.flip()
##
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##pygame.quit()
    
##import pygame
##dots = [[221, 432], [225, 331], [133, 342], [141, 310],\
##[51, 230], [74, 217], [58, 153], [114, 164],\
##[123, 135], [176, 190], [159, 77], [193, 93],\
##[230, 28], [267, 93], [301, 77], [284, 190],\
##[327, 135], [336, 164], [402, 153], [386, 217],\
##[409, 230], [319, 310], [327, 342], [233, 331],\
##[237, 432]]
##pygame.init()
##screen = pygame.display.set_mode([640,480])
##screen.fill([255,255,255])
##pygame.draw.lines(screen,[0,0,0],True,dots,1)
##pygame.display.flip()
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT():
##            running = False
##pygame.quit()

##import pygame,time
##dots = [[221, 432], [225, 331], [133, 342], [141, 310],\
##[51, 230], [74, 217], [58, 153], [114, 164],\
##[123, 135], [176, 190], [159, 77], [193, 93],\
##[230, 28], [267, 93], [301, 77], [284, 190],\
##[327, 135], [336, 164], [402, 153], [386, 217],\
##[409, 230], [319, 310], [327, 342], [233, 331],\
##[237, 432]]
##dots.append(dots[0])
##print dots
##pygame.init()
##screen = pygame.display.set_mode([640,480])
##screen.fill([255,255,255])
##for i in range(len(dots)-1):
##    pygame.draw.lines(screen,[0,0,0],True,[dots[i],dots[i+1]],1)
##    pygame.display.flip()
##    time.sleep(0.1)
##running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##pygame.quit()

import sys,pygame,time
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
picture = pygame.image.load("beach_ball.png")
for i in range(100):
    screen.blit(picture,[320,40+i])
    pygame.display.flip()
    screen.blit(picture,[320,40+i])
    pygame.display.flip()
    screen.blit(picture,[320,40+i])
    pygame.display.flip()
    screen.blit(picture,[320,40+i])
    pygame.display.flip()
    time.sleep(0.001)
    pygame.draw.rect(screen,[255,255,255], [320, 40+i, 90, 90], 0)
    time.sleep(0.001)
    pygame.display.flip()
    screen.blit(picture,[320,40+i+1])
    pygame.display.flip()
    screen.blit(picture,[320,40+i+1])
    pygame.display.flip()
    screen.blit(picture,[320,40+i+1])
    pygame.display.flip()
    screen.blit(picture,[320,40+i+1])
    pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


##import pygame, sys
##pygame.init()
##screen = pygame.display.set_mode([640,480])
##screen.fill([255, 255, 255])
##my_ball = pygame.image.load('beach_ball.png')
##x = 640
##y = 50
##screen.blit(my_ball,[x, y])
##pygame.display.flip()
##for looper in range (1, 200):
##    pygame.time.delay(20)
##    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)
##    x = x + 5
##    screen.blit(my_ball, [x, y])
##    pygame.display.flip()
##    running = True
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##pygame.quit()
