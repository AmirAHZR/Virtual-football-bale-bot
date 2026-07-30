from main import clubs
from balethon import Client
from balethon.conditions import private, text

def show_team(text):
    t = ""
    for position in ["دروازه‌بان", "مدافع", "هافبک", "مهاجم",'وینگر']:
        t += f"{position}"
        ls = [clubs[text].get_players_by_position(position)][0]
        res = " \\\ ".join(ls)
        t += f"\n"+res+"\n"
        
    t+="اگه می خوای تو ساخت بازی فوتبال مجازی با بات بله کمک کنی تو https://github.com/AmirAHZR/Virtual-football-bale-bot/tree/main در خدمتم"
    return t

bot = Client("937461250:tRBJJH3meQL5KZkt69ORgNCcVQ7griV7cm8")


@bot.on_message(private & text)
async def echo(message):
    try:
        if clubs[message.text]:
            
            await message.reply(show_team(message.text))
            
    except:
        pass


bot.run()

