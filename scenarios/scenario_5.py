import matplotlib.pyplot as plt
import numpy as np
import rkAMM
import helpers.aux as aux

def aux_scenario5(list_values):
    
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

    for i in list_values:
        aux.scenario_5(i)
        aux.result()

        array_q_vol = []
        array_prem = []
        array_vol = []

        for j in range(0, aux.NUM_SIM):    
            results = rkAMM.rkAMM()

            array_q_vol.append(results[8]) 
            array_prem.append(results[9])
            array_vol.append(results[10])
    
        colors = ['mediumblue', 'firebrick', 'limegreen']
        linestyles = ['dotted', 'dashed', 'solid']
        
        array_q_vol = [sum(x) for x in zip(*array_q_vol)]
        q_volume_values = [x / aux.NUM_SIM for x in array_q_vol]       
        ax.plot(y, q_volume_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=colors[list_values.index(i)], label = f"Invoices {int(i*100)}% collateralized")
        ax.legend(loc="upper left", prop = {'size': 8})
        ax.grid()

        array_prem = [sum(x) for x in zip(*array_prem)]
        prem_values = [x / aux.NUM_SIM for x in array_prem]
        ax2.plot(y, prem_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=colors[list_values.index(i)], label = f"Invoices {int(i*100)}% collateralized")
        ax2.legend(loc="upper left", prop = {'size': 8})
        ax2.grid()

        array_vol = [sum(x) for x in zip(*array_vol)]
        volume_values = [x / aux.NUM_SIM for x in array_vol]
        ax3.plot(y, volume_values, linewidth=2, linestyle=linestyles[list_values.index(i)], color=colors[list_values.index(i)],  label = f"Invoices {int(i*100)}% collateralized")
        ax3.legend(loc="upper left", prop = {'size': 8})
        ax3.grid()

    plt.show()