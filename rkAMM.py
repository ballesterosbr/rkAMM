import random
import helpers.aux as aux

def unpaid_delayed_aux(prob_unpaid):
    probability_delayed = random.random() > prob_unpaid
    if probability_delayed:
        return random.randint(aux.MIN_DELAY_INVOICE, aux.MAX_DELAY_INVOICE)
    else:
        return 100000

def generate_invoices():
    invoices_list = []
    for i in range(0, aux.MAX_NUMBER_INVOICES):
        delay_days = unpaid_delayed_aux(aux.PROB_UNPAID)

        invoices_list.append({
            'id':i,
            'q':round(random.uniform(aux.MIN_PERC_NOT_COLLATERALIZED,aux.MAX_PERC_NOT_COLLATERALIZED), 2),
            'q_amount': random.randint(aux.MIN_INVOICE_REQ_NOT_COL, aux.MAX_INVOICE_REQ_NOT_COL),
            'delay_days': delay_days,
            'col_when': 0,
            'collateralized': False,
            'paid': False
        })

    return invoices_list

def modify_liquidity_q(amount, total_q_volume):
    total_q_volume += amount
    return total_q_volume

def modifiy_liquidity_prem(amount, total_premium):
    total_premium += amount
    return total_premium

def get_premium(q_amount, q, total_q_volume, total_premium):
    volume = total_q_volume + total_premium
    prem = round(q*q/(1-q*(1+q_amount/(volume)))*q_amount, 2)
    return prem

def rkAMM():
    invoices =  generate_invoices()
    sum_q_amount = 0
    for i in range(len(invoices)):
        sum_q_amount += list(invoices[i].values())[2]
        #print(invoices[i])
    #print("Total collateral to afford", sum_q_amount)
    
    total_premium = aux.START_PREM_LIQUIDITY
    total_q_volume = aux.START_Q_LIQUIDITY
    total_volume = total_premium + total_q_volume
    paid_counter = 0
    collateralized_counter = 0
    collateralized_amount = 0
    unpayed_amount = 0
    unavailable_days = 0

    array_q_volume = [total_q_volume]
    array_prem = [0]
    array_vol = [total_volume]

    for i in range(0, aux.MAX_DAYS_SIM):
        prob_liq_added = random.random() < aux.PROB_ADD_LIQUIDITY

        if prob_liq_added:
            total_q_volume = modify_liquidity_q(random.randint(aux.MIN_LIQUIDITY_ADD, aux.MAX_LIQUIDITY_ADD), total_q_volume)
            
        try:
            q = invoices[i]['q']
            q_amount = invoices[i]['q_amount']

            if(total_q_volume - invoices[i]['q_amount']  > 0 and i < len(invoices) and invoices[i]['collateralized'] == False):
                prem = get_premium(q_amount, q, total_q_volume, total_premium)
                total_q_volume = modify_liquidity_q(-q_amount, total_q_volume)
                total_premium = modifiy_liquidity_prem(prem, total_premium)
                collateralized_counter += 1
                invoices[i]['collateralized'] = True
                invoices[i]['col_when'] = i

                collateralized_amount += q_amount
                unpayed_amount += q_amount

            else:               
                if(total_q_volume - invoices[i]['q_amount']  < 0):
                    unavailable_days += 1

            for j in invoices:
                if(i - j['col_when'] == j['delay_days'] and j['collateralized'] == True):
                    total_q_volume = modify_liquidity_q(j['q_amount'], total_q_volume)
                    j['paid'] = True
                    paid_counter += 1
                    unpayed_amount -= j['q_amount']
                
        except:
            for j in invoices:
                if(i - j['col_when'] == j['delay_days'] and j['collateralized'] == True):
                    total_q_volume = modify_liquidity_q(j['q_amount'], total_q_volume)
                    j['paid'] = True
                    paid_counter += 1
                    unpayed_amount -= j['q_amount']

        array_q_volume.append(total_q_volume)
        array_prem.append(total_premium)
        total_volume = total_q_volume + total_premium
        array_vol.append(total_volume)

    return collateralized_counter, (collateralized_counter-paid_counter), unpayed_amount, paid_counter, collateralized_amount, sum_q_amount, total_premium, total_volume, array_q_volume, array_prem, array_vol, unavailable_days