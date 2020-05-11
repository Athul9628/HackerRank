def compareStrings(s1, s2, s3):
    a = []
    a.append(s1)
    a.append(s2)
    a.append(s3)
    a.sort()
    c = "".join(map(str, a))
    print(a)
    return c


first_String = input()

second_String = input()

third_String = input()
result = compareStrings(first_String, second_String, third_String)
print(result)
