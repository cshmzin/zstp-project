from ltp import LTP


ltp = LTP(path='pretrained_model') # 默认加载 Small 模型

sents = ltp.sent_split(["该僵尸网络包含至少35000个被破坏的Windows系统，攻击者和使用者正在秘密使用这些系统来开采Monero加密货币。该僵尸网络名为“ VictoryGate”，自2019年5月以来一直活跃。","asdahdda,sad"])
print('分句:')
for sent in sents:
    print(sent)

sent =[sents[0]]
print('分词:')
seg, hidden = ltp.seg(sent)
print(seg[0])
print('词性标注:')
pos = ltp.pos(hidden)
print(pos[0])

print('语义角色标注:')
srl = ltp.srl(hidden, keep_empty=False)
print(srl[0])

print('句法分析:')
dep = ltp.dep(hidden)
print(dep[0])

def dep_AtoA(sent):
    seg, hidden = ltp.seg([sent])
    seg = seg[0]
    dep = ltp.dep(hidden)[0]
    print(seg)
    sbvs = []
    vobs = []
    results = []
    for d in dep:
        if d[2] == 'SBV':
            sbvs.append((d[0],d[1]))
        if d[2] == 'VOB':
            vobs.append((d[1],d[0]))
    for sbv in sbvs:
        for vob in vobs:
            if sbv[1] == vob[0]:
                results.append((seg[sbv[0]-1],seg[sbv[1]-1],seg[vob[1]-1]))
    print(results)
#dep_AtoA(sents[0])

def srl_AtoA(sent):
    seg, hidden = ltp.seg([sent])
    seg = seg[0]
    srl = ltp.srl(hidden, keep_empty=False)[0]

    results = []
    for s in srl:
        key = s[0]
        values = s[1]
        result_A0 = ''
        result_A1 = ''
        for value in values:
            if value[0] == 'A0':
                result_A0 = ''.join(seg[value[1]:value[2]+1])
            if value[0] == 'A1':
                result_A1 = ''.join(seg[value[1]:value[2]+1])
        if result_A0 != '' and result_A1 != '':
            results.append((result_A0,seg[key],result_A1))
    print(results)

srl_AtoA(sents[0])