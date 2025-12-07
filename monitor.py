import requests
import hashlib
import time

# ضع هنا رابط الصفحة اللي عايز تراقبها
URL = "https://example.com/page-to-monitor"

# ضع هنا التوكن الخاص بالبوت
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# ضع هنا الـ Chat ID الخاص بيك
CHAT_ID = "YOUR_CHAT_ID_HERE"

HASH_FILE = "last_hash.txt"

def get_page_hash():
    try:
        r = requests.get(URL, timeout=10)
        r.encoding = "utf-8"
        content = r.text
        return hashlib.md5(content.encode()).hexdigest()
    except:
        return None

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, params=params)
    except Exception as e:
        print("Error sending Telegram message:", e)

def read_last_hash():
    try:
        with open(HASH_FILE, "r") as f:
            return f.read().strip()
    except:
        return None

def write_last_hash(h):
    with open(HASH_FILE, "w") as f:
        f.write(h)

# رسالة اختبار عند التشغيل
send_telegram_message("✅ اختبار: السكريبت شغال تمام!")

print("🔍 Monitoring started...")

while True:
    current_hash = get_page_hash()

    if current_hash is None:
        print("⚠ Cannot fetch page.")
        time.sleep(300)
        continue

    last_hash = read_last_hash()

    if last_hash is None:
        write_last_hash(current_hash)
        print("📌 First run – hash saved.")
    elif current_hash != last_hash:
        print("❗ Change detected! Sending Telegram alert...")
        send_telegram_message(f"📢 تم تحديث صفحة الإعلانات! راجع الرابط:\n{URL}")
        write_last_hash(current_hash)
    else:
        print("✓ No changes detected.")

    time.sleep(300)  # يشيّك كل 5 دقايق
