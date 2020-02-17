# parctice with list in phyton and falsh back in first alpro 1

colors = ["red", "green" , "blue" , "yellow" ]

for i in range (len(colors)) :
    print (colors[i])
print()


for i in range (len(colors) -1 , -1 , -1): # --> (panjangnya , sampai ke berapa , mundurnya berapa) #
    print (colors[i])
print ()
print ()
print ()


# use reverse
for i in reversed(colors) :
    print (i)
print()
print ()
print ()

# ascending with the first alphabeth place on the top
for i in reversed(sorted(colors)) :
    print (i)
print ()
print ()
print ()
# descending number in list --> (panjangnya , sampai ke berapa , mundurnya berapa)
for i in range (5,-1,-1) :
    print (i)
print ()
print ()
print ()

#make another print with "kutip"
for i in range (len(colors)) :
    print (i ,"-->" , colors [i] )
print ()
print ()
print ()

for i in range (len(colors)) :
    print (i ,"-->" , '"' + colors [i] +'"' )
print ()
print ()
print ()

for i in range (len(colors)) :
    print (i ,"-->" , "\"" + colors [i] +"\"" )
print ()
print ()
print ()

#combine two lis in one print  ---> use zip 
name = ["a" , "b" , "c"]

for nama,warna in zip (name, colors) :
    print (nama , "SUKA" , warna)
print ()
print ()
print ()

lebihpendek = min(len(name) , len(colors))
for i in range (lebihpendek) :
    print (name[i] , "SUKA" , colors[i])

print ()
print ()
print ()

# Tuple is the other way of list that cannot be chnage like add with append etc
hari = ("SENIN" , "SELASA" , "RABU" , "KAMIS" , "JUMAT" , "SABTU" , "MINGGU")

for day in hari:
    print (day)
print ()
print ()
print ()

