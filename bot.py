from telethon import TelegramClient
import asyncio

# Nhập API ID và API HASH từ https://my.telegram.org/apps
API_ID = 22234310  # Thay bằng API ID của bạn
API_HASH = "99137cc9a73788b8cf643e7a2c6ec6db"  # Thay bằng API HASH của bạn

# Nhập ID nhóm cần gửi tin nhắn (Lấy bằng @userinfobot)
GROUP_ID = -1002307725134  # Thay bằng ID nhóm thật (dạng số nguyên, có thể âm)

# Tạo client
client = TelegramClient("bot_session", API_ID, API_HASH)

async def auto_send():
    while True:
        try:
            await client.send_message(GROUP_ID, "/fl3 huy.gio.taii")
            print("Đã gửi tin nhắn vào nhóm!")
        except Exception as e:
            print("Lỗi:", e)
        await asyncio.sleep(17 * 60)  # 16 phút

with client:
    client.loop.run_until_complete(auto_send())
