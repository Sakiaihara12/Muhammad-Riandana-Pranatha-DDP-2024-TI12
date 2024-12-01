from hitung import *
def hitungan_aritmatika():
    print('Pilih operasi aritmatika yang ingin dilakukan:')
    print('1.Penambahan')
    print('2.Pengurangan')
    print('3.Perkalian')
    print('4.Pembagian')
    print('5.Pangkat')
    pilihan = int(input('Masukkan nomor operasi aritmatika yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', tambah(a,b))
    elif pilihan == 2:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', kurang(a,b))
    elif pilihan == 3:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', kali(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', bagi(a,b))
    elif pilihan == 5:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', pangkat(a,b))
    else:
        print('pilihan tidak valid')

from bangun_datar import *
def Hitungan_Bangun_Datar():
    print('Pilih operasi aritmatika yang ingin dilakukan:')
    print('1.Persegi')
    print('2.Persegi Panjang')
    print('3.Segitiga')
    print('4.Lingkaran')
    print('5.Trapesium')
    pilihan = int(input('Masukkan nomor operasi Bangun Datar yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan Nilai Sisi Awal: '))
        print("Hasil Luas nya adalah: ", persegi(a))
    elif pilihan == 2:
        a = float(input('Masukkan Panjang:'))
        b = float(input('Masukkan Lebar:'))
        print('Hasil Luas nya adalah: ', persegi_panjang(a,b))
    elif pilihan == 3:
        a = float(input('Masukkan Alas:'))
        b = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', segitiga(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan Jari-Jari:'))
        print('Hasil Luas nya adalah: ', lingkaran(a))
    elif pilihan == 5:
        a = float(input('Masukkan Sisi 1:'))
        b = float(input('Masukkan Sisi 2:'))
        c = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', trapesium(a,b,c))
    else:
        print('Pilihan Tidak Valid.')

from bangun_ruang import *
def Hitungan_Bangun_Ruang():
    print('Pilih operasi Luas Bangun Ruang yang ingin dilakukan:')
    print('1.Kubus')
    print('2.Balok')
    print('3.Tabung')
    print('4.Bola')
    print('5.Prisma')
    pilihan = int(input('Masukkan nomor operasi Bangun Datar yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan Sisi:'))
        print('Hasil Luas nya adalah: ', kubus(a))
    elif pilihan == 2:
        a = float(input('Masukkan Panjang:'))
        b = float(input('Masukkan Lebar:'))
        c = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', balok(a,b,c))
    elif pilihan == 3:
        a = float(input('Masukkan Jari-Jari:'))
        b = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', tabung(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan Jari-Jari:'))
        print('Hasil Luas nya adalah: ', bola(a))
    elif pilihan == 5:
        a = float(input('Masukkan Alas:'))
        b = float(input('Masukkan Tinggi Alas:'))
        c = float(input('Masukkan Tinggi Prisma:'))
        print('Hasil Luas nya adalah: ', prisma(a,b,c))
    else:
        print('Pilihan Tidak Valid.')

def Menu():
    print('Welcome, Silahkan pilih Operasi Bilangan berikut ini: ')
    print('1.Aritmatika')
    print('2.Luas Bangun Datar')
    print('3.Luas Bangun Ruang')
    print('4.Keluar dari program')

def utama():
    while True:
        Menu()
        inputan=input('silahkan masukkan operasi yang ingin dijalankan (1,2,3, dan 4 jika ingin keluar):')
        if inputan == '1':
            hitungan_aritmatika()
        elif inputan == '2':
            Hitungan_Bangun_Datar()
        elif inputan == '3':
            Hitungan_Bangun_Ruang()

        elif inputan == '4':
            print('Mengeluarkan dari Program, Terima Kasih.')
            break
        else:
            print('Pilihan Tidak Valid, Silahkan coba lagi.')

if __name__ == "__main__":
    utama()