#!/usr/bin/env python3
""" To create an asynchronous coroutine that w takes in an integer argument """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
   
    new_rand = random.uniform(0, max_delay)
    await asyncio.sleep(new_rand)
    return new_rand
