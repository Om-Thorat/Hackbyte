import uuid
import hashlib

def hashText(text):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt

def matchHashedText(hashedText, providedText):
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()

def InsertUser(user,db):
    coll = db.Users
    pas = user['userinfo']['aud'];
    print(pas)
    hashed = hashlib.sha256(pas.encode("utf-8")).hexdigest()
    # print(hashed)
    Orgs = db.Organisations
    res = Orgs.find({"organisation": user['userinfo']['email'].split('@')[1].split('.')[0]});
    if(res.count() > 0):
        return
    else:
        NewOrg = {
            "organisation": user['userinfo']['email'].split('@')[1].split('.')[0],
            "rating1": 0,
            "rating2": 0,
            "usersrated": 0,
            "overview": "" 
        }
        print(NewOrg,Orgs)
        Orgs.insert_one(NewOrg);
    res = coll.find({"hash": hashed});
    # print(res.count())
    if(res.count() > 0):
        return
    else:
        NewUser = {
            "username": "coool",
            "organisation": user['userinfo']['email'].split('@')[1].split('.')[0],
            "rating1" : 0,
            "rating2" : 0,
            "lastrated": 0,
            "hash": hashed
        }
        coll.insert_one(NewUser)


