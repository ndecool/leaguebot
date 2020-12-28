import telepot
import sys
mqueue=""
split=sys.argv[1].split(',')
lenght=len(split)

for   y in range(lenght): 
    if y ==  0:
        mqueue = mqueue + ":fr:"+ split[y]+ "\n"
    else : 
        mqueue = mqueue + split[y]+ "\n"
print(mqueue)
bot = telepot.Bot('KEY BOT')
bot.sendMessage('your own id',mqueue)
