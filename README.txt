NSFWBOT.py
THIS SOURCE CODE IS FOR PEOPLE WHO WANT TO MAKE NSFW COMMANDS IN THEIR DISCORD.PY BOTS FOR DISCORD OR VOLTAGE BOTS FOR REVOLT.

FILES
- nsfwcommand.py = Basic command for everything in Discord.py
- nsfwcommand-revolt.py = Basic command for everything in Voltage
- nsfwoverall.py = Is how it would look in a general discord bot.
- nsfwoverall-revolt.py = Is how it would look in a general Revolt bot.

REQUIREMENTS
- Packages: discord.py for Discord/Voltage for Revolt
- Knowledge: Has some knowledge of discord.py/Voltage

SETUP FOR NSFWOVERALL.PY
1. client.run("BOTTOKENHERE") replace BOTTOKENHERE with your bot token you got from creating a bot at discord.com/developers
2. Replace <##NSFW content here> with your code
3. In botdev = [BOTOWNERIDSHERE], replace BOTOWNERIDSHERE with your Staff user ids. Seperating with comma.
- Example botdev = [720847987756105809, 872608213076426763]
4. (Optional): In client = commands.Bot(command_prefix = '!'), replace ! with the prefix you want.

SETUP FOR NSFWOVERALL-REVOLT.PY
1. client.run("BOTTOKENHERE") replace BOTTOKENHERE with your bot token you got from creating a bot at https://app.revolt.chat/settings/bots
2. Replace <##NSFW content here> with your code
3. (Optional): In client = commands.CommandsClient("!"), replace ! with the prefix you want.

TO USE nsfwcommand.py and nsfwcommand-revolt.py, you must have knowledge of discord.py or Voltage.

TUTORIAL VIDEOS:
You can watch my tutorials videos on setting this up.
discord.py tutorial: https://www.youtube.com/watch?v=t5MZ6zQnaU8
Voltage tutorial: https://www.youtube.com/watch?v=USkSvoap5NI

HOW IT WORKS:
if ctx.channel.is_nsfw(): detects if the command is being run in a NSFW enabled channel (or Age-restricted channel with discord's current channel name). But I will refere to these 18+ channels as NSFW channels
This it is excuted in a NSFW channel, it triggers the code within the "if ctx.channel.is_nsfw():". If it is triggered outside of NSFW enabled channels, it will trigger the else statement of the code with in this case would be: "This command can only be used in a NSFW channel"
The same thing happens with "if ctx.channel.nsfw:" for Revolt

DISCLAIMER:
Any NSFW content not suitable to be on discord/revolt sfw channels must stay in NSFW marked channels (Or Age-restricted channels as with Discord's name changes)