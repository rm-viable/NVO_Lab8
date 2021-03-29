import os
name_sdn = input("Please enter the name of your choice for the RYU SDN container: ")

create_sdn = os.popen('sudo docker run -it --name {} -d osrg/ryu'.format(name_sdn)).read()
#print(create_sdn)
print('\n******************************************************************')
print('RYU SDN container spun up with name {}'.format(name_sdn))
print('******************************************************************')