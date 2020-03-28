def anagram_check(str1, str2):
    if len(str1)!=len(str2):
        print("Not anagram1")
    count={}
    for i in str1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

    for i in str2:
        if i in count:
            count[i]-=1

    print(count)
    for i in count:
        if count[i]!=0:
            return ("not anagram")
    return ("anagram")
            

print(anagram_check("hello","helol"))
