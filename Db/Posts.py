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

def getOrgPosts(db,user):
    coll = db.Posts
    posts = []
    for i in coll.aggregate([
        { "$match": { "type": user['userinfo']['email'].split('@')[1].split('.')[0] } },
        { "$sort": { "likes": -1 } }
    ]):
        posts.append(i)
    return posts

def getOrgPublic(db,org):
    coll = db.Posts
    posts = []
    print(org)
    for i in coll.find({ "type": "world", "organisation": org}):
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

def searchPost(db,q):
    coll = db.Posts
    posts = []
    for i in coll.aggregate([
        {
            "$search": {
                "text": {
                    "query": q,
                    "path": ["text",
                             "title",
                             "organisation"],
                    "fuzzy": {}
                }
            }
        }
    ]):
        posts.append(i)
    print(posts)
    return posts