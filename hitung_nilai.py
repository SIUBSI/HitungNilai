import os # Mengimpor modul OS (Operating System)

# Membuat Fungsi
def mulai(): # Fungsi Mulai
    os.system("cls") # Menggunakan modul Os untuk membersihkan layar pada Terminal "cls" (Clear Screen)
    while True:
        pilihan = int(input("\nPilih Menu:\n1. Hitung Nilai Ujian Murni\n2. Akhiri Program\n= "))
        if pilihan == 1:
            hitungNilaiUjianMurni() # Memanggil fungsi hitungNilaiUjiaNMurni
        elif pilihan == 2:
            exit()
        else:
            print("\n[Pesan]: Pilihan", pilihan, "tidak ditemukan.")

def hitungNilaiUjianMurni():
    os.system("cls")
    jumlahSoal = int(input("Masukkan Total Soal: "))
    if jumlahSoal == 50: # Apabila jumlah soal yang diinginkan adalah 50 soal.
        jawabanBenar = float(input("Masukkan Jumlah Jawaban Benar: "))
        if jawabanBenar >= 0 and jawabanBenar <= 50:
            hasilNilaiUjian = jawabanBenar * 2.00
            print(f"""
            Jumlah Soal: {jumlahSoal}
            Jumlah Jawaban Benar: {int(jawabanBenar)}
            👀 Nilai Ujian Murni: {hasilNilaiUjian:.2f} ({hasilNilaiUjian})""")
        else:
            print("\nJumlah 'Jawaban Benar' yang anda masukkan tidak dapat melebihi '50' dan tidak dapat kurang dari 0.")
    elif jumlahSoal == 35: # Apabila jumlah soal yang diinginkan adalah 35 soal.
        jawabanSalah = float(input("Masukkan Jumlah Jawaban Salah: "))
        if jawabanSalah >= 0 and jawabanSalah <= 35:
            hasilNilaiUjian = (jumlahSoal - jawabanSalah) / jumlahSoal * 100
            jawabanBenar = jumlahSoal - jawabanSalah
            print(f"""
            Jumlah Soal: {jumlahSoal}
            Jumlah Jawaban Benar: {int(jawabanBenar)}
            Jumlah Jawaban Salah: {int(jawabanSalah)}
            👀 Nilai Ujian Murni: {hasilNilaiUjian:.2f} ({hasilNilaiUjian})""")
        else:
            print("\nJumlah 'Jawaban Salah' yang anda masukkan tidak dapat melebihi '35' dan tidak dapat kurang dari 0.")
    else:
        print("\nAnda hanya dapat memasukkan Jumlah soal (35 atau 50).")


mulai()