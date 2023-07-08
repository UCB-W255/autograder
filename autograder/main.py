import logging

from slack_sdk import WebClient

logging.basicConfig(level=logging.DEBUG)

client = WebClient()
api_response = client.api_test()
