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
    updatedataFromJson()

    if checkExistUsername(user) == False: 
        return 'Username does not found!'  # k tồn tại username
    elif checkUserPassword(user) == False: 
        return 'Your password is incorrect!'  # k đúng password
    else: return 'Logged in successfully!'

def createNewUser(user):
    updatedataFromJson()

    if checkExistUsername(user) == False:
        arr['users'].append(user)
        newF = open('data.json',"w")
        newF.write(json.dumps(arr))
        newF.close() # done :3 cần tối ưu để check file json dễ hơn, htại chỉ hiển thị trên 1 dòng -> rối mắt vcl
        return True # tạo user thành công
    else: return False # tạo user thất bại (đã tồn tại username trong json)

def searchDefault(searchType, inpStr):
    updatedataFromJson()
    returnArr = []
    for i in arr['books']:
        if searchType == 'id':
            i['id'] = str(i['id'])
        if i[searchType].startswith(inpStr):
            i['id'] = int(i['id'])
            returnArr.append(i)
    if returnArr == []: return False # return False nếu k tìm thấy
    else: return returnArr  # return Arr nếu tồn tại kquả

def searchBook(inpStr):
    arr = inpStr.split(' ', 1)
    for i in range(len(arr)):
        arr[i] = arr[i].strip().replace('"', '')
    if arr[0] == "F_ID":        arr[1] = arr[1].replace(' ', '')
    if arr[0] == "":            return False   #sai cú pháp search (khoảng trắng ở đầu )
    elif arr[0] == "F_ID":      return searchByID(arr[1])
    elif arr[0] == "F_Name":    return searchByName(arr[1])
    elif arr[0] == "F_Type":    return searchByType(arr[1])
    elif arr[0] == "F_Author":  return searchByAuthor(arr[1])

def searchByID(ID):
    return searchDefault('id', ID)

def searchByName(name):
    return searchDefault('name', name)

def searchByType(type):
    return searchDefault('type', type)

def searchByAuthor(author):
    return searchDefault('author', author)

import json
arr = 0
def updatedataFromJson():
    global arr
    f = open('data.json', "r")
    arr = json.loads(f.read())
    f.close()
    


########## test down this line ##########

#print(searchBook("F_ID 1"))
