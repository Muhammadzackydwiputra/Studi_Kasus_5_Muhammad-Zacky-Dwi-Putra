def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        harga = 200000
    elif jenis_kamar == "Deluxe":
        harga = 350000

    total_harga = harga * lama_menginap

    return total_harga

jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
tanggal_check_in = int(input("Masukkan tanggal check-in: "))
tanggal_check_out = int(input("Masukkan tanggal check-out: "))

lama_menginap = tanggal_check_out - tanggal_check_in

total_harga = hitung_biaya(jenis_kamar, lama_menginap)

print("Pemesanan Kamar Hotel")
print("Jenis kamar        :", jenis_kamar)
print("Tanggal check-in   :", tanggal_check_in)
print("Tanggal check-out  :", tanggal_check_out)
print("Lama menginap      :", lama_menginap, "malam")
print("Total harga        :", total_harga)