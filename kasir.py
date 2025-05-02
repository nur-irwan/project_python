
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
        print("=== Tambah Produk (ketik 'selesai' untuk berhenti) ===")
        while True:
            nama = input("Masukkan Nama Barang: ")
            if nama.lower() == 'selesai':
                break
            try:
                harga = int(input("Masukkan Harga Barang: "))
                jumlah = int(input("Masukkan Jumlah Barang: "))
                produk = Produk(nama, harga, jumlah)
                self.daftar_belanja.append(produk)
                print(f"{nama} ditambahkan ke keranjang.\n")
            except ValueError:
                print("Input harga dan jumlah harus berupa angka. Coba lagi.\n")

    def hapus_produk(self, nama):
        for produk in self.daftar_belanja:
            if produk.nama.lower() == nama.lower():
                self.daftar_belanja.remove(produk)
                print(f"{nama} telah dihapus dari keranjang.")
                return
        print(f"{nama} tidak ditemukan.")

    def edit_jumlah(self, nama, jumlah_baru):
        for produk in self.daftar_belanja:
            if produk.nama.lower() == nama.lower():
                produk.jumlah = jumlah_baru
                print(f"Jumlah {nama} diubah menjadi {jumlah_baru}.")
                return
        print(f"{nama} tidak ditemukan.")

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
        print(f"Kembalian: Rp{max(0, kembalian)}")
        if kembalian < 0:
            print("⚠️ Uang Anda kurang!")

    def simpan_struk_ke_file(self, uang_dibayar, nama_file="struk.txt"):
        total = self.hitung_total()
        with open(nama_file, "w") as file:
            file.write("=== STRUK BELANJA ===\n")
            for produk in self.daftar_belanja:
                file.write(f"{produk.nama} - {produk.jumlah} x Rp{produk.harga} = Rp{produk.subtotal()}\n")
            file.write(f"\nTotal: Rp{total}\n")
            file.write(f"Uang dibayar: Rp{uang_dibayar}\n")
            kembalian = uang_dibayar - total
            file.write(f"Kembalian: Rp{max(0, kembalian)}\n")
        print(f"Struk telah disimpan ke file '{nama_file}'")


if __name__ == '__main__':
    kasir = Kasir()
    while True:
        print("\n--- Menu Kasir ---")
        print("1. Tambah Produk")
        print("2. Hapus Produk")
        print("3. Edit Jumlah Produk")
        print("4. Tampilkan Belanjaan")
        print("5. Cetak Struk & Simpan ke File")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            kasir.tambah_produk()
        elif pilihan == '2':
            nama = input("Masukkan nama produk yang ingin dihapus: ")
            kasir.hapus_produk(nama)
        elif pilihan == '3':
            nama = input("Masukkan nama produk yang ingin diedit: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            kasir.edit_jumlah(nama, jumlah_baru)
        elif pilihan == '4':
            kasir.tampilkan_belanja()
        elif pilihan == '5':
            uang = int(input("Masukkan uang yang dibayarkan: "))
            kasir.cetak_struk(uang)
            kasir.simpan_struk_ke_file(uang)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan aplikasi kasir.")
            break
        else:
            print("Pilihan tidak valid.")
