import re

"""def check(password):
    
    if (len(password) < 8):
        return "Invalid Format!"
    
    elif not re.search(r"[a-z]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[A-Z]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[0-9]", password):
        return "Invalid Format!"
    
    elif not re.search(r"[_@$]", password):
        return "Invalid Format!"
    
    elif re.search(r"\s", password):
        return "Invalid Format!"
    
    else:
        return "Valid Format!"
 

print(check("A1!a"))"""

"""def validity(string):
    pattern = r'^[a-zA-Z]+(.*)[a-zA-Z0-9]$'

    if re.search(r'[!@#$%^&*()_]+',string):
        return "Invalid Format! Inclusion of special character."

    if re.findall(r'\s',string) != []:
        return "Invalid Format! Inclusion of white space."

    if re.match(pattern,string):
        return "Valid Format!"
    else:
        return "Invalid Format!"

string = input("Enter string: ")
print(validity(string))"""

"""def binary(num):
    pattern = re.compile(r'(^([01]+)([01\s]*)([01]*)$){1,}')

    if match := pattern.match(num):
        return "Valid Binary Format"

    else:
        return "Invalid Format!"

num = input("Enter binary number: ")
print(binary(num))"""


# Password checking - single exp
def pwd_single(passwd):

	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&]){6,20}$"

	pat = re.compile(reg)
	mat = re.search(pat, passwd)
	if mat:
		print("Password is valid.")
	else:
		print("Password invalid !!")


if __name__ == '__main__':
	pwd_single("1!a123A")
