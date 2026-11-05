import math
from .common import number,integer,identifier
def run(d):
 a=d['start'];b=d['end'];c=d.get('center',[0,0,0]);radius=number(d['radius'],0)
 if any(not isinstance(v,list)or len(v)!=3 for v in [a,b,c]):raise ValueError('vector')
 a=[number(v)for v in a];b=[number(v)for v in b];c=[number(v)for v in c]
 v=[b[i]-a[i]for i in range(3)];w=[a[i]-c[i]for i in range(3)];vv=sum(z*z for z in v)
 t=0 if vv==0 else min(1,max(0,-sum(w[i]*v[i]for i in range(3))/vv));nearest=[a[i]+t*v[i]for i in range(3)];distance=math.dist(nearest,c)
 roots=[]
 if vv:
  bb=2*sum(w[i]*v[i]for i in range(3));cc=sum(z*z for z in w)-radius**2;disc=bb*bb-4*vv*cc
  if disc>=0:
   roots=[r for r in [(-bb-math.sqrt(disc))/(2*vv),(-bb+math.sqrt(disc))/(2*vv)]if 0<=r<=1]
 return dict(closest_fraction=t,closest_point=nearest,clearance=distance-radius,blocked=distance<=radius,intersection_fractions=roots)
