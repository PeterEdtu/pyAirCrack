import os
import subprocess
import csv
import pandas
from io import StringIO

def execute(cmd):
    return subprocess.check_output(cmd.split(" ")).decode('utf-8').replace("\t", ",").replace(",,", ",")

def csv_convert(l):
    return pandas.read_csv(StringIO(l), delimiter=',')

#os.system("echo Start pyAirCrack") # Run with visible result

print("pyAirCrack is starting...")

# Get the first interface
l_interfaces = execute("sudo airmon-ng")
l_interfaces = csv_convert(l_interfaces).Interface
w_interface = l_interfaces[0]
print("{} interface(s) identified.".format(len(l_interfaces)))
print("{} is used.".format(w_interface))

print("Killing trouble processes...")
l_tprocesses = execute("sudo airmon-ng check kill")
print(l_tprocesses)
# TODO: Get the processes for relaunch

print("Starting monitoring mode...")
execute("sudo airmon-ng start {}".format(w_interface))

if "mon" not in w_interface:
    w_interface = w_interface+"mon"

# Waiting for the monitoring to be done (hidden)
m_result = execute("sudo airodump-ng {}".format(w_interface))
print(m_result)

# Active monitoring (visible)
#os.system("sudo airodump-ng {}".format(w_interface))

print("THIS SCRIPT IS NOT DONE YET.")