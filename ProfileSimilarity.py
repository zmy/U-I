import difflib
import pickle


class ProfileSim:
    def __init__(self, rrProFilePath, wbProFilePath):
        #TODO: deal with junk?
        self.rrProfile = pickle.load(open(rrProFilePath, 'rb'))
        self.wbProfile = pickle.load(open(wbProFilePath, 'rb'))
        self.matcher = difflib.SequenceMatcher()

    def getRRProfile(self, rrID):
        return self.rrProfile[rrID]
    
    def getWBProfile(self, wbID):
        return self.wbProfile[wbID]

    def compareStr(self, strA, strB):
        self.matcher.set_seqs(strA, strB)
        return self.matcher.ratio()

    def similarity(self, rrID, wbID):
        return self.compareStr(str(self.getRRProfile(rrID)), str(self.getWBProfile(wbID)))
