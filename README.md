# 🛠️ FixMate Bridge

This is the **FixMate Telegram Bridge**, a small Flask server that connects maintenance leads (from your chatbot or website) directly to your Telegram account.

## 🚀 Features
- Sends customer leads from the web form to your Telegram bot.
- Simple REST API endpoint: `/send_lead`
- Uses `Flask` + `Gunicorn` for production.

## 🧩 Environment Variables
| Key | Description | Example |
|-----|--------------|---------|
| TELEGRAM_BOT_TOKEN | Your Telegram bot token | `8590267654:AAG24Oo6GlAUjVxZ1JXjNLNq_LZ5gIK4BDs` |
| TELEGRAM_CHAT_ID | Your Telegram chat/user ID | `8187670531` |
| PORT | Port for Render | `10000` |

## 🧠 Example JSON to send
```json
{
  "fullName": "John Doe",
  "phone": "+27 78 555 1234",
  "service": "Plumbing Leak",
  "message": "Water leaking under sink"
}
