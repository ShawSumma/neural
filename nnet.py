class node():
    def __init__(self,ins):
        self.dat = ins
        self.inn = None
        self.g = 0
    def inter(self):
        g =  0
        for i in range(len(self.dat)):
            g += self.dat[i]*self.inn[i]
        self.out = g
        return g
def read(name='zen.txt'):
    x = [[[float(xc) for xc in xb.split(' ')] for xb in xa.split('\n')]for xa in open(name).read().split('\n\n')]
    return mavg(x)
def write(kin,name='zen.txt'):
    new = ''
    for i in kin:
        for j in i:
            for k in j:
                new += str(k) + ' '
            new = new[:-1]
            new += '\n'
        new += '\n'
    open(name,'w').write(new[:-2])
def layer(ind,dat):
    layer = [node(i) for i in dat]
    for i in range(len(layer)):
        layer[i].inn = ind
        layer[i] = layer[i].inter()
    return layer
def mex(rdat,ind):
    for i in range(len(rdat)):
        ind = layer(ind,rdat[i])
    bn = None
    hn = ind.index(max(ind))
    return hn
def gen(rdat,xen=10):
    rdat = [[[xc * random.randrange(100-xen,100+xen)*0.01 for xc in xb] for xb in xa]for xa in rdat]
    return rdat
def rset(rdat):
    return [[[random.random()*2-1 for xc in xb] for xb in xa]for xa in rdat]
def mavg(rdat):
    c = 0
    av = 0
    for xa in rdat:
        for xb in xa:
            for xc in xb:
                c += 1
                av += xc
    return [[[xc * c/av for xc in xb] for xb in xa]for xa in rdat]
def guess(ind,file='out.txt'):
    rdat = gen(read(name=file))
    x = mex(rdat,ind)
    return [x,rdat]

def ngen(ds):
    st = ds[0]
    ret = []
    for d in ds[1:]:
        gen = []
        for i in range(d):
            gen.append([0.5 for i in range(st)])
        ret.append(gen)
        st = d
    ret = rset(ret)
    return ret
def learn(data,nodes,going=10,file=None,verb=False,overwrite=False,ending='',spec={}):
    tpn = {
        'over': 10
        }
    tpn.update(spec)
    ofs = tpn
    out = file
    if out == None:
        write(ngen(nodes))
        nout = 'out.txt'
    else:
        try:
            open(out,'r').read()
        except:
            write(ngen(nodes),name=out)
        nout = out
    if overwrite:
        write(ngen(nodes),name='out.txt' if file == None else file)
        nout = out
    dats = data
    random.shuffle(dats)
    trained = [0 for i in range(max([i[0] for i in dats])+1)]
    bes = 0
    total = 0
    c = 0
    for nv in range(going):
        for i in dats:
            out = guess(i[1],file=nout) 
            if out[0] == i[0]:
                trained[i[0]] += 1
                total += 1
                if trained[i[0]] <= 100:
                    write(out[1],name=nout)
                if trained[i[0]] > 500 and min(trained) < 20:
                    write(gen(read(name=nout),xen=ofs['over']),name=nout)
            else:
                trained[i[0]] -= 10
                if trained[i[0]] < 0:
                    trained[i[0]] = 0
        if verb:
            print(int(total/len(dats)*100),trained)
            total = 0
        if min(trained) > 200:
            break
        c += 1
    if ending != '':
        return(eval(ending))
import random
