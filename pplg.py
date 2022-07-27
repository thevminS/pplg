import os

# Date Sorting
def dateSort(list,start,end):
        
     if start == 0:
        listn=[]
        for x in list:
            listn.append(x[:end])
        return listn 
     else:     
        listn=[]
        for x in list:
            listn.append(x[start:end])
        return listn 

# Combinations
def comb(list1,list2,list3=""):
    comb=[]
    if list3 == "" :
        for x in list1:
            for y in list2:
                comb.append(x+y)
                comb.append(y+x)
    else :
        for x in list1:
            for y in list2:
                for z in list3:
                    comb.append(x+y+z)
                    comb.append(x+z+y)
                    comb.append(y+z+x)
                    comb.append(y+x+z)
                    comb.append(z+x+y)
                    comb.append(z+y+x)
    return comb
    
def print_to_file(filename, unique_list):
     f = open(filename, "w")
     unique_list.sort()
     f.write(os.linesep.join(unique_list))
     f.close()
     f = open(filename, "r")
     lines = 0
     for line in f:
          lines += 1
     f.close()
     print("\n")
     print(
          "[+] Saving dictionary to "
          + filename
          + ", counting "
          + str(lines)
          + " words."
     )
     print("\n")
     ex = input(print("> Type q to quit the program or press Enter to continue:")).lower()
     if (ex == "exit") :
       print("[+] Quitting...")
       quit()
     main()

def interactive():
 #Inputs
    profile = {}

    #owner
    name = input("> First Name: ").lower()
    profile["name"] = str(name)
    profile["surname"] = input("> Surname: ").lower()
    profile["nick"] = input("> Nickname: ").lower()
    birthdate = input("> Birthdate (DDMMYYYY): ") 
    profile["birthdate"] = str(birthdate)
    print("\r\n")

    #wife
    profile["wife"] = input("> Partners name: ").lower()
    profile["wifen"] = input("> Partners nickname: ").lower()
    wifeb = input("> Partners birthdate (DDMMYYYY): ")
    profile["wifeb"] = str(wifeb)
    print("\r\n")

    #kid
    profile["kid"] = input("> Child's name: ").lower()
    profile["kidn"] = input("> Child's nickname: ").lower()
    kidb = input("> Child's birthdate (DDMMYYYY): ")
    profile["kidb"] = str(kidb)
    print("\r\n")

    #pet
    profile["pet"] = input("> Pet's name: ").lower()

    #company
    profile["company"] = input("> Company name: ").lower()
    print("\r\n")

    #words
    profile["words"] = [""]
    words1 = input(
        "> Do you want to add some key words about the victim? Y/[N]: "
    ).lower()
    words2 = ""
    if words1 == "y":
        words2 = input(
            "> Please enter the words, separated by comma. [i.e. hacker,juice,black]: "
        )
    profile["words"] = words2.split(",")

    #chars    
    profile["chars"] = [""]
    char1 = input(
        "> Do you want to add some characters victim might use? Y/[N]: "
    ).lower()
    char2 = ""
    if char1 == "y":
        char2 = input(
            "> Please enter the words, separated by spaces. [i.e. @ # $ ,]: "
        )
    profile["chars"] = char2.split(" ")

    #dates    
    profile["dates"] = [""]
    date1 = input(
        "> Do you want to add some important dates about the victim? Y/[N]: "
    )
    date2 = ""
    if date1 == "y":
        date2 = input(
            "> Please enter the dates, separated by comma (DDMMYYYY). [i.e. 01042002,23122000,23112000]: "
        )
    profile["dates"] = date2.split(",")

    #mobile number    
    profile["teleNo"] = [""]
    tele1 = input(
        "> Do you want to add some telephone numbers of the victim? Y/[N]: "
    )
    tele2 = ""
    if tele1 == "y":
        tele2 = input(
            "> Please enter the telephone numbers, separated by comma. [i.e. 0761234567,0721234567]: "
        )
    profile["teleNo"] = tele2.split(",")

    generate_wordlist_from_profile(profile)  # generate the wordlist

def generate_wordlist_from_profile(profile):
    
    # Telephone numbers
    telenum = profile["teleNo"]

    # Reverse Telephone number
    telerev=[]
    for x in telenum :
        telerev.append(x[::-1])

    telenum = telenum + telerev

    # Creating date list
    dates=[profile["birthdate"]]+[profile["wifeb"]]+[profile["kidb"]]+profile["dates"]
    dates=[value for value in dates if value != '']

    date_yyyy = list(set(dateSort(dates,4,8)))
    date_yy = list(set(dateSort(dates,6,8)))
    date_dd = list(set(dateSort(dates,0,2)))
    date_mm = list(set(dateSort(dates,2,4)))

    totdates = dates + date_yyyy + date_yy + date_dd + date_mm

    # Name list
    name_list=[profile["name"],profile["surname"],profile["nick"],profile["wife"],profile["wifen"],profile["kid"],profile["kidn"],profile["pet"],profile["company"]]
    name_list=[value for value in name_list if value != '']


    # Convert first letters to uppercase
    nameup=[]
    for x in name_list :
        nameup.append(x.title())

    names= name_list + nameup 

    # Reverse name
    reverse=[]
    for x in names :
        reverse.append(x[::-1])

    names = names + reverse
    names = list(set(names))

    # Creating word list by names 
    nlist=[]
    for x in names:
        for y in names:
            if names.index(x) != names.index(y) :
                nlist.append(x + y)
                for z in names:
                    if (names.index(x) != names.index(z) and names.index(y) != names.index(z) and names.index(x) != names.index(y)):
                        nlist.append(x + y + z)

    # Creating word list by names and dates
    ndlist = comb(names,totdates)

    # Creating word list by names, dates and characters
    char = profile["chars"]
    ncdlist = comb(names,totdates,char)

    # Creating word list by additional words
    
    wordup = []
    for x in profile["words"] :
        wordup.append(x.title())

    words = profile["words"] + wordup

    # Reverse words
    wordrev=[]
    for x in words :
        reverse.append(x[::-1])
    
    words = profile["words"] + wordup + wordrev

    wdclist = comb(words,totdates,char)

    wdlist = comb(words,totdates)

    nwclist = comb(names,words,char)       

    nwlist = comb(names,words)       

    nwtlist  = comb(names,words,totdates)       

    unique_list = totdates + names + words + ndlist + ncdlist + wdclist + wdlist + nwclist + nwlist + nwtlist + telenum
    unique_list = list(set(unique_list))

    print_to_file(profile["name"] + ".txt", unique_list)


def main():
     print("**       Command-line interface to the ppl-generator      **")
     print("*                          __                              *")
     print("*                         |  |                             *")
     print("*                         |  |                             *")
     print("*                         |  |                             *")
     print("*                    __ __|  |__ __                        *")
     print("*                   |  |  |  |  |  |                       *")
     print("*                   |  |  |  |  |  |                       *")
     print("*                   \              /                       *")
     print("*                    \            /                        *")
     print("*                     \          /                         *")
     print("*                      ----------                          *")
     print("\n")
     print("**PRESS ENTER TO SKIP INFORMATIONS**")
     print("\n")
     interactive()

if __name__ == '__main__' :
    main()









    
    










