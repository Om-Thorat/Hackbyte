def getOrganisations(db):
    coll = db.Organisations
    data = []
    for i in coll.find():
        data.append(i)
    return data