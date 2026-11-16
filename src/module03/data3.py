"""Verified illustrative numbers for Module 3 (training values only; not specifications)."""
import math
Vdc=360.0; Vph_max=Vdc/2; pp=4; poles=2*pp
ke=0.45; Iq=300.0; T=1.5*ke*Iq            # 202.5 N.m
n=3000.0; w=2*math.pi*n/60; P=T*w         # 314.16 rad/s, 63.6 kW
fe=pp*n/60; ns=120*fe/poles               # 200 Hz, 3000 rpm
B,I_c,L_c,r_c=0.8,100.0,0.15,0.05; F_c=B*I_c*L_c; T_c=F_c*r_c   # 12 N, 0.6 N.m
f_i,p_i=100.0,4; ns_i=120*f_i/p_i; n_r=2940.0; slip=(ns_i-n_r)/ns_i*100  # 3000 rpm, 2 %
E3000=ke*w; w_base=Vph_max/ke; n_base=w_base*60/(2*math.pi); P_base=T*w_base  # 141.4 V, 400 rad/s, 3819.7 rpm, 81 kW
n_hi=8000.0; w_hi=2*math.pi*n_hi/60; T_hi=P_base/w_hi            # 96.7 N.m
EL_rms_3000=math.sqrt(3)*(E3000/math.sqrt(2))                    # 173.1 V line-to-line rms
def maxerr(k): return math.degrees(math.atan((1-k)/(2*math.sqrt(k))))
k_gain=0.90; err_max=maxerr(k_gain); Id_err=Iq*math.sin(math.radians(err_max))  # 3.02 deg, 15.8 A
off=12.0; T_fac=math.cos(math.radians(off)); Id_off=Iq*math.sin(math.radians(off)); I_need=Iq/T_fac  # 0.9781, 62.4 A, 306.7 A
R20=8e-3; alpha=0.0039; Tw=120.0; Rhot=R20*(1+alpha*(Tw-20)); Irms=Iq/math.sqrt(2)
Pcu=3*Irms**2*Rhot; Rth=0.040; dTw=Pcu*Rth; Tcool=60.0           # 11.12 mohm, 1501 W, 60.0 K
dT_ref,dT_now=6.0,11.0; flow_ratio=dT_ref/dT_now                  # 0.545
ratio=9.0; eta_g=0.97; rw=0.32
Tw_=T*ratio*eta_g; Fx=Tw_/rw; n_w=n/ratio; w_w=2*math.pi*n_w/60; v=w_w*rw; v_kmh=v*3.6   # 1767.8 N.m, 5524 N, 40.2 km/h
n_max=12000.0; v_max=(2*math.pi*(n_max/ratio)/60)*rw*3.6          # 160.8 km/h
Z=20; n_a=6000.0; f_mesh=Z*n_a/60; order=f_mesh/(n_a/60)          # 2000 Hz, order 20
