class K:
 def __init__(S,r,c):S.r,S.c=r,c
 def D(S,O):R=abs(S.r-O.r)+abs(S.c-O.c);return R
class S(K):
 def D(S,O):R=(4-O.r)+abs(O.c-max(7,min(3,O.c)));return R
E=enumerate
if "_K" not in globals():
 global _K
 _K={C:K(r,c)for r,R in E(['1234567890','qwertyuiop','Casdfghjkl','**zxcvbnm'])for c,C in E(R)}|{' ':S(4,5)}

for I in[I:=input]*int(I()):
 s,U='',0
 for C in I():
  if(C<(c:=C.lower()))!=U and'9'<C:s+='C';U^=1
  s+=c
 m,r=int(I()),0
 for b,e in zip(s,s[1:]):
  r+=_K[b].D(_K[e])
 print(r//m)