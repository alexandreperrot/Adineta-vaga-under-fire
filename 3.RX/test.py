# -*- coding: utf-8 -*-
"""
Alexandre Perrot

"""
from matplotlib import pyplot as plt
from scipy.stats import poisson
import numpy as np


def loadfile(n):
    with open(f'outputs/RX_{n}.csv','rt') as f:
        data=np.loadtxt(f,skiprows=8,delimiter=',')
    dose=data[:,3]
    return dose

def hist():
    fig, ax = plt.subplots(2, figsize=(8,6))
    bins=range(80000,90000,100)
    n='Count_21.10E8'
    count=loadfile(n)
    ax[1].hist(count,bins=bins, density=True, histtype='step', linewidth=1.5, alpha=0.8, label=n)
    mu=count.mean()
    pois=poisson.pmf(bins,mu)
    plt.plot(bins,pois,linewidth=1, color='r', linestyle='dashed', label='poisson')
    n=f'Dose_21.10E8'
    dose=loadfile(n)
    print(min(dose))
    ax[0].hist(dose,bins=30, histtype='step', linewidth=1.5, alpha=1, label=n)

    ax[1].set_xlabel('# RX')
    ax[1].set_ylabel('# bins')
    ax[1].legend()
    
    ax[0].set_xlabel('Dose (Gy)')
    ax[0].set_ylabel('# bins')
    ax[0].legend()

    plt.suptitle('Poisson distribution over # RX (precise)',bbox=dict(facecolor='None',edgecolor='black'))
    plt.tight_layout()
    plt.savefig('RX_poisson_precise.png')

def all_hist():
    fig, ax = plt.subplots(2, figsize=(8,6))
    bins=range(35000,86000)
    for i in range(10,153,142):
        n=f'Count_{i}.10E7'
        count=loadfile(n)
        ax[1].hist(count,bins=bins, density=True, histtype='step', linewidth=1.5, alpha=0.8, label=n)
        mu=count.mean()
        pois=poisson.pmf(bins,mu)
        if i==21 :
            plt.plot(bins,pois,linewidth=1, color='r', linestyle='dashed', label='poisson')
        else :
            plt.plot(bins,pois,linewidth=1, color='r', linestyle='dashed',)
        #ax[1].annotate(xy=((i-3)/2,0.5), xycoords=('data','axes fraction'),text=f'$\mu$={count.mean():.0f}',
        #color='r', bbox=dict(facecolor='None',edgecolor='r') )


        n=f'Dose_{i}.10E7'
        dose=loadfile(n)
        print(min(dose))
        #bins_dose=np.linspace(0,110,20)
        ax[0].hist(dose,bins=30, histtype='step', linewidth=1.5, alpha=1, label=n)
        #ax[0].annotate(xy=(2*(i-3),0.5), xycoords=('data','axes fraction'),text=f'{dose.mean():.2f} $Gy$',
        #color='r', bbox=dict(facecolor='None',edgecolor='r') )

    ax[1].set_xlabel('# RX')
    ax[1].set_ylabel('# bins')
    ax[1].legend()
    
    ax[0].set_xlabel('Dose (Gy)')
    ax[0].set_ylabel('# bins')
    ax[0].legend()

    plt.suptitle('Poisson distribution over # RX (precise)',bbox=dict(facecolor='None',edgecolor='black'))
    plt.tight_layout()
    plt.savefig('RX_poisson_precise.png')

all_hist()