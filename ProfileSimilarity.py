import difflib
import math
import pickle


class ProfileSim:
    #TODO: train to learn the weight matirx
    weight = {
        ('生日','生日'): 0.8,
        ('星座','生日'): 0.3,
        ('性别','性别'): 0.2,
        ('名称','真实姓名'): 0.9,
        ('名称','昵称'): 0.8,
        ('个人网站','昵称'): 0.6,
        ('我的域名','昵称'): 0.6,
        ('个性域名','昵称'): 0.6,
        ('个人网站','博客'): 0.8,
        ('我的域名','博客'): 0.8,
        ('个性域名','博客'): 0.8,
        ('QQ','QQ'): 0.9,
        ('家乡','所在地'): 0.2,
        ('所在城市','所在地'): 0.3,
        ('大学','大学'): 0.6,
        ('高中','高中'): 0.5,
        ('初中','初中'): 0.5,
        ('小学','小学'): 0.5,
        ('中专技校','高中'): 0.2,
        ('所在学校','大学'): 0.3,
        ('所在学校','高中'): 0.2,
        ('所在学校','初中'): 0.2
    }

    def __init__(self, rrProFilePath, wbProFilePath):
        #TODO: deal with junk?
        self.rrProfile = pickle.load(open(rrProFilePath, 'rb'))
        self.wbProfile = pickle.load(open(wbProFilePath, 'rb'))
        self.matcher = difflib.SequenceMatcher()

    def compareStr(self, strA, strB):
        self.matcher.set_seqs(strA, strB)
        return self.matcher.ratio()

    def getRRProfile(self, key='all'):
        if key=='all':
            return self.rrProfile[self.rrID]
        else:
            profile = self.rrProfile[self.rrID]
            if key in profile:
                return profile[key]
            else:
                return None

    def getWBProfile(self, key='all'):
        if key=='all':
            return self.wbProfile[self.wbID]
        else:
            profile = self.wbProfile[self.wbID]
            if key in profile:
                return profile[key]
            else:
                return None

    def compareItems(self, rrKeys, wbKeys):
        sumsim = 0
        sumwgt = 0
        for rrKey in rrKeys:
            rrVal = self.getRRProfile(rrKey)
            if rrVal is None: continue
            for wbKey in wbKeys:
                if (rrKey,wbKey) in self.weight:
                    wbVal = self.getWBProfile(wbKey)
                    if wbVal is None: continue
                    sumwgt += self.weight[(rrKey,wbKey)]
                    sumsim += self.compareStr(rrVal, wbVal) * self.weight[(rrKey,wbKey)]
        return sumsim/sumwgt

    def similarity(self, rrID, wbID):
        self.rrID = rrID
        self.wbID = wbID
        #TODO: use compareItems to group similar keys rather than directly sum as following
        sumsim = 0
        sumwgt = 0
        for (rrKey, wbKey) in self.weight.keys():
            rrVal = self.getRRProfile(rrKey)
            wbVal = self.getWBProfile(wbKey)
            if rrVal is not None and wbVal is not None:
                sumwgt += self.weight[(rrKey,wbKey)]
                sumsim += self.compareStr(rrVal, wbVal) * self.weight[(rrKey,wbKey)]
        if sumwgt==0:
            return 0
        else:
            return sumsim/math.sqrt(sumwgt) #sumsim, sumsim/sumwgt
