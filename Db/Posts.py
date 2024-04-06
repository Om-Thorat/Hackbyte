import time 

def getPosts(db,user):
    coll = db.Posts
    posts = []
    if(not user):
        for i in coll.find({"type":"world"}):
            print(i)
            posts.append(i)
        return posts
    else:
        for i in coll.find({"type" : { "$in": ["world", user['userinfo']['email'].split('@')[1].split('.')[0]] }}):
            posts.append(i)
        return posts



def InsertPost(db,title,body,tags,type):
    coll = db.Posts
    coll.insert({
        "text": body,
        "title": title,
        "tags": tags.split("-"),
        "type":type,
        "likes": 0,
        "time": time.time()
    })
