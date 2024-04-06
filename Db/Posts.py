import time 

def getPosts(db,user):
    coll = db.Posts
    posts = []
    if(not user):
        for i in coll.aggregate([
            { "$match": { "type": "world" } },
            { "$sort": { "likes": -1 } }
        ]):
            posts.append(i)
        return posts
    else:
        for i in coll.aggregate([
            { "$match": { "type": { "$in": ["world", user['userinfo']['email'].split('@')[1].split('.')[0]] } } },
            { "$sort": { "likes": -1 } }
        ]):
            posts.append(i)
        return posts



def InsertPost(db,title,body,tags,type,user):
    coll = db.Posts
    # print(time.time())
    coll.insert({
        "text": body,
        "title": title,
        "tags": tags.split(","),
        "type":type,
        "likes": 0,
        "time": time.time()*1000,
        "organisation": user['userinfo']['email'].split('@')[1].split('.')[0]
    })
