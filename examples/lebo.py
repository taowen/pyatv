"""Simple example that scans for devices and connects to first one found."""

import asyncio
import sys

import pyatv

LOOP = asyncio.get_event_loop()


# Method that is dispatched by the asyncio event loop
async def find_lebo(loop):
    """Find a device and print what is playing."""
    print("Discovering devices on network...")
    atvs = await pyatv.scan(loop, timeout=5)

    if not atvs:
        raise Exception('No lebo found')

    for atv in atvs:
        if '投屏电视' in atv.name:
            return atv
    raise Exception('No lebo found')

async def main(loop):
    lebo = await find_lebo(loop)
    print(lebo)

if __name__ == "__main__":
    # Setup event loop and connect
    LOOP.run_until_complete(main(LOOP))
