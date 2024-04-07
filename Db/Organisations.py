def getOrganisations(db):
    coll = db.Organisations
    data = []
    for i in coll.find():
        data.append(i)
    return data

def getOrg(db,org):
    coll = db.Organisations
    return coll.find_one({"organisation":org})
