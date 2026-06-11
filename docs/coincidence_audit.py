from fractions import Fraction
from math import comb
import itertools, json

def Dg(l):
    if l==0: return 1
    if l==1: return 10
    return comb(9+l,l)-comb(7+l,l-2)
D={l:Dg(l) for l in range(0,8)}

exprs=[]
for i in range(0,8):
    for d in (1,2,4):
        exprs.append((Fraction(D[i],d), f"D{i}/{d}"))
for i,j in itertools.combinations(range(0,8),2):
    for s in (1,-1):
        for d in (1,2,4):
            v=Fraction(D[i]+s*D[j],d)
            exprs.append((v,f"(D{i}{'+' if s>0 else '-'}D{j})/{d}"))
            v2=Fraction(D[j]-D[i],d)
            exprs.append((v2,f"(D{j}-D{i})/{d}"))

def hits(target,tol):
    out=[]
    for v,name in exprs:
        if v>0 and abs(float(v)-target)/target<=tol:
            out.append((float(v),name))
    return out

total=len(exprs)
h220_exact=[(v,n) for v,n in exprs if v==220]
h220=hits(220,0.02)
h303=hits(303,0.02)
h303_within_LCDM=hits(301.75,0.02)
print("total expressions:",total)
print("exact 220:",h220_exact)
print("within 2% of 220:",sorted(set(h220)))
print("within 2% of 303:",sorted(set(h303)))

ideal=18/1.0171
window=(ideal*0.95, ideal*1.05)
base={'2':2,'n_obs':3,'n*-3':8,'n*-2':9,'n*-1':10,'n*':11,'dim_so10':45,'2dim':90}
cand={}
for (na,a),(nb,b) in itertools.product(base.items(),repeat=2):
    for op,val in (('+',a+b),('-',a-b),('*',a*b)):
        for s in (1,2):
            v=s*val
            if window[0]<=v<=window[1]:
                cand[f"{s}*({na}{op}{nb})" if s==2 else f"{na}{op}{nb}"]=v
total_L=len(base)**2*3*2
print("Lambda coeff window:",window)
print("Lambda space size:",total_L,"hits:",len(cand))
ints=sorted(set(cand.values()))
print("hit values:",ints)

e18=[k for k,v in cand.items() if v==18]
print("expressions equal 18:",len(e18), e18[:12])

for tol in (0.005,0.01,0.02,0.05):
    print("tol",tol,"hits220",len(set(hits(220,tol))),"hits303",len(set(hits(303,tol))))
