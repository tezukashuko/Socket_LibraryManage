def checkExistUsername(user):
    user_str = user['username']
    for i in arr['users']:
        if user_str == i['username']:
            return True # đã tồn tại
    return False # k tồn tại

def checkUserPassword(user):
    for i in arr['users']:
        if user['username'] == i['username'] and user['password'] == i['password']:
            return True # đúng password
    else: return False # sai password

def checkLogin(user):
    err = 0
    if not checkExistUsername(user): err = 1   # k tồn tại username
    elif not checkUserPassword(user): err = 2  # k đúng password
    if err == 1: print('Username does not found!')
    elif err == 2: print('Your password is incorrect!')
    else: print('Login successfully!')

def createNewUser(user):
    if not checkExistUsername(user):
       # arr['users'].append(user)
       # newF = open('data.json',"w")
       # newF.write(json.dumps(arr['users']))
       # newF.close()
       # write = rewrite toàn bộ file json, ch tối ưu
        return True # tạo user thành công
    else: return False # tạo user thất bại

def checkInputType(inp):
   if inp.strip().isdigit(): return False  # inp là số -> False
   else: return True  # inp là str -> True

def searchDefault(searchType, inpStr):
    if checkInputType(inpStr):
        returnArr = []
        for i in arr['books']:
            if i[searchType].startswith(inpStr):
                returnArr.append(i)
        if returnArr == []: return False
        else: return returnArr  # return Arr nếu tồn tại kquả
    else: return False  # return False nếu k tìm thấy

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

user = {}
user['username'] = '123'
user['password'] = '123'

createNewUser(user)
print('\n')

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

f.close()