# post a message to discord api via a bot
# bot must be added to the server and have write access to the channel
# you may need to connect with a websocket the first time you run the bot
#   use a library like discord.py to do so
import requests
#import datetime
import json
#import pickle
from argparse import ArgumentParser
import os
import sys

class DiscordMsg:
    def __init__(self,authToken):
        self.authToken = authToken

    def post_msg(self,channelID,message):
        baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
        headers = { "Authorization":"{}".format(self.authToken),
                    "Content-Type":"application/json", }
        POSTedJSON =  json.dumps ( {"content":message} )

        r = requests.post(baseURL, headers = headers, data = POSTedJSON)

def main():
    parser = ArgumentParser(description='Send')
    parser.add_argument("--secret", dest="config_path",
                        help="Farming Secret Config Path", metavar="AUTH", default="secret.json")
    options = parser.parse_args()

    cwd = sys.path[0]
    with open(os.path.join(cwd,options.config_path)) as f:
        data = json.loads(f.read())

    msg = DiscordMsg(data["authToken"]) # get from the bot page. must be a bot, not a discord app
    for k,v in data["farmConfig"].items():
        msg.post_msg(k,v) # Channel is 2nd number in the discord url


    #Will not use this any more as we'll run a cronjob every 30 mins
    ##Open the timecheck file if exists, if not set default time epoch 0
    #try:
        #with open("timecheck.pickle","rb") as f:
            #timecheck=pickle.load(f)
    #except:
        #o_time=datetime.datetime.fromtimestamp(0)
        #timecheck = [o_time, o_time]

    #timenow = datetime.datetime.now()
    #timediff_farm = timenow-timecheck[0]
    #timediff_peel = timenow-timecheck[1]

    #if timediff_farm>datetime.timedelta(hours=1):
        #post_msg("831647957681831946","+farm")
        #timecheck[0] = datetime.datetime.now()
        #with open("timecheck.pickle","wb") as f:
            #pickle.dump(timecheck,f)
    #else:
        #print(timediff_farm,"is not close to 1 hour to farm Rebirth/Remastered")

    #if timediff_peel>datetime.timedelta(hours=5):
        #post_msg("760419063351869460","+peel")
        #timecheck[1] = datetime.datetime.now()
        #with open("timecheck.pickle","wb") as f:
            #pickle.dump(timecheck,f)
    #else:
        #print(timediff_peel,"is not close to 5 hours to peel ESP")

if __name__=="__main__":
    main()
