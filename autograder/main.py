import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from psycopg_pool import AsyncConnectionPool
from slack_sdk import WebClient

from autograder.utils import get_conn_str, get_user_by_email

load_dotenv()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("autograder")
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.async_pool = AsyncConnectionPool(conninfo=get_conn_str())
    yield
    await app.async_pool.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    user_id = get_user_by_email(client)
    print(user_id)

    return vars(client.chat_postMessage(channel=user_id, text="test"))["data"]


@app.get("/students")
async def get_all_students(request: Request):
    async with request.app.async_pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                SELECT *
                FROM student
            """
            )
            results = await cur.fetchall()
            return results


@app.get("/students/{github_username}")
async def get_students_by_github(github_username: str, request: Request):
    async with request.app.async_pool.connection() as conn:
        async with conn.cursor() as cur:
            query = f"""
                SELECT ischool_email
                FROM student
                WHERE LOWER(github_username) = LOWER('{github_username}')
            """
            logger.debug(query)
            await cur.execute(query)
            ischool_email = await cur.fetchall()

            user_id = get_user_by_email(client, ischool_email[0][0])

            return vars(client.chat_postMessage(channel=user_id, text="test"))["data"]


# client.files_upload(
#     channels=user_id,
#     title="Your test output",
#     file="./output.log",
#     initial_comment="Here is the file",
# )
