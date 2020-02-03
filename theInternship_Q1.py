def acronym(buffer):
    acronym =""
    for word in buffer.split():
        if(word[0].isupper()==True):
            acronym=acronym+word[0]
    return acronym

def main(): 
    loop = int(input(""),10)
    ans = list()
    for i in range(loop):
        buffer = input("")
        ans.append(acronym(buffer))
        ans.sort()
        ans.sort(key=len, reverse=True)
    print(*ans,sep="\n")
if __name__ == '__main__':
    main()