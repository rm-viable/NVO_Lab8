import os
net_id = input("Please enter the new network id: ")
subnet_id = input("Please enter the new subnet id: ")
subnet_range = input("Please enter the new subnet range: ")
router_id = input("Please enter the router id: ")

create_net = os.popen('openstack network create {}'.format(net_id)).read()
#print(create_net)
print('\n******************************************************************')
print('Network with net id {} is created'.format(net_id))
print('******************************************************************')

create_subnet = os.popen('openstack subnet create {} --network {}  --subnet-range {}'.format(subnet_id,net_id,subnet_range)).read()
#print(create_subnet)
print('\n******************************************************************')
print('Subnet with subnet id {} has joined network {}'.format(subnet_id,net_id))
print('******************************************************************')

connect_router = os.popen('openstack router add subnet {} {}'.format(router_id,subnet_id)).read()
#print(connect_router)
print('\n******************************************************************')
print('Subnet with subnet id {} has joined router {}'.format(subnet_id,router_id))
print('******************************************************************')

