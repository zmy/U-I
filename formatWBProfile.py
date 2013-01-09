import pickle


wbProFilePath = 'weibo.profile.p'
wbProfile = pickle.load(open(wbProFilePath, 'rb'))
newProfile = {}
for wbID, profile in wbProfile.items():
    newProfile[wbID] = {}
    for key, value in profile.items():
        if value.strip()!='':
            newProfile[wbID][key.strip()] = value.strip()
pickle.dump(newProfile, open(wbProFilePath, 'wb'))
