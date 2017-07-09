# Andrew J Miller
# Jun 9 2017

"""
    Bot that prints to the console (andros.py)
""";

# Import libraries
import asyncio
import json
import sys
import aiohttp

# Need these also
from api import api_call
from config import DEBUG, TOKEN

# This is pretty obvious to see.
# This takes in the messaege as long as it's a message and prints it out.
# If there's an error it lets us know.
async def consumer(message):
    """
        Display recieved message
    """
    if message.get('type') == 'message':
        user = await api_call('users.info', {'user': message.get('user')})
        
        print("{0}: {1}".format(user["user"]["name"], message["text"]))
        
    else:
        print(message, file= sys.stderr)


# This connects but notice the added aysyncio funciton.
async def andros(token = TOKEN):
    """
        Creates a bot that connects with Slack Real Time Messaging API
    """
    rtm = await api_call("rtm.start")
    assert rtm['ok'], "Error connecting to RTM API"

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(rtm["url"]) as ws:
            async for msg in ws:
                assert msg.tp == aiohttp.MsgType.text
                message = json.loads(msg.data)
                asyncio.ensure_future(consumer(message))

# Run Block
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(DEBUG)
    loop.run_until_complete(andros())
    loop.close()