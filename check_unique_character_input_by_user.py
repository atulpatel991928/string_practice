def is_unique(str):
    if len(str)>256:
        return False
    else:
        dict={}


        for s in str:
            if (s in dict.key())==False:
                dict[s]="True"
            else:
                return False
        return True

str=input("enter string:")
print(is_unique(str))