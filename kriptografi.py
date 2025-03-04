import kripton

def menu():
    print("Şifreleme Yöntemleri:")
    print("1. Caesar Şifreleme")
    print("2. Caesar Şifre Çözme")
    print("3. Vigenere Şifreleme")
    print("4. Vigenere Şifre Çözme")
    print("5. Playfair Şifreleme")
    print("6. Playfair Şifre Çözme")
    print("7. Çıkış")

def main():
    while True:
        menu()
        choice = input("Bir seçenek girin (1-7): ")

        if choice == "1":
            how_many = int(input("Kaç adım kaydırmak istiyorsunuz? "))
            input_file = input("Şifrelenecek dosyanın adını girin: ")
            output_file = input("Çıktı dosyasının adını girin: ")
            kripton.caesar_crypt(how_many, input_file, output_file)

        elif choice == "2":
            how_many = int(input("Kaç adım kaydırmak istiyorsunuz? "))
            input_file = input("Şifresi çözülecek dosyanın adını girin: ")
            output_file = input("Çıktı dosyasının adını girin: ")
            kripton.caesar_decrypt(how_many, input_file, output_file)

        elif choice == "3":
            input_file = input("Şifrelenecek dosyanın adını girin: ")
            output_file = input("Çıktı dosyasının adını girin: ")
            key = input("Anahtarı girin: ")
            kripton.vigenere_crypt(input_file, output_file, key)

        elif choice == "4":
            input_file = input("Şifresi çözülecek dosyanın adını girin: ")
            output_file = input("Çıktı dosyasının adını girin: ")
            key = input("Anahtarı girin: ")
            kripton.vigenere_decrypt(input_file, output_file, key)

        elif choice == "5":
            kripton.playfair_crypt()

        elif choice == "6":
            kripton.playfair_decrypt()

        elif choice == "7":
            print("Görüşmek üzere!")
            break

        else:
            print("Geçersiz seçenek. Lütfen 1-7 arası bir seçenek girin.")

if __name__ == "__main__":
    main()
