
def main():
    hangmanRaw = input("")
    hangman = hangmanRaw.split(" ")
    result = ['_']*12
    print(*result, sep=" ")
    # print(hangman)
    # print(hangman[0], hangman[2])
    for i in range(5):
        ans = input("")
if __name__ == '__main__':
    main()