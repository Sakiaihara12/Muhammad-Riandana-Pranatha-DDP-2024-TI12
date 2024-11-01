# Tugas 2 Menghitung Luas menggunakan match case 
hitung_luas = int(input("""Pilih Salah Satu:
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran
3. Hitung Luas Segitiga
"""))

match hitungan_luas:
  case 1:
    print("Menghitung Luas Persegi")
    sisi = int(input("Masukkan Nilai Sisi: "))
    hitung_luas_persegi = sisi **2
    print (f"Jadi Luas Persegi Dengan Sisi {sisi} CM Adalah {hitung_luas_persegi} ²")
  case 2:
    print("Menghitung Luas Lingkaran")
    jari_jari = int(input("Masukkan Jari Jari Awal: "))
    phi = 22/7
    hitung_luas_lingkaran = phi * (jari_jari ** 2)
    print (f"Jadi Luas Lingkaran Dengan Jari Jari {jari_jari} CM Adalah {hitung_luas_lingkaran} ²")
  case 3:
    print("Menghitung Luas Segitiga")
    alas = int(input("Masukkan Nilai Alas: "))
    tinggi = int(input("Masukkan Nilai Tinggi: "))
    hitung_luas_segitiga = 1/2 * alas * tinggi
    print(f"Jadi Luas Segitiga Alas {alas} CM Dan Tinggi {tinggi} CM Adalah {hitung_luas_segitiga} ² ")
  case _:
    print("Pilihan Tidak Valid")