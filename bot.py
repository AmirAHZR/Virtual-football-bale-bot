from main import clubs
from balethon import Client
from balethon.conditions import private, text

bot = Client("937461250:tRBJJH3meQL5KZkt69ORgNCcVQ7griV7cm8")


@bot.on_message(private & text)
async def echo(message):
    try:
        if clubs[message.text]:
            t = ""
            for position in ["دروازه‌بان", "مدافع", "هافبک", "مهاجم",'وینگر']:
                t += f"{position}"
                ls = [clubs[message.text].get_players_by_position(position)][0]
                res = " \\\ ".join(ls)
                t += f"\n"+res+"\n"
                
            t+="اگه می خوای تو ساخت بازی فوتبال مجازی با بات بله کمک کنی تو https://github.com/AmirAHZR/Virtual-football-bale-bot/tree/main در خدمتم"
            await message.reply(t)
            
    except:
        pass


bot.run()

