import subprocess

subprocess.call("ifconfig",shell=True)
subprocess.call("sudo ifconfig enp2s0 down",shell=True)
subprocess.call("sudo ifconfig enp2s0 hw ether 00:01:04:20:02:88",shell=True)
subprocess.call("sudo ifconfig enp2s0 up",shell=True)  
subprocess.call("ifconfig ",shell=True)                                            
