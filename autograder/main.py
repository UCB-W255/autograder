import logging
import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("autograder")

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


users_store = {}
email = "james.winegar@corrdyn.com"
try:
    result = client.users_lookupByEmail(email=email)
except SlackApiError:
    logger.error("Unable to find user by email: {}".format(email))
    exit(1)

print(result["user"].keys())
user_id = result["user"]["id"]
print(user_id)

# client.chat_postMessage(channel=user_id, text="test")

client.files_upload(
    channels=user_id,
    title="Your test output",
    file="./output.log",
    initial_comment="Here is the file",
)
