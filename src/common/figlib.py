import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle, Polygon
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if 'Liberation' in f and 'Sans' in f and 'Narrow' not in f: fm.fontManager.addfont(f)
plt.rcParams['font.family']='Liberation Sans'
plt.rcParams['mathtext.fontset']='custom'
plt.rcParams['mathtext.rm']='Liberation Sans'
plt.rcParams['mathtext.it']='Liberation Sans:italic'
plt.rcParams['mathtext.bf']='Liberation Sans:bold'
PAGE='#DDE8D5'; CARD='#EAF3E2'; HEAD='#2F6B1A'; ACC='#3D7A25'; DARK='#2A5418'; RULE='#6BA04A'
BLUE='#3B82C8'; YEL='#F0C336'; RED='#B23A3A'; PRED='#F6DAD5'; GREY='#8A9A84'; LGREY='#C9D6C2'; INK='#1F2A1B'
W=6.6
def fig(h, w=W): return plt.figure(figsize=(w,h), dpi=220, facecolor=CARD)
def canvas(f, xlim, ylim, rect=(0,0,1,1)):
    ax=f.add_axes(rect); ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis('off'); ax.set_facecolor(CARD); return ax
def box(ax,x,y,w,h,txt='',fc='white',ec=ACC,lw=1.2,fs=8.5,tc=INK,bold=False,r=0.06,alpha=1,ls='-',z=2):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0,rounding_size={r}",fc=fc,ec=ec,lw=lw,alpha=alpha,ls=ls,zorder=z))
    if txt: ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,color=tc,fontweight='bold' if bold else 'normal',zorder=z+1,linespacing=1.15)
def arrow(ax,p0,p1,color=BLUE,dashed=False,lw=1.8,ms=11,z=4,style='-|>'):
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle=style,mutation_scale=ms,color=color,lw=lw,ls=(0,(4,3)) if dashed else '-',zorder=z,shrinkA=0,shrinkB=0))
def line(ax,xs,ys,color=BLUE,lw=1.8,dashed=False,z=3):
    ax.plot(xs,ys,color=color,lw=lw,ls=(0,(4,3)) if dashed else '-',zorder=z,solid_capstyle='round')
def txt(ax,x,y,s,fs=8.5,c=INK,ha='center',va='center',bold=False,z=6,**k):
    return ax.text(x,y,s,fontsize=fs,color=c,ha=ha,va=va,fontweight='bold' if bold else 'normal',zorder=z,**k)
def save(f,name,outdir='figs'):
    import os; os.makedirs(outdir,exist_ok=True); f.savefig(f'{outdir}/{name}.png',dpi=220,facecolor=CARD); plt.close(f)
def style_axes(ax):
    ax.set_facecolor('white')
    for s in ax.spines.values(): s.set_color(ACC)
    ax.tick_params(colors=INK,labelsize=8); ax.grid(True,color=LGREY,lw=0.6)
