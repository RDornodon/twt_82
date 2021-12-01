class K:
 def __init__(S,r,c,C):S.r,S.c,S.C=r,c,C
 def D(S,O):
  if('0'>S.C)>S.c:S.c=min(7,max(3,O.c))
  R=S.c
  if'0'>O.C:O.c=min(7,max(3,S.c))
  return abs(S.r-O.r)+abs(R-O.c)
E=enumerate
_K={C:K(r,c,C)for r,R in E(['1234567890','qwertyuiop','Casdfghjkl','**zxcvbnm'])for c,C in E(R)}
for I in[I:=input]*int(I()):
 s,U='',0
 _K[' ']=K(4,0,' ')
 for C in I():
  if(C<(c:=C.lower()))!=U and'9'<C:s+='C';U^=1
  if s[-1:]!=c:s+=c
 m,r=int(I()),0
 for b,e in zip(s,s[1:]):
  r+=_K[b].D(_K[e])
 print(r//m)