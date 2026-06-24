import time
import os
from colorama import init, Fore, Style
import net.minecraft.world.level.Level as Level
import net.minecraft.resources.DataLocation as DataLocation

init(autoreset=True)
log = ""
environment = "Main"
base_path = os.path.join(os.environ[DataLocation.get_save_system()], ".minecraft-py")
if Level.isClient:
    log_path = os.path.join(base_path, "log/client")
else:
    log_path = os.path.join(base_path, "log/server")
os.makedirs(log_path, exist_ok=True)
full_path = os.path.join(log_path, "latest.log")


def set_environment(name):
    global environment
    environment = name


def get_timestamp(color=True):
    z = time.localtime()
    hour = str(z.tm_hour).zfill(2)
    min_ = str(z.tm_min).zfill(2)
    sec = str(z.tm_sec).zfill(2)
    if color==True:
        return f"{Fore.CYAN}[{hour}:{min_}:{sec}]{Style.RESET_ALL}"
    else:
        return f"[{hour}:{min_}:{sec}]"


def write_log(strip):
    global log
    log += strip + "\n"
    try:
        with open(full_path, "w") as file:
            file.write(log)
    except Exception as e:
        print(f"Falied to write log file: {e}")


def info(text, programname="minecraft"):
    strip = f"{get_timestamp()} {Fore.GREEN}[{environment}/INFO]{Style.RESET_ALL} {Fore.BLUE}({programname}){Style.RESET_ALL} {text}"
    print(strip)
    strip_ = f"{get_timestamp(False)} [{environment}/INFO] ({programname}) {text}"
    write_log(strip_)


def error(text, programname="minecraft"):
    strip = f"{get_timestamp()} {Fore.RED}[{environment}/ERROR] ({programname}) {text}{Style.RESET_ALL}"
    print(strip)
    strip_ = f"{get_timestamp(False)} [{environment}/ERROR] ({programname}) {text}"
    write_log(strip_)


def warning(text, programname="minecraft"):
    strip = f"{get_timestamp()} {Fore.YELLOW}[{environment}/WARNING] ({programname}) {text}{Style.RESET_ALL}"
    print(strip)
    strip_ = f"{get_timestamp(False)} [{environment}/WARNING] ({programname}) {text}"
    write_log(strip_)
