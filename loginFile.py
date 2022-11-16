# names=['Kapil Rai','Puja Rai','Prisha Rai']
# usernames=['kapsrai','mathurpuja17','hob']
# passwords=['monkey','chinni@27','unicorns$01']
import json
filename = './data.json'
with open(filename,"r") as file:
    data = json.load(file)

passwords = []
usernames=[]
names=[]
for us in data['accounts']:
    usernames.append(us['username'])

for ps in data['accounts']:
    passwords.append(ps['password'])

for nm in data['accounts']:
    names.append(nm['fullName'])

def get_interface(user,password):
    name=""
    print(user,password)

    for users in usernames:
        if users == user:
            if password== passwords[usernames.index(user)]:
                name= names[usernames.index(user)]
    print(name,"this is name")
    return name

def add_new(user,password,name):
    if user != None and password !=None and name != None:
        usernames.append(user)
        passwords.append(password)
        names.append(name)
        
        data['accounts'].append({"fullName":name,"username":user,"password":password})
        with open(filename,"w") as file:
            json.dump(data,file)