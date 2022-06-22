import subprocess
import os
active_servers = []
inactive_servers = []
with open(os.devnull, "wb") as limbo:
    for n in range(0, 254):
        ip = "10.0.50.{0}".format(n)
        result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                                  stdout=limbo, stderr=limbo).wait()
        if result:
            inactive_servers.append(ip)
            #print(inactive_servers)
        else:
            active_servers.append(ip)
            print(active_servers)
