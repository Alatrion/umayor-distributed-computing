import requests
import json
import math

valor_inicial = 1
valor_final = 32
total_valores = valor_final - valor_inicial
total_nodos = 16
steps = math.ceil(total_valores/total_nodos) # redondear hacia arriba
print(steps)

lista = list(range(valor_inicial, valor_final, steps))

import aiohttp
import asyncio

ran = list(range(1,total_nodos))
ran.append(total_nodos)
#results = []

async def get_values():
    async with aiohttp.ClientSession() as session:
        for i in ran:
            print(i)
            async with session.post('http://localhost:{}{}/sum-range'.format('30',(str(i-1).zfill(2))), data={'starting_number': str(lista[i-1]), 'ending_number': str(lista[i])}) as resp:
                print(await resp.text())
                #results.append(await resp.json())
        #return results

asyncio.run(get_values())
