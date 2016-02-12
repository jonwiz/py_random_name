import random

consonants = 'bcdfghjklmnpqrst'
vowels = 'aeiou'
names = []
dupes = []

tries = 1
max_tries = 1000000



def randomFullName(gender):
    firstname = randomNames(gender=gender, nameCount=1, charLen=3)
    middlename = randomNames(gender=gender, nameCount=1, charLen='random')
    lastname = randomNames(gender=gender, nameCount=1, charLen=7)

    return "{} {} {}".format(firstname[0], middlename[0], lastname[0])


def randomNameList(args, gender = 'm'):
    names = []
    for i in range(1,int(args['nameCount']) + 1):
        x = random.choice(consonants)
        y = random.choice(consonants)
 
        z = random.choice(consonants)
        v = random.choice(vowels)
        
        #don't start name with x
        while(x == 'x'):
            x = random.choice(consonants)
        
        if(x == 'q'):
            v = 'u'
            y = random.choice(vowels)
            while(y == 'u'):
                y = random.choice(vowels)
                
        if(x in ['f','p']):
            v = 'r'
            y = random.choice(vowels)
            
        four = random.choice(vowels)
        if(y in vowels):
            four = random.choice(consonants)
            z = random.choice(vowels)
            
        if(four in vowels):
            if(gender == 'm'):
                z = 'n'
            else:
                z = 's'
        
        n3 = x + v + y
        n4 = x + v + y + four
        n5 = x + v + y + four + z
        
        
        six_suffix = {'m': ['ra','on','da'], 'f': ['ri','si','la']}
        n6 = n4 + random.choice(six_suffix[gender])
        
        s1 = random.choice(vowels)
        s2 = random.choice(consonants)
        
        #don't allow j ending
        while(s2 in ['j','q', 'h']):
            s2 = random.choice(consonants)
            
            
        if(gender == 'f'):
            s1 = 'e'
            s2 = 'r'
            
        if(z in vowels):
            s1 = random.choice(consonants)
            s2 = random.choice(vowels)
            if(gender == 'f'):
                s1 = 'l'
                s2 = 'a'
            
        seven = s1 + s2
        
        n7 = n5 + seven
        
        namesizes = [None,None,None,n3, n4, n5, n6, n7]
        if(args['charLen'] == 'random'):
            
            idx = random.randint(3,7)
            
        else:
            idx = args['charLen']
        
        
        
        name = namesizes[idx].capitalize()
        names.append(name)
    
    return names

def randomNames(needle=None, gender='m', **args):
    tries = 1
    if((args['charLen'] != 'random') and (args['charLen'] < 3 or args['charLen'] > 7)):
        print("Name length must be between 3 and 7")
        return []
#     consonants = 'bcdfghjklmnpqrstvwxyz'
    
    names = randomNameList(args, gender=gender)
    if(needle is not None):
        for t in range(1, max_tries):
            if(needle not in names):
                names = randomNameList(args, gender=gender)
                tries = tries + 1
            else:
                break
    
        print('{} Tries to generate Needle {}!'.format(tries, needle))
        if(tries >= max_tries):
            print("Reached maximum attempts to generate {}".format(needle))

 
    return list(set(names))