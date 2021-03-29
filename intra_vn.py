import os
import paramiko
import time

def runSshCmd(hostname, username, password, cmd, timeout=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password,
            allow_agent=False, look_for_keys=False, timeout=timeout)
    stdin, stdout, stderr = client.exec_command(cmd)
    data = stdout.read()
    packet_lost = str(data).split(',')[-1].split('\\')[0][0:4]
    print('Packet loss percentage is: {}'.format(packet_lost))
    resp = str(data).split(',')[-1].split('\\')[1][1:]
    print('Response details: {}'.format(resp))
    #print(client)
    client.close()

def disable_port_security():
    print('Please enter the name of the instance and the IP address of the interface to disable port security.')
    name_instance = input("Please enter the name of the instance: ")
    ip_instance = input("Please enter the IP address of the interface: ")
    print('\n')
    x = os.popen('openstack port list --server {} | grep {}'.format(name_instance,ip_instance)).read()
    y = x.split(' ')
    if_id = y[1]
    print('\n*** Disabling port security...')
    #first disable security group
    disable_sec_group = os.popen('openstack port set  --no-security-group {}'.format(if_id)).read()
    #then disable port security
    disable_port_sec = os.popen('openstack port set --disable-port-security {}'.format(if_id)).read()
    print('\n*** Port security disabled!')

port_disable_qty = input("Please enter the number of interfaces to be disabled: ")
count = 0
while count != int(port_disable_qty):
    disable_port_security()
    count += 1
    
print('\n*** The reachability between instances check will begin now...')
floating_ip = input("Please enter the floating ip of one of the server for SSH: ")
ping_ip = input("Please enter the ip of the other server for ping: ")
print('\n******************************************************************')
runSshCmd(floating_ip, "cirros", "gocubsgo", "ping {} -c 4".format(ping_ip))
print('******************************************************************\n')

