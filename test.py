import random as r

if __name__ == '__main__':
    #x = "ECE_180_DA_DB"
    #if x == "ECE_180_DA_DB":
    #    print("You are living in 2017")
    #else:
    #    # this is a comment
    #    x = x + " - Best class ever"
    #    print(x)
    val = int(input("Enter the number of random letters to generate: "))
    out = ""
    for i in range(val):
        out = out + chr(r.randrange(97,122))

    print("The new word we've created for you is: " + out)
    print("Use it in a sentence to impress all of your friends!")
    
