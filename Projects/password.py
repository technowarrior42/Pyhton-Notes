import time

# Asıl şifrenin ta kendisi
asil_sifre : str = "1838736"

def sure_fonksiyonu(sure : int) -> None:
    # Belli bir deneme hakkını bitirdikten sonra bu süreyi başlat.
    for sn in range(sure, 0, -1):
        print(f"Kalan süre: {sn} saniye")

        time.sleep(1)
    
    # Süre bittimi tekrar şifreyi yazabilir.
    sifre_fonksiyonu()

def sifre_fonksiyonu() -> None:
    # max deneme sayısı.
    kalan_deneme : int = 4

    while kalan_deneme > 0:
        # Kullanıcı girişi yapılır.
        sifre = input("Şifreyi giriniz: ")

        # Şifrenin girilip girilmediği kontrol edilir.
        if bool(sifre):
            if sifre == asil_sifre:
                print("Hoşgeldiniz.")
                break
            
            else:
                # Şifre yanlışsa her denemede bir deneme hakkı elden alınacaktır.
                kalan_deneme -= 1

                if kalan_deneme != 0:
                    print("Şifre yanlış lütfen tekrar giriniz.")
                    print(f"{kalan_deneme} hakkınız kaldı. ")
            
        else:
            print("Lütfen şifreyi giriniz.")
        
        if kalan_deneme == 0:
            print("Tüm deneme haklarınız bitti. Süre bittikten sonra tekrar deneyiniz.")
            sure_fonksiyonu(120)

sifre_fonksiyonu()