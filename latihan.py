# -----------Buat sebuah list sebanyak 5 elemen dengan nilai bebas--------------
print("Buat sebuah list sebanyak 5 elemen dengan nilai bebas")
listA = [1, 2, 3, 4, 5]
print(listA)
print()

print("* akses list: *")
print ("tampilkan element ke 3 = ", listA[2])
print ("ambil nilai elemen ke 2 sampai elemen ke 4 =",listA[1:4])
print ("ambil elemen terakhir = ",listA[-1])
print()

print("* ubah element list: *")
listA[3] = True
print ("ubah elemen ke 4 dengan nilai lainnya = ", listA )
listA[3:] = [6, 7]
print ("ubah elemen ke 4 sampai dengan elemen terakhir = ", listA )
print()

print("* tambah elemen list: *")
listB=[]
listB.extend(listA[0:2])
print ("ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B) = ", listB )
listB.extend(["tiga"])
print ("tambah list B dengan nilai string = ", listB )
listB.extend([4,5,6])
print ("tambah list B dengan 3 nilai = ", listB )
c=listA+listB
print ("gabungkan list B dengan list A ", c )

