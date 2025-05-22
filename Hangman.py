# Hangman

# Guess
def game(w) :
    word = [x.upper() for x in w]
    found = ["_" for x in w]
    wasted = []
    left = 7
    print("Let's play.")
    while True :
        guess = (input("You have %d live(s) remaining, guess a letter : %s \n" % (left," ".join(found))))
        if guess.isalpha() :
            guess = guess.upper()
            if guess in word and guess not in found :
                for i in range(0,len(word)) :
                    if word[i] == guess:
                        found[i] = guess
                print("%s is in the word." % (guess))
                if word == found :
                    print("Congratulations!")
                    break
            elif guess in word and guess in found or guess in wasted :
                print("%s already guessed." % (guess))
            else :
                left -= 1
                wasted.append(guess)
                print("%s is not in the word." % (guess))
                if left == 0 :
                    print("You lost, the word was %s" %("".join(word)))
                    break
        else :
            guess = input("Type a letter. \n")


if __name__ == "__main__" :
    game("Thomas")