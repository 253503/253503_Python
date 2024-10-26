def remove_vowels(txt):
    for i in 'AEIOUaeiou':
        txt=txt.replace(i,"")
    return txt
print(remove_vowels("dgfedhfweai"))