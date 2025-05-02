# Aplikasi Kasir Sederhana

class Produk:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def subtotal(self):
        return self.harga * self.jumlah

class Kasir:
    def __init__(self):
        self.daftar_belanja = []

    def tambah_produk(self):
        nama = input("Masukkan Nama Barang: ")
        harga = int(input("Masukkan Harga Barang: "))
        jumlah = int(input("Masukkan Jumlah Barang: "))
        produk = Produk(nama, harga, jumlah)
        self.daftar_belanja.append(produk)
        print(f"{nama} ditambahkan ke keranjang.\n")

    def tampilkan_belanja(self):
        if not self.daftar_belanja:
            print("Belum ada barang dalam keranjang.")
            return
        print("=== Daftar Belanja ===")
        for produk in self.daftar_belanja:
            print(f"{produk.nama} - {produk.jumlah} x Rp{produk.harga} = Rp{produk.subtotal()}")
        print(f"Total: Rp{self.hitung_total()}")

    def hitung_total(self):
        return sum(produk.subtotal() for produk in self.daftar_belanja)

    def cetak_struk(self, uang_dibayar):
        total = self.hitung_total()
        print("\n=== STRUK BELANJA ===")
        self.tampilkan_belanja()
        print(f"Uang dibayar: Rp{uang_dibayar}")
        kembalian = uang_dibayar - total
        print(f"Kembalian: Rp{kembalian if kembalian >= 0 else 0}")
        if kembalian < 0:
            print("⚠️ Uang Anda kurang!")

# === Pemakaian Program ===
kasir = Kasir()

# Tambah 2 produk sebagai contoh
kasir.tambah_produk()
kasir.tambah_produk()

# Tampilkan belanjaan
kasir.tampilkan_belanja()

# Cetak struk
uang = int(input("\nMasukkan uang yang dibayarkan: "))
kasir.cetak_struk(uang)
