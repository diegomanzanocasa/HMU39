import sys
import os
import requests
import json

from time import sleep

FILE_NAME = '/tmp/last_known_ip.dat'
TIME_INTERVAL = 10
TEAMS_ID = 'c87a997a-cb22-4f4b-b826-d7b84ba19bc3'
CHANNEL_ID = "19:6330121ab5ae463da28ceedd06897c68@thread.skype"

def raspberry_trigger(text)
    # todo code to conenct with raspberry
    pass


def check_alarm_messages():
    teams_get_messages_url = 'https://graph.microsoft.com/beta/teams/' + TEAMS_ID +'/' \
                             'channels/' + CHANNEL_ID + '/messages/'
    headers = {"Authorization": 'Bearer ' + access_token_gmc}
    try:
        response = requests.get(teams_get_messages_url, headers=headers)
        # TODO check response here and if it is contains different strings call to raspberry
        # raspberry_trigger(text)
    except Exception as e:
        with open(FILE_NAME, 'w') as fw:
            fw.write("TEMP")


try:
    while True:
        check_alarm_messages()
        sleep(TIME_INTERVAL)
except KeyboardInterrupt:
    print("Stopping program ...")
except:
    print("Unexpected error: %s" % sys.exc_info()[0])
    raise
