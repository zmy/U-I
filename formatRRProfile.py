import re
import pickle


rrProFilePath = 'renren.profile.p'
rrProfile = pickle.load(open(rrProFilePath, 'rb'))
newProfile = {}
for rrID, profile in rrProfile.items():
    newProfile[rrID] = {}
    for key, value in profile.items():
        if key!='工作信息' and value.strip()!='':
            if key=='生日':
                value = re.sub(r'\S*座', '', value)
                value = re.sub(r'\s', '', value)
            newProfile[rrID][key.strip()] = value.strip()
pickle.dump(newProfile, open(rrProFilePath, 'wb'))
