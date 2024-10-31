# SSH-Login-Brute-Forcing

## Disclaimer

_This script demonstrates a basic brute-force technique intended for educational purposes and authorized penetration testing only._ 

_**Unauthorized use of this script is illegal and unethical**._ 

_By using this script, you agree to the following:_

_- You have explicit permission to test the system in question._

_- You will not use this script against any system that you do not own or manage._

_- You understand the legal implications of unauthorized access and agree to take full responsibility for your actions._

_Always prioritize ethical practices in cybersecurity. If you're unsure about the legality of your actions, please consult with a legal professional._

<br>

## Screenshots:

<img width="310" alt="2024-10-31 01_53_44-Grammarly Web UI" src="https://github.com/user-attachments/assets/ecbcb987-0f66-4bd1-8b23-e658345db70f">  <img width="250" alt="2024-10-31 01_56_28-kali-linux-2024 3 - VMware Workstation" src="https://github.com/user-attachments/assets/9d3f76ed-521c-46ea-b7fb-1a0009039eac">


<br>

## Steps to perform password Brute Forcing using the provided script:

#### Step 1: Make sure pwntools is installed in your Kali Linux Virtual Machine.
    sudo apt-get install python3-pwntools 
<br>

#### Step 2: Make use of your own wordlist.
<br>

#### Step 3:  Make sure SSH service  is enabled on your Kali Machine:
      sudo systemctl start ssh
<br>

## Detailed overview of how to write the script:
#### 1. Import required libraries: 'pwn' for SSH connections and 'paramiko' for handling SSH exceptions.
<br>

#### 2. Set up variables:
     'host': The target IP address (in this case, localhost)
     'username': The username to attempt login with (set to "kali")
     'attempts': A counter to keep track of login attempts
<br>

#### 3. Open the password list file ("/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-100.txt") in read mode.
<br>

#### 4. Iterate through each password in the file:
    Strip newline characters from the password
    Print the current attempt number and password being tried
<br>

#### 5. Attempt an SSH connection using the current password:
    If successful, print the valid password and break the loop
    If unsuccessful, catch the AuthenticationException and print "Invalid Password!"
<br>

#### 6. Increment the attempt counter and continue to the next password.


