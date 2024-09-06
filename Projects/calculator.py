while True:
    # Kullanıcı girişleri:
    # İlk iki sayıyı giriniz.
    num1 = int(input("1. Sayıyı giriniz: "))
    num2 = int(input("2. Sayıyı giriniz: "))

    # İki sayı arasında olacak metodu seç.
    method = input("Metodu giriniz: ")

    # Metodun yazılıp yazılmadığı kontrol edilsin.
    if bool(method):
        try:
            result = None

            # Hangi metod belirtildiyse onu seç.
            match(method):
                case "+":
                    result = num1 + num2

                case "-":
                    result = num1 - num2

                case "*":
                    result = num1 * num2

                case "/":
                    result = num1 / num2

                case "^":
                    result = num1 ** num2

                case _:
                    print("HATA: Geçersiz metod bildirildi.")

            # Sonucu yazdır.
            if result is not None:
                if method == "/":
                    print(f"Sonuç: {result:.2f}")

                else:
                    print(f"Sonuç: {result}")

        except ZeroDivisionError:
            # 0'a bölünme varsa hata mesajı verilsin.
            print("HATA: 0'a bölünme var. Lütfen farklı bir sayı deneyiniz.")

    else:
        print("HATA: Lütfen bir metod giriniz.")
    
    # Kullanıcı döngünün devam etmesini istemiyorsa devam ettirilmesin.
    if input("INFO: Devam etmek istiyor musunuz? (e\h): ").lower() != "e":
        break
else:
    # Bunun aslında pek anlamı yok.
    print("Döngü başarıyla sona erdi.")