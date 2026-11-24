class Cafe:
    def _init_(self, nama):
        self.nama = nama

    def pembukaan(self):
        print("================================")
        print("       SELAMAT DATANG DI CAFE")
        print("================================")
        print(f"Jamani: Wah, akhirnya sampai juga di {self.nama}!")
        print("Barista: Selamat datang! Silakan duduk.")
        print("Jamani: Terima kasih.")

    def pesan_kopi(self):
        print("\nBarista: Mau pesan apa, Kak?")
        print("1. Kopi Hitam")
        print("2. Cappuccino")
        print("3. Kopi Susu")

        pilihan = input("Jamani: Saya mau nomor berapa? ")

        if pilihan == "1":
            kopi = "Kopi Hitam"
        elif pilihan == "2":
            kopi = "Cappuccino"
        elif pilihan == "3":
            kopi = "Kopi Susu"
        else:
            kopi = "Kopi Susu"

        print(f"Jamani: Saya pesan {kopi} satu.")
        print(f"Barista: Baik, satu {kopi}. Ditunggu ya!")
        return kopi

    def percakapan(self):
        print("\nBarista: Ini kopinya, Kak.")
        print("Jamani: Wah, terima kasih.")
        print("Barista: Apakah kopinya sesuai selera?")
        print("Jamani: Enak sekali, cocok untuk menemani santai.")
        print("Barista: Senang mendengarnya.")
        print("Jamani: Cafe ini nyaman sekali.")
        print("Barista: Terima kasih sudah berkunjung.")
        print("Jamani: Sama-sama, saya pasti datang lagi.")

    def penutup(self):
        print("\n================================")
        print("Jamani: Baik, saya pulang dulu.")
        print("Barista: Hati-hati di jalan!")
        print("Terima kasih sudah berkunjung.")
        print("================================")


# Program Utama
cafe = Cafe("Cafe Senja")

cafe.pembukaan()
pesanan = cafe.pesan_kopi()
cafe.percakapan()
cafe.penutup()