# Andrew J Miller
# Jun 9 2017

# Import libraries
import asyncio
import aiohttp

# Import our config file.
# This is just to hide the Token file.
from config import DEBUG, TOKEN

async def api_call(method, data = None, token = TOKEN):
    # This calls the slack API.
    
    # Acts on aiohttp.Client as session
    with aiohttp.ClientSession() as session:
        
        # Creates our form.
        form = aiohttp.FormData(data or {})
        
        # Adds our token to the form.
        form.add_field('token', token)
        
        # This is a coroutine, it is a function that stops and resumes based on the awaoy response below.
        # 
        async with session.post('https://slack.com/api/{0}'.format(method),
                                data = form) as response:
            assert 200 == response.status, ('{0} with {1} failed.'.format(method, data))
            
            return await response.json()


# This is the main run block.
# if you get an ok it means your token key is working.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(DEBUG)
    response = loop.run_until_complete(api_call('auth.test'))
    loop.close()

    assert response['ok']
    print(response)