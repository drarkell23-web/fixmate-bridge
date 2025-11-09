from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ===========================
# 🔒 KEEP THESE SECRET!
# ===========================
BOT_TOKEN = "8590267654:AAG24Oo6GlAUjVxZ1JXjNLNq_LZ5gIK4BDs"
CHAT_IDS = ["8187670531"]  # Add more if you want to receive on multiple chats

@app.route("/")
def home():
    return jsonify({"ok": True, "message": "FixMate Telegram Bridge is running."})

@app.route("/send_lead", methods=["POST"])
def send_lead():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"ok": False, "error": "No data received"}), 400

    msg = f"""🛠️ *New FixMate Lead*
👤 *Name:* {data.get('fullName','-')}
📞 *Phone:* {data.get('phone','-')}
📧 *Email:* {data.get('email','-')}
🧰 *Service:* {data.get('serviceCategory','-')}
📝 *Issues:* {data.get('specificIssues','-')}
🏠 *Property:* {data.get('propertyType','-')}
📍 *Address:* {data.get('address','-')}, {data.get('city','')}
📅 *Preferred:* {data.get('preferredDate','-')} {data.get('preferredTime','-')}
💵 *Budget:* {data.get('budgetRange','-')}
☎️ *Contact:* {data.get('contactMethod','-')}
🧾 *Notes:* {data.get('extraNotes','-')}"""

    for cid in CHAT_IDS:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
                timeout=10
            )
        except Exception as e:
            print(f"⚠️ Telegram send failed for {cid}: {e}")

    return jsonify({"ok": True, "message": "Lead sent to Telegram."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
