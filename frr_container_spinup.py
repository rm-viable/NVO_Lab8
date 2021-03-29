import os
name_frr = input("Please enter the name of your choice for the FRR container: ")

create_frr = os.popen('sudo docker run --rm -it --privileged --name {} sflow/frr'.format(name_frr)).read()
#print(create_frr)
print('\n******************************************************************')
print('FRR container spun up with name {}'.format(name_frr))
print('******************************************************************')