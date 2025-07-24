import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import os
from threading import Thread
from flask import Flask

class AltinTakipBot:
    def __init__(self):
        self.bot_token = "7919653089:AAHMtvSOC1MHX7dnRJsISoL9qGq1vI7XVDw"
        self.chat_id = "-4818998822"
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        self.altin_url = "https://altin.doviz.com/gram-altin"
        self.baslangic_alis = None
        self.baslangic_satis = None
        self.son_alis = None
        self.son_satis = None
        self.artis_miktari = 50  # TL
        self.bildirim_araligi = 3600  # 1 saat
        self.son_bildirim_zamani = None

    def vakifbank_fiyat_al(self):
        try:
            response = requests.get(self.altin_url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            vakifbank_row = None
            for row in soup.find_all("tr"):
                if row.find("td") and "Vakıfbank" in row.text:
                    vakifbank_row = row
                    break
            if vakifbank_row:
                tds = vakifbank_row.find_all("td")
                fiyat1 = float(tds[1].text.strip().replace(".", "").replace(",", "."))
                fiyat2 = float(tds[2].text.strip().replace(".", "").replace(",", "."))
                alis = min(fiyat1, fiyat2)
                satis = max(fiyat1, fiyat2)
                return alis, satis
            else:
                print("Vakıfbank satırı bulunamadı!")
                return None, None
        except Exception as e:
            print(f"Fiyat alınırken hata: {e}")
            return None, None

    def telegram_mesaj_gonder(self, mesaj):
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": mesaj,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=data, timeout=10)
            if response.status_code == 200:
                print(f"Mesaj gönderildi: {mesaj}")
                return True
            else:
                print(f"Mesaj gönderilemedi: {response.text}")
                return False
        except Exception as e:
            print(f"Telegram mesaj gönderme hatası: {e}")
            return False

    def fiyat_degisimi_kontrol(self, yeni_alis, yeni_satis):
        simdi = time.time()
        bildirim_gonderildi = False
        # Alış fiyatı kontrolü
        if self.son_alis is not None:
            fark_alis = yeni_alis - self.baslangic_alis
            if abs(fark_alis) >= self.artis_miktari:
                tip = "ARTIŞ" if fark_alis > 0 else "DÜŞÜŞ"
                mesaj = f"<b>Vakıfbank Gram Altın Alış Fiyatı {tip}!</b>\n\n"
                mesaj += f"Başlangıç: {self.baslangic_alis:,.2f} ₺\n"
                mesaj += f"Güncel: {yeni_alis:,.2f} ₺\n"
                mesaj += f"Değişim: {fark_alis:+,.2f} ₺\n"
                mesaj += f"⏰ {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
                if self.son_bildirim_zamani is None or simdi - self.son_bildirim_zamani > self.bildirim_araligi:
                    self.telegram_mesaj_gonder(mesaj)
                    self.son_bildirim_zamani = simdi
                    bildirim_gonderildi = True
        # Satış fiyatı kontrolü
        if self.son_satis is not None:
            fark_satis = yeni_satis - self.baslangic_satis
            if abs(fark_satis) >= self.artis_miktari:
                tip = "ARTIŞ" if fark_satis > 0 else "DÜŞÜŞ"
                mesaj = f"<b>Vakıfbank Gram Altın Satış Fiyatı {tip}!</b>\n\n"
                mesaj += f"Başlangıç: {self.baslangic_satis:,.2f} ₺\n"
                mesaj += f"Güncel: {yeni_satis:,.2f} ₺\n"
                mesaj += f"Değişim: {fark_satis:+,.2f} ₺\n"
                mesaj += f"⏰ {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
                if self.son_bildirim_zamani is None or simdi - self.son_bildirim_zamani > self.bildirim_araligi:
                    self.telegram_mesaj_gonder(mesaj)
                    self.son_bildirim_zamani = simdi
                    bildirim_gonderildi = True
        self.son_alis = yeni_alis
        self.son_satis = yeni_satis
        return bildirim_gonderildi

    def bot_durumu_gonder(self):
        mesaj = f"🤖 <b>Vakıfbank Gram Altın Takip Botu Aktif</b> 🤖\n\n"
        mesaj += f"Başlangıç Alış: {self.baslangic_alis:,.2f} ₺\n"
        mesaj += f"Başlangıç Satış: {self.baslangic_satis:,.2f} ₺\n"
        mesaj += f"Bildirim Eşiği: ±{self.artis_miktari} TL\n"
        mesaj += f"⏰ {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        mesaj += f"\nBot çalışıyor ve fiyatları takip ediyor..."
        self.telegram_mesaj_gonder(mesaj)

    def takip_dongusu(self):
        print("Vakıfbank altın takip botu başlatıldı...")
        while True:
            alis, satis = self.vakifbank_fiyat_al()
            if alis is not None and satis is not None:
                if self.baslangic_alis is None or self.baslangic_satis is None:
                    self.baslangic_alis = alis
                    self.baslangic_satis = satis
                    self.son_alis = alis
                    self.son_satis = satis
                    print(f"Başlangıç Alış: {alis:,.2f} ₺, Satış: {satis:,.2f} ₺")
                    self.bot_durumu_gonder()
                else:
                    print(f"Güncel Alış: {alis:,.2f} ₺, Satış: {satis:,.2f} ₺")
                    self.fiyat_degisimi_kontrol(alis, satis)
            else:
                print("Fiyatlar alınamadı, tekrar deneniyor...")
            time.sleep(300)  # 5 dakika

    def baslat(self):
        try:
            self.takip_dongusu()
        except KeyboardInterrupt:
            print("\nBot durduruluyor...")
            self.telegram_mesaj_gonder("🛑 <b>BOT DURDURULDU</b> 🛑")
        except Exception as e:
            print(f"Bot başlatılırken hata: {e}")

if __name__ == "__main__":
    # Botu ayrı bir thread'de başlat
    t = Thread(target=lambda: AltinTakipBot().baslat())
    t.daemon = True
    t.start()

    # Flask web sunucusunu başlat (Render için)
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Altın Takip Botu Çalışıyor!"

    @app.route("/health")
    def health():
        return "OK"

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port) 