import requests
import json
import math
import aiohttp
import asyncio
import time 


valor_inicial = 1
valor_final = 32
total_valores = valor_final - valor_inicial
total_nodos = 4
steps = math.ceil(total_valores/total_nodos) # redondear hacia arriba
print(steps)

lista = list(range(valor_inicial, valor_final, steps))


ran = list(range(1,total_nodos))
ran.append(total_nodos)
results = []

start_time = time.time()

async def get_sum_range_response(session, i):
    if i == ran[-1]:
        async with session.post('http://localhost:{}{}/sum-range'.format('30',(str(i-1).zfill(2))), data={'starting_number': str(lista[i-1]), 'ending_number': str(valor_final)}) as resp:
            results.append(await resp.text())
    else:                
        async with session.post('http://localhost:{}{}/sum-range'.format('30',(str(i-1).zfill(2))), data={'starting_number': str(lista[i-1]), 'ending_number': str(lista[i])}) as resp:
            results.append(await resp.text())

async def get_values():
    async with aiohttp.ClientSession() as session:
        tasks = [get_sum_range_response(session, i) for i in ran]
        await asyncio.gather(*tasks)

asyncio.run(get_values())
current_time = time.time() - start_time
print("--- %s seconds ---" % (current_time))

async def get_sum_response(session, i, number_list, new_number_list):
    req = requests.post('http://localhost:{}{}/sum'.format('30',(str(i-1).zfill(2))),
                            {'num1': str(number_list[i-1]), 'num2': str(number_list[i])})
    new_number_list.append(int(req.text))

async def sum_iterations(number_list, current_nodes):
    if len(number_list) == 1:
        return number_list
    print("+++++", current_nodes)
    print("-----", number_list)
    current_layer = list(range(1,current_nodes,math.ceil(current_nodes/(len(number_list)/2))))
    new_number_list = []
    print(current_layer)
    async with aiohttp.ClientSession() as session:
        tasks = [get_sum_response(session, i, number_list, new_number_list) for i in current_layer]
        await asyncio.gather(*tasks)
    return(new_number_list)

number_list = results
while (len(number_list) != 1):
    number_list = asyncio.run(sum_iterations(number_list, total_nodos))
    current_time = time.time() - current_time
    print("--- %s seconds ---" % (current_time))
print(number_list)