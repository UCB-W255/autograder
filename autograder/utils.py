import logging
import os

from slack_sdk.errors import SlackApiError

logger = logging.getLogger("autograder")


def get_user_by_email(client, email="winegarj@ischool.berkeley.edu"):
    try:
        result = client.users_lookupByEmail(email=email)["user"]["id"]
    except SlackApiError:
        logger.error("Unable to find user by email: {}".format(email))
        exit(1)

    return result


def get_conn_str():
    return f"""
    dbname={os.getenv('POSTGRES_DB')}
    user={os.getenv('POSTGRES_USER')}
    password={os.getenv('POSTGRES_PASSWORD')}
    host={os.getenv('POSTGRES_HOST')}
    port={os.getenv('POSTGRES_PORT')}
    """
