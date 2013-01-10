from ProfileSimilarity import ProfileSim


simc = ProfileSim('renren.profile.p', 'weibo.profile.p')
file = open('simMat.txt', 'w')
cnt = 0
tol = len(simc.rrProfile.keys())
for rrID in simc.rrProfile.keys():
    cnt += 1
    if len(simc.rrProfile[rrID])>1:
        print('calc {}: {}/{}'.format(rrID, cnt, tol))
        for wbID in simc.wbProfile.keys():
            sim = simc.similarity(rrID, wbID)
            if sim > 0.01:
                file.write(rrID+' '+wbID+' '+str(sim)+'\n')
file.close()
