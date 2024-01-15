#TRHODAW128F42756F1-TRHXPXI128F934F6F1
ordet = "TRHODAW128F42756F1"

listan = []
with open("unique_tracks.txt", "r", encoding="utf-8") as file:
    for row in file:
        listan.append(row)


kl = max(listan, key=len)
print(len(kl), "as")

h = ''
for elem in ordet:
    val = ord(elem)
    h = h + str(val)

print(h)
print(int(h)% 100000)

b = ''
ordet2 = "TRXPXI128F934F6F1"
for elem in ordet2:
    val = ord(elem)
    b = b + str(val)
print(b)
print(int(b)% 100000)

hashletterlist = list()
for letter in ordet2:
    hashletter = str(ord(letter))
    hashletterlist.append(hashletter)
pre_hashad = "".join(hashletterlist)
hashad = int(pre_hashad) % 100000
print(pre_hashad,"nyhash")
print(hashad, "nyhash")



"""key: key
calculates hashfunktion for key"""



"""
def hashcount(listan,n):
    hashdic = {}
    coldic = {}
    count = 0
    for row in listan:
        keyvalue = hashfunction(row,n)
        if keyvalue in hashdic:
            count += 1
            existing = coldic.get(keyvalue)
            if existing is None:
                existing = ""
            coldic[keyvalue] = existing + "-" + row
        else:
            hashdic[keyvalue] = row
    print(coldic)
    return count"""


"""def my_hash_function(line, length):
    hashletterlist = list()
    for letter in line:
        hashletter = str(ord(letter))
        hashletterlist.append(hashletter)
    pre_hashad = "".join(hashletterlist)
    hashad = int(pre_hashad) % length
    return pre_hashad, hashad"""


"""def my_hash_function(key,n):
    return int(''.join(map(lambda x: str(ord(x)), key))) % n
    # Detta kommer alltid att vara mindre än size"""
