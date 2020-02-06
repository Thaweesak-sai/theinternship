
def main():
    hangmanRaw = input("")
    hangman = hangmanRaw.split(" ")
    result = ['_']*12
    wrong = list()
    pos = list()
    score =0
    print(*result, sep=" ")
    for i in range(5):
        ans = input("")
        for j in range(len(hangman)):
            if hangman[j]==ans:
                pos.append(j)
        if pos!=[]:
            for k in range(len(pos)):
                result[pos[k]]=ans
                score+=1
        else:
            wrong.append(ans)
        print(*result,*wrong)
        pos.clear()
    print(score)
if __name__ == '__main__':
    main()