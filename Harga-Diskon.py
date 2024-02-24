# Script python untuk perhitungan harga diskon
# https://github.com/anon9497

# Meminta input harga awal dan persen diskon
harga_awal = float(input("Masukkan harga awal: "))
persen_diskon = float(input("Masukkan persen diskon: "))

# Menghitung harga akhir setelah diskon
harga_akhir = harga_awal * (1 - persen_diskon/100)

# Menampilkan hasil perhitungan
print("Harga awal:", harga_awal, "rupiah")
print("Diskon:", persen_diskon, "%")
print("Harga akhir:", harga_akhir, "rupiah")