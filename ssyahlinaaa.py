# Tulis kode di sini..
tugas = int(input("Masukkan nilai tugas: "))  
# input nilai tugas
uts = int(input("Masukkan nilai UTS: "))      
# input nilai uts
uas = int(input("Masukkan nilai UAS: ")) 
# input nilai uas

nilai_akhir = (tugas * 0.4) + (uts * 0.3) + (uas * 0.3)
# menghitung nilai akhir  

print("Nilai akhir:", nilai_akhir)     
# menampilkan nilai akhir
print("Tipe data:", type(nilai_akhir))
# menampilkan tipe data