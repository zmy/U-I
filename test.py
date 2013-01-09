from ProfileSimilarity import ProfileSim


rrID = '239486743'
#'283033405' -> '2995253071'
#'239486743' -> '532971334'/'1748153860'
#'247776090' -> '1395366355'
simc = ProfileSim('renren.profile.p', 'weibo.profile.p')


#===============================================================================
# keys = set()
# for rrID, profile in simc.rrProfile.items():
#    keys = keys | profile.keys()
#    if '所在' in profile:
#        print(rrID, profile)
# print(keys)
#===============================================================================


#print(simc.compareStr('1989年8月17日', '1989年8月17日'))
#print(simc.compareStr('1989年8月17日', '1984年9月9日'))
#print(simc.similarity(rrID, '1395366355'))
#print(simc.getRRProfile())
#print(simc.getWBProfile())
#print(simc.similarity(rrID, '1690677517'))
#print(simc.getWBProfile())

maxv = -1
maxi = ''
cnt = 0
for wbID in simc.wbProfile.keys():
    cnt += 1
    val = simc.similarity(rrID, wbID)
    print('{}/{}: {}-{}'.format(cnt, len(simc.wbProfile.keys()), wbID, val))
    if val > maxv:
        maxv = val
        maxi = wbID
print(maxi, maxv)
