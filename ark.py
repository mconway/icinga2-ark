#!/usr/bin/env python3

import argparse
import json
import requests

def main():
    try:
        parser = argparse.ArgumentParser(description='DoThings')
        parser.add_argument("--ipaddress", required=True)
        parser.add_argument("--port", required=False, default=27015)
        args = parser.parse_args()
        request = requests.get("http://arkservers.net/api/query/" + args.ipaddress + ":" + args.port)
        response = request.content
        if response == b"null":
            print("Server is Offline")
            exit(1)
        else:
            jsonData = json.loads(response)
            print(jsonData["info"]["HostName"] + ": " + str(jsonData["info"]["Players"]) + "/" + str(jsonData["info"]["MaxPlayers"]))
    except Exception as e:
        print(e)

main()
