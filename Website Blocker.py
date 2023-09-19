import os
import sys
import ctypes

def run_as_admin():
    # Re-run the script with administrator privileges
    if sys.platform == 'win32':
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    else:
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

def block_websites():
    websites_to_block = [
        "www.example.com"
        # Add more websites as needed
    ]

    hosts_path = '/etc/hosts' if sys.platform != 'win32' else r"C:\Windows\System32\drivers\etc\hosts"

    redirect_ip = "127.0.0.1"

    try:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in websites_to_block:
                if website not in content:
                    file.write(redirect_ip + " " + website + "\n")
        print("Websites blocked successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if os.name != 'posix' and not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script requires administrator privileges to block websites.")
        run_as_admin()
    else:
        block_websites()
