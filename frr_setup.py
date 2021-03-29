import os

bgp_config = os.popen("sudo docker exec -it abcd vtysh -c enable -c 'config term' -c 'router bgp 65000' -c 'neighbor 172.17.0.3 remote-as 65001' -c 'end' -c 'wr'").read()

print(bgp_config)
