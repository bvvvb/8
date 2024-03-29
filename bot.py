from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
from telegraph import upload_file
import os
app=Client(
    "topac_mustafa",
    api_id = 21236276,#ايبي ايدي
    api_hash = "775f8c2f523b73c64a1a2149458480f2",#ايبي هاش
    bot_token = '6815404267:AAGQ5NE4p1kY9X4F2j8clhtjVIIK7UKTA1E'#توكن بوتك
)

@app.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f""" - welcome {message.from_user.mention}
Convert the link to the Telegraph link
 Supported formulas : jpeg - png - jpg - mp4 - gif
 [ usaByte ](https://t.me/usaByte)"""
    await app.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@app.on_message(filters.media & filters.private)
async def glink(client, message):
    try:
        async def progress(current, total):
            await text.edit_text(f"Loading.. {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            lo = await message.download(location, progress=progress)
            await text.edit_text("Uploading..")
            up = upload_file(lo) 
            await text.edit_text(f"**the Link**:\n\n<code>https://telegra.ph{up[0]}</code>")     
            os.remove(lo) 
        except Exception as e:
            await text.edit_text(f"**Error**\n\n<i>**Because**: {e}</i>")
            os.remove(lo) 
            return                 
    except Exception:
        pass        
                      
print('')
sleep(2)
print("   تم التشغيل")
app.run()
