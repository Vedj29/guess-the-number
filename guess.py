secret_no=256
while True:
    n=int(input("Guess the no."))
    if n < secret_no:
        print("too low")
    elif n > secret_no:
        print("too high")
    else:
        print("correct guess")
        break
        
