## Simple script to ping a set of IPs and return the results

import os
import time

with open('host.txt') as f:
	hosts = f.readlines()

	for host in hosts:
		host = host.strip()
		print('Pinging ' + host + '...')
		response = os.system('ping -c 2 ' + host)

		if response == 0:
			print('\n' + host + ' is up!')
			print('_' * 30)
		else:
			print('\n' + host + ' is up!')
			print('_' * 30)
		time.sleep(3)