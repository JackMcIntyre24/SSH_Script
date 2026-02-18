import subprocess
# Author: Jack McIntyre
# Date: 2/17/2026
#
# This short program that checks to see if a user has an ssh key
# and then prompts them to create one if they don't have one
check_key_command = 'cd ~/.ssh ; ls'

result = subprocess.run(
    ["powershell", "-Command", check_key_command],
    capture_output=True, 
    text=True,           
    check=True           
)

# Check to see if commond ssh key ending exists
if "id_ed25519.pub" in result.stdout.strip():
    print(f"id_ed25519.pub key found!")
    exit()
elif "id_rsa.pub" in result.stdout.strip():
    print(f" id_rsa.pub key found!")
    exit()
elif "id_ecdsa.pub" in result.stdout.strip():
    print(f" id_ecdsa.pub key found!")
    exit()
else:
    print("key was either not recognized or doesn't exist")

# Retrieve input from user    
print("Would you like to create one? [y/n]")
user_input = input()

# if yes, turn over terminal to create key
if(user_input == "y"):
    command2 = 'ssh-keygen'
    
    print()
    result1 = subprocess.run(
        ["powershell", "-Command", command2],
        text=True,          
        check=True          
    )
else:
    exit()