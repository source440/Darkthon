import threading
import subprocess

def run_server():
    subprocess.run(["python3", "server.py"])

def run_bot():
    subprocess.run(["python3", "-m", "Tepthon"])

# تشغيل السيرفر في ثريد منفصل
threading.Thread(target=run_server).start()

# تشغيل البوت
run_bot()
