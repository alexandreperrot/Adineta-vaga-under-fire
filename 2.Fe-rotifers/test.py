# -*- coding: utf-8 -*-
"""
Alexandre Perrot

"""
from matplotlib import pyplot as plt
from scipy.stats import poisson
import numpy as np


def loadfile(n):
    with open(f'outputs/F_{n}.csv','rt') as f:
        data=np.loadtxt(f,skiprows=8,delimiter=',')
    dose=data[:,3]
    return dose

def cmap(dose,n):
    dose=dose.reshape(50,50)
    plt.imshow(dose, cmap='seismic')
    plt.xlabel('Xbins')
    plt.ylabel('Ybins')
    plt.title(f'{n} Protons',bbox=dict(facecolor='None',edgecolor='black'),
              pad=16.0, horizontalalignment='left',position=(0,0))
    plt.colorbar(label='# protons')
    plt.savefig(f'P_Dose_{n}_cmap.png')

def hist(dose,n):
    fig, ax = plt.subplots()
    ax.hist(dose,bins=30, linewidth=1, edgecolor='darkblue', color='darkblue',alpha =0.5, label='topas')
    plt.title(f'{n} Protons',bbox=dict(facecolor='None',edgecolor='black'),
              pad=16.0, horizontalalignment='left',position=(0.2,0))
    plt.xlabel('# protons')
    plt.ylabel('# bins')
    plt.legend()
    plt.savefig(f'P_Dose_{n}_hist.png')
    
def all_hist():
    fig, ax = plt.subplots(2, figsize=(8,6))
    bins=range(0,20,1)
    for i in range(3,26,10):
        
        n=f'Count_{i}.10E3'
        count=loadfile(n)
        ax[1].hist(count,bins=bins, density=True, histtype='step', linewidth=1.5, alpha=0.8, label=n)
        mu=count.mean()
        pois=poisson.pmf(bins,mu)
        if i==23 :
            plt.plot(bins,pois,linewidth=1, color='r', linestyle='dashed', label='poisson')
        else :
            plt.plot(bins,pois,linewidth=1, color='r', linestyle='dashed',)
        ax[1].annotate(xy=((i-3)/2,0.5), xycoords=('data','axes fraction'),text=f'$\mu$={count.mean():.0f}',
        color='r', bbox=dict(facecolor='None',edgecolor='r') )


        n=f'Dose_{i}.10E3'
        dose=loadfile(n)
        bins_dose=np.linspace(0,110,20)
        ax[0].hist(dose,bins=bins_dose, histtype='step', linewidth=1.5, alpha=1, label=n)
        ax[0].annotate(xy=(2*(i-3),0.5), xycoords=('data','axes fraction'),text=f'{dose.mean():.2f} $Gy$',
        color='r', bbox=dict(facecolor='None',edgecolor='r') )

    ax[1].set_xlabel('# Fe')
    ax[1].set_ylabel('# bins')
    ax[1].legend()
    
    ax[0].set_xlabel('Dose (Gy)')
    ax[0].set_ylabel('# bins')
    ax[0].legend()

    plt.suptitle('Poisson distribution over # Fe (precise)',bbox=dict(facecolor='None',edgecolor='black'))
    plt.tight_layout()
    plt.savefig('F_poisson_precise.png')


all_hist()