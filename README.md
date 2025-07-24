# Gold Price Telegram Bot (Vakıfbank)

This bot continuously tracks Vakıfbank's gram gold buy and sell prices. It sends a notification to your Telegram group every time the price increases or decreases by 50 TL compared to the starting value.

---

## Features

- 📊 **Real-time gold price tracking (Vakıfbank)**
- 🚨 **Threshold notifications (±50 TL change)**
- 📈 **Buy and sell price monitoring**
- ⏰ **Notification interval control (1 hour)**
- 💬 **Telegram group integration**

## Installation

1. **Install required packages:**
```bash
pip install -r requirements.txt
```

2. **Check bot settings:**
   - Make sure your bot token and chat ID are correct in `altin_takip_bot.py`

## Usage

```bash
python altin_takip_bot.py
```

## How it works
- The bot fetches Vakıfbank's gram gold buy and sell prices from [altin.doviz.com](https://altin.doviz.com/gram-altin)
- The starting buy and sell prices are set as the reference
- If the buy or sell price changes by ±50 TL or more, a notification is sent
- Notifications are limited to once per hour for each type

## Security
- Keep your bot token safe
- Make sure your chat ID is correct
- Run the bot only on trusted servers

## Troubleshooting
- If the bot doesn't work, check your internet connection
- Make sure your bot token and chat ID are correct

---

# Altın Takip Telegram Botu (Vakıfbank)

Bu bot, Vakıfbank'ın gram altın alış ve satış fiyatlarını sürekli takip eder. Başlangıç değerine göre alış veya satış fiyatı her 50 TL arttığında veya azaldığında Telegram grubunuza bildirim gönderir.

## Özellikler

- 📊 **Gerçek zamanlı Vakıfbank altın fiyat takibi**
- 🚨 **Eşik değer uyarıları (±50 TL değişim)**
- 📈 **Alış ve satış fiyatı takibi**
- ⏰ **Bildirim aralığı kontrolü (1 saat)**
- 💬 **Telegram grup entegrasyonu**

## Kurulum

1. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

2. **Bot ayarlarını kontrol edin:**
   - `altin_takip_bot.py` dosyasında bot token ve chat ID'nin doğru olduğundan emin olun

## Kullanım

```bash
python altin_takip_bot.py
```

## Nasıl çalışır?
- Bot, [altin.doviz.com](https://altin.doviz.com/gram-altin) adresinden Vakıfbank gram altın alış ve satış fiyatlarını çeker
- Başlangıçta alış ve satış fiyatlarını referans olarak alır
- Alış veya satış fiyatı ±50 TL değişirse bildirim gönderir
- Her bildirim türü için en az 1 saat arayla tekrar bildirim gönderilir

## Güvenlik
- Bot token'ınızı güvenli tutun
- Chat ID'nizi doğru ayarladığınızdan emin olun
- Botu sadece güvenilir sunucularda çalıştırın

## Sorun Giderme
- Bot çalışmıyorsa internet bağlantınızı kontrol edin
- Bot token'ınızın ve chat ID'nizin doğru olduğundan emin olun 