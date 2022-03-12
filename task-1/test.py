import requests
import json
import math

valor_inicial = 1
valor_final = 32
total_valores = valor_final - valor_inicial
total_nodos = 4
steps = math.ceil(total_valores/total_nodos) # redondear hacia arriba
print(steps)

lista = list(range(valor_inicial, valor_final, steps))

import aiohttp
import asyncio

ran = list(range(1,total_nodos))
ran.append(total_nodos)
#results = []

async def get_response(session, i):
    if i == ran[-1]: #155050
        async with session.post('http://localhost:{}{}/sum-range'.format('30',(str(i-1).zfill(2))), data={'starting_number': str(lista[i-1]), 'ending_number': str(valor_final)}) as resp:
            print(await resp.text())
    else:                
        async with session.post('http://localhost:{}{}/sum-range'.format('30',(str(i-1).zfill(2))), data={'starting_number': str(lista[i-1]), 'ending_number': str(lista[i])}) as resp:
            print(await resp.text())

async def get_values():
    async with aiohttp.ClientSession() as session:
        tasks = [get_response(session, i) for i in ran]
        await asyncio.gather(*tasks)
#        for i in ran:
#            print(i)


asyncio.run(get_values())
