#!/usr/bin/env python3

#
# Sample client for connecting to Gourmet translation server. Ensure the docker is running separately, using
#  docker run -p 4000:4000 -i --rm <IMAGE_NAME> 
# (setting the external port as appropriate)
#


import argparse
import logging
import sys

import json
import requests

LOG = logging.getLogger(__name__)

def main():
  logging.basicConfig(format='%(asctime)s %(levelname)s: %(name)s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--hostname", default="localhost")
  parser.add_argument("-p", "--port", default="4000")
  args = parser.parse_args()

  LOG.debug(f"Connecting to translation server at {args.hostname}{args.port}")


  to_translate = "The climate summit was held in Glasgow."
  payload =  {"q" : to_translate}

  response = requests.post(f"http://{args.hostname}:{args.port}/translation", json = payload)
  if response:
    ret_payload = response.json()
    print(f"Translation: {ret_payload['result']}")
    print(f"Time: {ret_payload['time_taken']}")
    print(f"Error: {ret_payload['error']}")
  else:
    response.raise_for_status()




if __name__ == "__main__":
  main()
