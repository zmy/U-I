from ProfileSimilarity import ProfileSim


rrID = '239486743'
simc = ProfileSim('renren.profile.p', 'weibo.profile.p')
maxv = -1
maxi = ''

#print(simc.compareStr({'b':'b','a':'a'}, {'a':'a','b':'b'}))

print(simc.similarity(rrID, '1768190510'))
print(simc.similarity(rrID, '532971334'))

keys = set()
for rrID, profile in simc.rrProfile.items():
    keys = keys | profile.keys()
    if '所在' in profile:
        print(rrID, profile)

print(keys)

#===============================================================================
# cnt = 0
# for wbID in simc.wbProfile.keys():
#    cnt += 1
#    print('{}/{}'.format(cnt, len(simc.wbProfile.keys())))
#    val = simc.similarity(rrID, wbID)
#    if val > maxv:
#        maxv = val
#        maxi = wbID
# print(maxi)
#===============================================================================
