# This is a scratch file for developing the Discord vesion of the bot
# Andy Miller
# Jun 9 2017

# Import libraries & grab neccessary objects
import asyncio
import json
import aiohttp
from config import TOKEN
URL = "https://discordapp.com/api"

# This defines the call to the Discord API.
# It asks for a response from the URL
# The response is returned as a JSON.
async def api_call(path):
    """
        Returns the JSON body of a call to the Discord Rest API
    """
    
    with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}{path}") as response:
            assert 200 == response.status, response.reason
            return await response.json()

# This program runs the definition based on the gateway path.
# Notice no TOKEN has been used yet.
# That is because this main is connecting us to our websocket.
# The asynchrony of this function is that it continues other processes until this is ready/
async def main():
    """Main program."""
    response = await api_call("/gateway")
    await start(response["url"])

# But where is the start function?
# Oh it's here:
# We wait for a message and then we print it
# But where is the start function?
# Oh it's here:
# We wait for a message and then we print it
async def start(url):
    with aiohttp.ClientSession() as session:
        async with session.ws_connect(
                f"{url}?v=6&encoding=json") as ws:
            async for msg in ws:
                data = json.loads(msg.data)
                
                if data["op"] == 10: # Hello
                    await ws.send_json({
                        "op": 2, #Identity
                        "d": {
                            "token": TOKEN,
                            "properties": {},
                            "compress": False,
                            "large_threshold": 250
                        }
                    })
                
                elif data["op"] == 0: "Dispatch"
                    print(data['t'], data['d'])
                    
                else:
                    print(data)