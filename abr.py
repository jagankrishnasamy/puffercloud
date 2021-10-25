import paramiko

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

def run_ssh_commands(ip):
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

    for item in cmnds:
        test_command = ""
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
    html_file = r"exp.html"
    address_list = get_ips(html_file)
    print(address_list[1])
    run_ssh_commands(address_list[1])
    # for item in address_list:
    #     run_ssh_commands(item)
    # print("finished")



if __name__ == "__main__":
    main()
