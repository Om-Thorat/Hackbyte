def getPosts(db):
    coll = db.Posts
    posts = []
    for i in coll.find():
        print(i)
        posts.append(i)
    return posts