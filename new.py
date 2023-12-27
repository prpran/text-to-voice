import pyttsx3

n = input("enter a number:")

#9
#one nines are nine
dict = {
    "1" : "ones",
    "2" : "twos",
    "3" : "threes",
    "4" : "fours",
    "5" : "fives",
    "6" : "sixes",
    "7" : "sevens",
    "8" : "eights",
    "9" : "nines",
    "10" : "tens"
}

txt=""
for i in range(1,11):
    mul =  i*int(n)
    txt+= str(i) + " " +dict[n] + "are" + str(mul) + "\n"


engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()


