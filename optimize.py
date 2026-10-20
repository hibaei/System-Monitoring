import psutil
import subprocess
def adjust_priority(pid, priority):
 try:
  subprocess.run(['renice', str(priority), str(pid)], check=True)
  print(f"Ajusted priority for PID {pid} to {priority}")
 except subprocess.CalledProcessError as e:
  print(f"Error adjusting priority: {e}")
for proc in psutil.process_iter(['pid','name','cpu_percent']):
 if proc.info['cpu_percent'] > 80:
  adjust_priority(proc.info['pid'],19) 
