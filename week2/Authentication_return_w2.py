import getpass

userPass= {'victor':12345, 'bryan':67890, 'alejandro' : 12345 }
userRole={'victor': 'User', 'bryan': 'Developer', 'alejandro': 'Admin'}

def logIn(user,paw):
 role="Role not defined"
 if user in userPass.keys() and paw == userPass[user]:
     role=userRole[user]
     return True, role
 else:
       return False, role
     
user=input("user: ")
pw=int(getpass.getpass("Password:"))

print(logIn(user,pw))