def checkUsername(newUser):
    user_str = newUser['username']
    for i in arr['user']:
        if user_str == i['username']:
            return False
    arr.append(newUser) ### lỗi nha, arr[user]
    return True

def checkLogin(user):
    username = user['username']
    password = user['password']
    for i in arr['users']:
        if username == i['username']:
            if password == i['password']:
                err = 0
                break
            else: 
                err = 1
                break
        else: err = 2
    if err == 1: print('Your password is incorrect!')
    elif err == 2: print('Username does not found!')
    else: print('Login successfully!')

def checkInputType(inp):
   if inp.strip().isdigit(): return False
   else: return True

def searchDefault(searchType, inpStr):
    if checkInputType(inpStr):
        returnArr = []
        for i in arr['books']:
            if i[searchType].startswith(inpStr):
                returnArr.append(i)
        if returnArr == []: return False
        else: return returnArr
    else: return False

def searchByName(name):
    return searchDefault('name', name)

def searchByID(ID):
    return searchDefault('id', ID)

def searchByType(type):
    return searchDefault('type', type)

def searchByAuthor(author):
    return searchDefault('author', author)

import json

f = open('data.json', "r")
arr = json.loads(f.read())
newArr = []

user = {}
user['username'] = '123'
user['password'] = '123'

book = {}
book['id'] = 1
book['name'] = 'admin'
book['author'] = 'admin'
book['type'] = 'admin'

x = searchByName(book['name'])
for i in x:
    print('ID: ' + i['id'])
    print('Name: ' + i['name'])
    print('Type: ' + i['type'])
    print('Author: ' + i['author'])
    print('\n')