import paramiko
import time
from selenium import webdriver

def get_html_file(link, chrome_driver_path, cloud_user, cloud_pass):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.cloudlab.us/login.php")

    username = driver.find_element_by_name("uid")
    password = driver.find_element_by_name("password")
    username.send_keys(cloud_user)
    password.send_keys(cloud_pass)
    driver.find_element_by_id("quickvm_login_modal_button").click()

    driver.get(link)
    time.sleep(3)

    with open("exp.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

# Input: Path of the html file of the list view CloudLab webpage
# Output: A list of addresses
def get_ips(html_path):
  html_file = html_path
  with open(html_file, "r") as fp:
    lines = fp.readlines()

  login = "error"
  for line in lines:
    if "window.LOGINUID" in line:
      login = line.split("'")[1]
      break

  if login == "error":
    print("Wrong HTML File")

  target_string = "ssh://" + login + "@"
  address_list = []
  for line in lines:
    if target_string in line:
      address = line.split('@')[1].split(':')[0]
      address_list.append(address)

  return address_list

# Runs all of the ssh commands for a machine
# Input: The target machine's IP
# Note: Fill in the correct key file here: paramiko.RSAKey.from_private_key_file(r"C:\Users\Jagan\Documents\sshkeys\privkey")
def run_ssh_commands(ip, priv_key_file, username):
    paramiko.util.log_to_file("log_" + ip + ".txt")

    ssh = paramiko.SSHClient()
    k = paramiko.RSAKey.from_private_key_file(priv_key_file)

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = username
    ssh.connect(hostname=ip, username=user, pkey=k)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mkdir testing_dir_b")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("pwd > temp.txt")

    with open("commands_b.txt", 'r') as fp:
        cmnds = fp.read().splitlines()

    print(cmnds)

    for item in cmnds:
        test_command = ""
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(item)
        if "nohup" in item:
            time.sleep(3)
            ssh.close()
            del ssh, ssh_stdin, ssh_stdout, ssh_stderr
            return
        stdout = []
        stderr = []
        for line in ssh_stderr:
            stdout.append(line.strip())
            stderr.append(line)

        print("The command was: " + item)
        print("The output is: " + str(stdout))
        print("")


    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mkdir testing_dir_g")
    ssh.close()
    del ssh, ssh_stdin, ssh_stdout, ssh_stderr

# Function used for debugging: It runs a single command as set in the item variable
# Inputs: the IP of the target machine
def run_single_commands(ip):
    paramiko.util.log_to_file("log_" + ip + ".txt")

    ssh = paramiko.SSHClient()
    k = paramiko.RSAKey.from_private_key_file(r"C:\Users\Jagan\Documents\sshkeys\privkey")

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = "krish133"
    ssh.connect(hostname=ip, username=user, pkey=k)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mkdir testing_dir_b")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("pwd > temp.txt")

    with open("commands.txt", 'r') as fp:
        cmnds = fp.read().splitlines()

    print(cmnds)

    item = r"source /users/krish133/.bashrc;cd /opt/puffer/emulation;python working_end_to_end.py one-trace-google/ ../src/puffer_settings.yml 152 TrainPhaseMPC"
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(item)
    exit_status = ssh_stdout.channel.recv_exit_status()
    if exit_status == 0:
        print("File Deleted")
    else:
        print("Error", exit_status)
    stdout = []
    stderr = []
    for line in ssh_stderr:
        stdout.append(line.strip())
        stderr.append(line)

    print("The command was: " + item)
    print("The output is: " + str(stdout))
    print("")


    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("mkdir testing_dir_g")
    ssh.close()
    del ssh, ssh_stdin, ssh_stdout, ssh_stderr

def main():
    #uncomment the relevant section

    chrome_driver_path = r'C:\Users\Jagan\Documents\ECE 29401\puffercloud\chromedriver.exe'
    cloud_user = "krish133"
    cloud_pass = "<Enter Password>"
    link = "https://www.cloudlab.us/status.php?uuid=ff65e30d-3ba8-11ec-84f8-e4434b2381fc"
    html_file = r"exp.html" # Only change if providing a custom html file and not using selenium
    priv_key_file = r"C:\Users\Jagan\Documents\sshkeys\privkey"
    ssh_username = "krish133"

    # This section downloads the html file with ip addresses from CloudLab
    get_html_file(link, chrome_driver_path, cloud_user, cloud_pass)

    # This section parses the html file to get the address list
    address_list = get_ips(html_file)
    print(address_list)

    # Flow to run commands on a single machine
    print(address_list[4])
    run_ssh_commands(address_list[4], priv_key_file, ssh_username)
    # run_single_commands(address_list[3])

    # Flow to run all commands on all machines
    # for item in address_list:
    #     run_ssh_commands(item, priv_key_file, username)
    # print("finished")



if __name__ == "__main__":
    main()
