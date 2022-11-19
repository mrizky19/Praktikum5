from prettytable import PrettyTable
stop = False

item = []
while (not stop):
    nama = input("Masukan Nama : ")
    nim = input("NIM : ")
    tugas = input("Nilai Tugas : ")
    uts = input("Nilai UTS : ")
    uas = input("Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    item.append([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah Data? Y/N : ")
    if (tanya == "n"):
        stop = True
    
print("===================================================================")

x = PrettyTable()
no = 0

for isi in item:
    no += 1
    x.field_names = ["No", "Nama", "Nim", "Tugas", "UTS", "UAS", "Nilai Akhir"]
    x.add_row([no, isi[0], isi[1], isi[2], isi[3], isi[4], isi[5]])
print(x)

