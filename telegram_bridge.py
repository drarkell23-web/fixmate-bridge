from flask import Flask, request, jsonify
import requests
from datetime import datetime
import os

app = Flask(__name__)

# Telegram Bot Config
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8590267654:AAG24Oo6GlAUjVxZ1JXjNLNq_LZ5gIK4BDs")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "8187670531")


@app.route("/")
def index():
    return jsonify({"ok": True, "message": "FixMate Telegram Bridge is running."})


@app.route("/send_lead", methods=["POST"])
def send_lead():
    """Receives lead data and sends it to Telegram."""
    data = request.get_json()
    if not data:
        return jsonify({"ok": False, "error": "No JSON data received"}), 400

    name = data.get("fullName", "Unknown")
    phone = data.get("phone", "N/A")
    service = data.get("service", "N/A")
    message = data.get("message", "N/A")

    text = (
        f"🧰 *New Maintenance Lead Received!*\n\n"
        f"👤 Name: {name}\n"
        f"📞 Phone: {phone}\n"
        f"🛠 Service: {service}\n"
        f"📝 Message: {message}\n"
        f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"},
            timeout=10
        )
        if response.status_code == 200:
            return jsonify({"ok": True, "message": "Lead sent to Telegram!"})
        else:
            return jsonify({"ok": False, "error": "Telegram API error"}), 500
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
