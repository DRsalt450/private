print ("jaké má příjmení obama?")
print("a: obama")
print("b: to nikdo neví")
print("c: habibi")
answer= input("choose:")

body = 0

if answer == "a":
    body += 1
    print("very nice!")
    print("you now have",body)
else:
    print("nuh uh")
    print("you now have",body)

print("coughing baby vs hydrogen bomb, who wins?")
print("a: coughing baby")
print("b: hydrogen bomb")
print("c: a tie")
answer_2=input("choose:")

if answer_2 == "b":
    body += 1
    print("very nice!")
    print("you now have",body)

else:
    print("nuh uh")
    print("you now have",body)

if body < 2:
    print("u got:",body)
    print("u suck")

else:
    print("u got",body)
    print("i hope you did this on 1. try")
