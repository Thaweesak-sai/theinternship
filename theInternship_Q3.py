"""
Digit Hangman, The Internship Program 2020 third question
Created By Thaweesak Saiwongse (Note) 06/02/2020
"""
def main():
    hangmanRaw = input("")
    hangman = hangmanRaw.split(" ")
    result = ['_']*12 #list of result
    wrong = list() #list for collecting wrong guess
    pos = list() # list of correct guess indexes
    score =0
    print(*result, sep=" ")
    for i in range(5):
        ans = input("")
        for j in range(len(hangman)): 
            if hangman[j]==ans: #guess answer is correct
                pos.append(j) #add the index to the list
        if pos!=[]: #if the guess is wrong
            for k in range(len(pos)):
                result[pos[k]]=ans #add correct guess to show in result
                score+=1 #update score
        else:
            wrong.append(ans) #add incorrect guess to wrong list
        print(*result,*wrong)
        pos.clear()
    print(score)
if __name__ == '__main__':
    main()