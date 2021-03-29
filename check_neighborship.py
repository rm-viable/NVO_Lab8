import os
name_frr = input("Please enter the name of the FRR container to check neighborship: ")


print('\n******************************************************************')
print('Checking neighborship...')
print('******************************************************************')

create_frr = os.popen('sudo docker exec -it {} vtysh -c "sh ip bgp neighbor" | grep Established'.format(name_frr)).read()
print(create_frr)

create_frr = os.popen('sudo docker exec -it {} vtysh -c "sh ip bgp neighbor" | grep neighbor'.format(name_frr)).read()
print(create_frr)
