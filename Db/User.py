def InsertUser(user,db):
    coll = db.Users
    NewUser = {
        "username": "bruh",
        "organisation": user['userinfo']['email'].split('@')[1].split('.')[0],
        "rating1" : 0,
        "rating2" : 0,
        "lastrated": 0
    }
    coll.insert_one(NewUser)


