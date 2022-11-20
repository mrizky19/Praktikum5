# import package tabulate
from tabulate import tabulate

# membuat list kosong untuk menampung data
dataMahasiswa = []
no = 0

# melakukan perulangan input sesuai keinginan sampai pertanyaan tambah data dimunculkan kembali
while(True):
# membuat variable untuk menampung inputan
    no += 1
    nama = input("Masukan Nama : ")
    nim = input("Masukan NIM : ")
    tugas = float(input("Masukan Nilai Tugas : "))
    uts = float(input("Masukan Nilai UTS : "))
    uas = float(input("Masukan Nilai UAS : "))
    
# menjumlahkan nilai dari tugas,uts dan uas
    nilaiAkhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)

# menambahkan data input ke list dataMahasiswa
    dataMahasiswa.append(
        [no, nama, nim, tugas, uts, uas, nilaiAkhir])

# input tambah data jika tekan y maka input kembali, selain itu berhenti dan tampilkan data
    tambahData = input("Tambah Data? (y/t) : ")
    if(tambahData == "t"):
        break

# tampilkan dataMahasiswa menggunakan tabulate package agar tampilan berbentuk table

print(tabulate(dataMahasiswa, headers=[
      "No", "Nama", "Nim", "Tugas", "UTS", "UAS", "Nilai Akhir"], tablefmt="fancy_grid"))