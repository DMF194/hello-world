#madlibs game
#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscrie to __"
##youtuber ="Fong"#string variable 

#a few ways to do this
##print("subscribe to "+ youtuber)
##print("subscribe to {}".format(youtuber))
##print(f"subscribe to {youtuber}")

adj=input("Adjective is :")
verb1=input("Verb is : ")

madlib=f"Computer programing is so {adj}! It makes me excited\
    I love to {verb1}"

print(madlib)