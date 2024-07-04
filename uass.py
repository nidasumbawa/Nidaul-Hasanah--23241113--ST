# Program untuk memilih warna

warna = ["merah", "biru", "hijau", "kuning", "ungu"]

while True:
    print("Daftar warna:")
    for i, w in enumerate(warna):
        print(f"{i+1}. {w}")

    pilihan = int(input("Masukkan nomor warna yang Anda pilih (0 untuk keluar): "))

    if pilihan == 0:
        print("Terima kasih telah menggunakan program ini.")
        break

    if pilihan > 0 and pilihan <= len(warna):
        print(f"Anda memilih warna {warna[pilihan-1]}")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")