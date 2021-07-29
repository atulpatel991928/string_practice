def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if (str[i] == str[j]):
                return False;
    return True;
str = "Guthjdnn";

if (uniqueCharacters(str)):
    print("True", str);
else:
    print("False", str);

