import matplotlib.pyplot as plt
import numpy as np
import random
import rkAMM
import helpers.aux as aux

def aux_scenario1(list_values):
    
    fig = plt.figure(figsize=(20, 30))

    y = np.arange(0, aux.MAX_DAYS_SIM+1, 1, dtype=int)
    plt.rcParams["figure.figsize"] = (20,10)

    ax = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax.set_title('AMM Q Volume')
    ax.set_xlabel('Days')
    ax.set_ylabel('Volume') 
    ax.set_xlim([0, len(y)])

    ax2.set_title('Premium')
    ax2.set_xlabel('Days')
    ax2.set_ylabel('Prem') 
    ax2.set_xlim([0, len(y)])

    ax3.set_title('Total Volume (Q + Prem)')
    ax3.set_xlabel('Days')
    ax3.set_ylabel('Total Volume') 
    ax3.set_xlim([0, len(y)])

    plt.title('Total Volume (Q + Prem)')
    plt.xlabel('Days')
    plt.ylabel('Total Volume') 
    plt.xlim([0, len(y)])
    
    for i in list_values:
        aux.scenario_1(i[0], i[1])
        aux.result()
        
        array_q_vol = []
        array_prem = []
        array_vol = []

        for j in range(0, aux.NUM_SIM):    
            results = rkAMM.rkAMM()

            array_q_vol.append(results[8]) 
            array_prem.append(results[9])
            array_vol.append(results[10])
        
        curve_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
        linestyles = ['dotted', 'dashed', 'solid', 'dashdot', (0, (1,10)), (0, (3,5,1,5,1,5))]

        array_q_vol = [sum(x) for x in zip(*array_q_vol)]
        q_volume_values = [x / aux.NUM_SIM for x in array_q_vol]        
        ax.plot(y, q_volume_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=curve_color, label = f"Prob. Contribution LP = {int(i[0]*100)}% and Liquidity Contribution = {int(i[1]*100)}% of initial Q")
        ax.legend(loc="upper left", prop = {'size': 8})
        ax.grid()

        array_prem = [sum(x) for x in zip(*array_prem)]
        prem_values = [x / aux.NUM_SIM for x in array_prem]
        ax2.plot(y, prem_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=curve_color, label = f"Prob. Contribution LP = {int(i[0]*100)}% and Liquidity Contribution = {int(i[1]*100)}% of initial Q")
        ax2.legend(loc="upper left", prop = {'size': 8})
        ax2.grid()

        array_vol = [sum(x) for x in zip(*array_vol)]
        volume_values = [x / aux.NUM_SIM for x in array_vol]
        ax3.plot(y, volume_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=curve_color, label = f"Prob. Contribution LP = {int(i[0]*100)}% and Liquidity Contribution {int(i[1]*100)}% of initial Q")
        ax3.legend(loc="upper left", prop = {'size': 8})
        ax3.grid()

    plt.show()