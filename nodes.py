def nodes(tree):
    from collections import defaultdict
    nouveau_niveau=-1
    niveau_actuel=-1
    default_value1=['']
    parent=defaultdict(lambda: default_value1)
    filiation={}
    #Indicators
    i1=-1 #Indicates the parent we are working with
    i2=-1 #Indicates the child we are working with
    while(niveau_actuel<=maxim(tree)):
        for char in tree:
            if char=='[':
                nouveau_niveau+=1
                if nouveau_niveau==niveau_actuel+1:
                    i1+=1
                    i2=-1
                    parent[i1]=''
                if nouveau_niveau==niveau_actuel+2:
                    i2+=1
                    if filiation.get(parent[i1])==None:
                        filiation[parent[i1]]=['']
                    else: 
                        filiation[parent[i1]].append('')
                continue
            if char==']':
                nouveau_niveau-=1
                continue
            if nouveau_niveau==niveau_actuel+1:
                parent[i1]+=char
                continue
            if nouveau_niveau==niveau_actuel+2:
                filiation[parent[i1]][i2]+=char
                continue
            if nouveau_niveau>niveau_actuel+2:
                continue
            if nouveau_niveau<niveau_actuel+1:
                continue
        niveau_actuel+=1
        i1=-1
        i2=-1
    return filiation

def maxim(tree):
    compt=-1
    maxim=-1
    for char in tree:
        if char=='[':
            compt+=1
        if compt>maxim:
            maxim=compt
        if char==']':
            compt-=1
    return maxim