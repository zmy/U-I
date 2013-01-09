import difflib
import pickle


class ProfileSim:
    def __init__(self, rrProFilePath, wbProFilePath):
        #TODO: deal with junk?
        self.rrProfile = pickle.load(open(rrProFilePath, 'rb'))
        self.wbProfile = pickle.load(open(wbProFilePath, 'rb'))
        self.matcher = difflib.SequenceMatcher()

    def getRRProfile(self, rrID, key='all'):
        if key=='all':
            return self.rrProfile[rrID]
        else:
            profile = self.rrProfile[rrID]
            if key in profile:
                return profile[key]
            else:
                return None

    def getWBProfile(self, wbID, key='all'):
        if key=='all':
            return self.wbProfile[wbID]
        else:
            profile = self.wbProfile[wbID]
            if key in profile:
                return profile[key]
            else:
                return None

    def compareStr(self, strA, strB):
        self.matcher.set_seqs(strA, strB)
        return self.matcher.ratio()

    def similarity(self, rrID, wbID):
        return self.compareStr(str(self.getRRProfile(rrID)), str(self.getWBProfile(wbID)))
