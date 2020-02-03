"""
Sorting Acronyms, The Internship Program 2020 first question
Created By Thaweesak Saiwongse (Note) 03/02/2020
"""

def acronym(buffer):
    """ acronym function. to look for the first character of each word in string
    Args:
        buffer (string) input from user

    Returns:
        acronym for each line of input
    """
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
        ans.sort()                              #alphabetically sort
        ans.sort(key=len, reverse=True)         #sort by length
    print(*ans,sep="\n")
if __name__ == '__main__':
    main()