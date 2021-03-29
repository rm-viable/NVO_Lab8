import os
import paramiko
import time

def netcheck():
    x = os.popen('openstack network list').read()
    y = []
    n = 6
    for items in x.split('|'):
        try:
            y.append(x.split('|')[n])
            n += 4
        except:
            pass        
    y = [item.strip() for item in y]

    return y


def avail_floating_ip_list_check():
    x = os.popen('openstack floating ip list --status DOWN').read()
    y = x.split(' ')
    floating_ip_list = []
    for items in y:
        if items.count('.') == 3:
            floating_ip_list.append(items)
    print('\n******************************************************************')
    print('Please check below list for the available floating IPs')
    print(floating_ip_list)
    print('******************************************************************\n')


def instance_creation():
    net_list = netcheck()
    instance_name = input("\n*** Please enter the new instance name: ")
    floating_ip = input("*** Please enter the floating ip to be associated: ")
    print('*** Available networks are: {}'.format(net_list))
    net_id = input("Please enter the network id or ids to be associated: ")
    print('\n')
    create_net = os.popen('openstack server create --flavor m1.tiny --image cirros-0.5.2-x86_64-disk --key-name rmkey --network {} {}'.format(net_id,instance_name)).read()
    print('\n*** Instance created! ')
    create_net = os.popen('openstack server add floating ip {} {}'.format(instance_name,floating_ip)).read()
    print('\n*** Floating IP associated to the instance.')
    print('*** Calling the connectivity checker to login to instance and check reachability from host and to the internet ...')
    time.sleep(30)
    
    print('\n******************************************************************')
    print('*** Host VM connectivity report is ready!')
    runSshCmd(floating_ip, "cirros", "gocubsgo", "ping 172.24.4.1 -c 4")
    print('******************************************************************\n')

    print('\n******************************************************************')
    print('*** Internet connectivity report is ready!')
    runSshCmd(floating_ip, "cirros", "gocubsgo", "ping 8.8.8.8 -c 4")
    print('******************************************************************\n')


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

avail_floating_ip_list_check()
instance_creation()
