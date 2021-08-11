from os import link
import aiohttp
import asyncio
import pandas as pd
df_row = pd.read_csv("109all.csv")
async def main():
    links = df_row.URL[11:20]
    async with aiohttp.ClientSession() as session:
        for i in range (len (links)):

            async with session.get(links[i]) as response:

                print("Status:", response.status)

                html = await response.text()
                print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())