import os

create_sdn = os.popen('sudo docker run -it --name commander_bone -d osrg/ryu').read()
print(create_sdn)

print('*** Copying the required config files for BGP at the SDN controller...')
create_sdn = os.popen('sudo docker cp bgp_sdn_frr.py crypton:/root/ryu/ryu/services/protocols/bgp/bgp_sdn_frr.py').read()

print('*** BGP ready at the controller end')


create_sdn = os.popen('sudo docker exec -it commander_bone bash -c "cd ryu/ryu/services/protocols/bgp" -c "ryu-manager application.py --bgp-app-config-file bgp_sdn_frr.py"').read()
print(create_sdn)
