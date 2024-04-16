import re

''''
§6Command Help: §f/kill/n
§6Description: §fKills specified player./n
§6Usage(s);/n
/kill §e<player>§r §6- Kills the specified player/n
'''
file = '''
    §6Command Help: §f/kill
    §6Description: §fKills specified player.
    §6Usage(s);
    /kill §e<player>§r §6- Kills the specified player
'''

print(re.sub('§.?','',file))