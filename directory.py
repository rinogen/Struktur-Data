#soal kertas no 2
mhs = {"nama"  : "Arief Zuhri" , 
       "prodi" : "D4 Teknologi Rekayasa Perangkat Lunak",
       "alamat": {"desa"      : "Sinduharjo",
                 "kecamatan"  : "Ngaglik",
                 "kabupaten" : "Sleman",
                 "provinsi"  : "DIY"
                 }
       }
       
print ("ALAMAT =" + "\n",
       mhs["alamat"]["desa"]+"\n" ,
       mhs["alamat"]["kecamatan"]+"\n",
       mhs["alamat"]["kabupaten"]+"\n",
       mhs["alamat"]["provinsi"]+ "\n" )
print()
print()
print()



#soal kertas no 3
penilaian = {"materi 1" : 80,
             "materi 2" : 87,
             "materi 3" : [66 , 75 , 65],
             "materi 4" : {"diskusi" : 90,
                           "kuis"    : 70
                           }
             } 


import statistics

def hitungnilai(penilaian) :
    nm_1 = 0.2 * penilaian["materi 1"]
    nm_2 = 0.2 * penilaian["materi 2"] 
    nm_3 = 0.3 * statistics.mean(penilaian["materi 3"])
    nm_4 = 0.3 * (penilaian["materi 4"]["diskusi"] + penilaian ["materi 4"]["kuis"]) / len(penilaian["materi 4"])
    
    return nm_1 + nm_2 + nm_3 + nm_4

print("skor" , hitungnilai(penilaian))
print()
print()
print()

#soal papan 

datamhs= {"nama"  : "adi",
          "umur"  : 20,
          "mk"    : {
                      "matematika diskrit"  : ["A" , 2],
                      "pemrograman"         : ["B" , 3],
                      "struktur data"       : ["B" , 2]
                    }
          }
mk_ambil =[]
for mk in datamhs["mk"].keys():
    mk_ambil.append(mk)
print ("Mata Kuliah yang diambil =", ",".join(mk_ambil))

IPK = (datamhs["mk"]["matematika diskrit"][1]*4 + datamhs["mk"]["pemrograman"][1]*3 + datamhs["mk"]["struktur data"][1]*3) / (datamhs["mk"]["matematika diskrit"][1] + datamhs["mk"]["pemrograman"][1] + datamhs["mk"]["struktur data"][1])
    

print ("Mata Kuliah yang diambil =",  datamhs["mk"])
print ("IPK =" , IPK )


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    