import subprocess
interface= "enp2s0"
macs="00:22:55:99:66:88"
print("change the mac id "+ interface +" to "+macs)
subprocess.call(" sudo ifconfig "+ interface +" down",shell=True)
subprocess.call(" sudo ifconfig "+ interface +" hw ether "+macs,shell=True)
subprocess.call(" sudo ifconfig "+ interface +" up",shell=True)
