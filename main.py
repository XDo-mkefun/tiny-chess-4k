import json,os,urllib.request as q
U=os.environ["MAKEFUN_ENV_URL"]
def P(p,b):
 with q.urlopen(q.Request(U+p,json.dumps(b).encode()))as x:return json.load(x)
V=(0,100,320,330,500,900)
NJ=(-33,-31,-18,-14,14,18,31,33);RD=(-16,-1,1,16);BD=(-17,-15,15,17);KJ=RD+BD
B=bytearray(128);S=C=0;E=-1;K=[4,116];N=0;T={};Z=[2,1]+[0]*14+[8,4,0];M=99999
X=Exception
def u(m):
 f=ord(m[0])+16*int(m[1])-113;t=ord(m[2])+16*int(m[3])-113
 return f|t<<7|('nbrq'.index(m[4])+2)<<14 if m[4:]else f|t<<7
def y(m):
 f=m&127;t=m>>7&127
 return chr(97+(f&7))+str(f//16+1)+chr(97+(t&7))+str(t//16+1)+('nbrq'[(m>>14)-2]if m>>14 else'')
def h(y,w):
 for t in(y-15,y-17,y+15,y+17):
  if not t&136 and B[t]==1+6*w and(t>y)==w:return 1
 for d in NJ+KJ:
  t=y+d
  if not t&136 and B[t]==2+6*w+4*(d in KJ):return 1
 for d in RD+BD:
  t=y+d
  while not t&136:
   v=B[t]
   if v:
    if v-6*w==5 or v-6*w==(4 if d in RD else 3):return 1
    break
   t+=d
 return 0
def g(cp):
 ms=[];a=ms.append
 for f in range(128):
  if f&136:continue
  v=B[f]
  if not v or(v<7)!=(S==0):continue
  t=v%6
  if t==1:
   d=16-32*S;lr=7-7*S;o=f+d
   if not o&136:
    if not B[o]and not cp:
     if o>>4==lr:ms+=[f|o<<7|pr<<14 for pr in(5,4,3,2)]
     else:
      a(f|o<<7)
      if f>>4==1+5*S and not B[o+d]:a(f|(o+d)<<7)
    for dd in(d-1,d+1):
     o=f+dd
     if not o&136 and((B[o]and(B[o]<7)!=(S==0))or o==E):
      if o>>4==lr:ms+=[f|o<<7|pr<<14 for pr in(5,4,3,2)]
      else:a(f|o<<7)
  elif t in(2,0):
   for d in(NJ if t==2 else KJ):
    o=f+d
    if o&136:continue
    y=B[o]
    if(not y and not cp)or(y and(y<7)!=(S==0)):a(f|o<<7)
   if t==0 and not cp:
    for d in(1,-1):
     rb=(1+3*S)<<(d<0);ks=K[S];kt=ks+2*d;rs=ks+3*d-(d<0)
     if C&rb and B[rs]==4+6*S and not(B[ks+d]or B[kt])and(d>0 or not B[ks-3])and not(h(ks,1-S)or h(ks+d,1-S)or h(kt,1-S)):a(ks|kt<<7)
  else:
   for d in(BD,RD,RD+BD)[t-3]:
    o=f+d
    while not o&136 and not B[o]:
     if not cp:a(f|o<<7)
     o+=d
    if not o&136 and(B[o]<7)!=(S==0):a(f|o<<7)
 return ms
def m(x):
 global C,E,S
 f=x&127;t=(x>>7)&127;pr=x>>14
 v=B[f];cap=B[t];cs=t
 if v%6==1 and t==E and not cap:
  cs=t-16+32*S
  cap=B[cs];B[cs]=0
 z=(cap,cs,C,E)
 B[t]=pr+6*S if pr else v
 B[f]=0
 if v%6==0:
  K[S]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0
  C&=~(12-9*(S==0))
 C&=~(Z[f//7]|Z[t//7])
 E=(f+t)//2 if v%6==1 and abs(t-f)==32 else-1
 S^=1
 return z
def n(x,z):
 global C,E,S
 cap,cs,C,E=z
 f=x&127;t=(x>>7)&127;pr=x>>14
 S^=1
 B[f]=B[t]if not pr else 1+6*S
 B[t]=0
 if cap:B[cs]=cap
 if B[f]%6==0:
  K[S]=f
  if t-f==2:B[t+1]=B[t-1];B[t-1]=0
  elif f-t==2:B[t-2]=B[t+1];B[t+1]=0
def e():
 s=0
 for f in range(128):
  if f&136:continue
  v=B[f]
  if not v:continue
  t=v%6;w=v>6;u=V[t];r=f>>4;c=f&7
  if t==1:u+=8*(r-1+w*(7-2*r))
  elif t==2:u+=18*(1<c<6 and 1<r<6)
  s+=u*(1-2*w)
 return s*(1-2*S)
def o(ms,pl,tm):
 ms.sort(key=lambda x:B[x>>7&127]+99*(x==tm),reverse=1)
def s(d,a,b,pl):
 global N
 N+=1
 if N>40000:raise X
 k=(bytes(B),S,C,E)
 q=d<=0
 t=0 if q else T.get(k)
 if t and t[0]>=d and(t[1]>=b if t[2]==1 else t[1]<=a if t[2]==2 else 1):return t[1]
 ck=q and h(K[S],1-S)
 st=q and e()
 if q and not ck:
  a=max(a,st)
  if st>=b:return b
 ms=g(q and not ck)
 o(ms,pl,t[3]if t else 0)
 ao=a;bs=st if q and not ck else-M;bm=0;nl=0
 for x in ms:
  u=m(x)
  if h(K[1-S],S):n(x,u);continue
  nl+=1
  v=-s(d-1,-b,-a,pl+1)
  n(x,u)
  if v>bs:bs=v;bm=x
  a=max(a,v)
  if a>=b:break
 if not nl:return bs if q and not ck else-9999+pl if h(K[S],1-S)else 0
 if not q:T[k]=(d,bs,2*(bs<=ao)or(bs>=b),bm)
 return bs
def c():
 global N
 N=0;bm=0;d=1
 while 1:
  try:
   s(d,-M,M,0)
   t=T.get((bytes(B),S,C,E))
   bm=t[3]if t else 0
   d+=1
  except X:break
 if not bm:
  for x in g(0):
   u=m(x)
   if not h(K[1-S],S):bm=x
   n(x,u)
   if bm:break
 return bm
while 1:
 z=P('/game',{})
 if z['status'][0]=='d':break
 while z['status'][0]=='y':
  B[:]=b'\0'*128
  for i,v in enumerate((4,2,3,5,6,3,2,4)):B[i]=v;B[16+i]=1;B[96+i]=7;B[112+i]=v+6
  S=0;C=15;E=-1;K[:]=[4,116]
  for mv in z['moves']:m(u(mv))
  z=P('/move',{'game':z['game'],'move':y(c())})
