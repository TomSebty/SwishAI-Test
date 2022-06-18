import cpuinfo
from fastapi import FastAPI
from datetime import datetime
import requests
import socket
from psutil import net_if_addrs, cpu_count, virtual_memory
import GPUtil

app = FastAPI()

def get_sys_info():
	cpu = cpuinfo.get_cpu_info()['brand_raw']
	cores = cpu_count()
	if GPUtil.getGPUs():
		gpu = GPUtil.getGPUs()[0].name 
	else:
		gpu =  "No GPU Found"
	time = datetime.utcnow()
	local_ip = socket.gethostbyname(socket.gethostname())
	external_ip = get_external_ip()
	memory = format(virtual_memory().total/(1024**2), ".2f")
	return cpu, cores, gpu, time, local_ip, external_ip, memory

def get_external_ip():
	resp = requests.get("https://ident.me/", timeout=10)
	if resp:
		return resp.text
	else:
		return "Cannot access ident.me"

@app.get("/")
async def root():
	print("Hello World")
	cpu, cores, gpu, time, local_ip, external_ip, memory = get_sys_info()
	return {"cpu": cpu,
			"cores": cores,
			"gpu": gpu,
			"time_utc": time, 
			"local_ip": local_ip,
			"external_ip": external_ip,
			"memory": "{} MB".format(memory)}
