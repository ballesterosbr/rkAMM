import rkAMM

# Base scenario
NUM_SIM = 10
MAX_NUMBER_INVOICES = 500
MIN_PERC_NOT_COLLATERALIZED = 0.05
MAX_PERC_NOT_COLLATERALIZED = 0.5
MIN_INVOICE_REQ_NOT_COL = 100
MAX_INVOICE_REQ_NOT_COL = 2000
PROB_HACK = 0.0
PROB_UNPAID = 0.00 + PROB_HACK
PROB_ADD_LIQUIDITY = 0.0
MIN_LIQUIDITY_ADD = 0
MAX_LIQUIDITY_ADD = 0
MAX_DELAY_INVOICE = 120
MIN_DELAY_INVOICE = 30
MAX_DAYS = 500
ADDITIONAL_DAYS = 30
MAX_DAYS_SIM = MAX_DAYS + MAX_DELAY_INVOICE + ADDITIONAL_DAYS
START_Q_LIQUIDITY = 10000
START_PREM_LIQUIDITY = 0
INITIAL_TOTAL_VOLUME = START_Q_LIQUIDITY + START_PREM_LIQUIDITY

def reset():
    global PROB_ADD_LIQUIDITY
    global MIN_LIQUIDITY_ADD
    global MAX_LIQUIDITY_ADD
    PROB_ADD_LIQUIDITY = MIN_LIQUIDITY_ADD = MAX_LIQUIDITY_ADD = 0
    global MIN_DELAY_INVOICE
    global MAX_DELAY_INVOICE
    MIN_DELAY_INVOICE, MAX_DELAY_INVOICE = 30, 120
    global PROB_UNPAID
    PROB_UNPAID = 0
    global MIN_INVOICE_REQ_NOT_COL
    global MAX_INVOICE_REQ_NOT_COL
    MIN_INVOICE_REQ_NOT_COL, MAX_INVOICE_REQ_NOT_COL = 100, 2000
    global MIN_PERC_NOT_COLLATERALIZED
    global MAX_PERC_NOT_COLLATERALIZED
    MIN_PERC_NOT_COLLATERALIZED, MAX_PERC_NOT_COLLATERALIZED = 0.05, 0.5

def scenario_1(prob_add_liq, perc_liq_add):
    global PROB_ADD_LIQUIDITY
    global MIN_LIQUIDITY_ADD
    global MAX_LIQUIDITY_ADD
    PROB_ADD_LIQUIDITY, MIN_LIQUIDITY_ADD, MAX_LIQUIDITY_ADD = prob_add_liq, 0, perc_liq_add*START_Q_LIQUIDITY

def scenario_2(prob_unpaid):
    global PROB_UNPAID
    PROB_UNPAID = prob_unpaid

def scenario_3(min_invoice_delay, max_invoice_delay):
    global MIN_DELAY_INVOICE
    global MAX_DELAY_INVOICE
    MIN_DELAY_INVOICE, MAX_DELAY_INVOICE = min_invoice_delay, max_invoice_delay

def scenario_4(invoice_amount_not_col):
    global MIN_INVOICE_REQ_NOT_COL
    global MAX_INVOICE_REQ_NOT_COL
    MIN_INVOICE_REQ_NOT_COL = MAX_INVOICE_REQ_NOT_COL = invoice_amount_not_col*START_Q_LIQUIDITY

def scenario_5(invoice_col):
    global MIN_PERC_NOT_COLLATERALIZED
    global MAX_PERC_NOT_COLLATERALIZED
    MAX_PERC_NOT_COLLATERALIZED = MIN_PERC_NOT_COLLATERALIZED = 1-invoice_col

def hack_scenario(prob_hack, invoice_col):
    global PROB_UNPAID
    global MIN_PERC_NOT_COLLATERALIZED
    global MAX_PERC_NOT_COLLATERALIZED
    global MIN_INVOICE_REQ_NOT_COL
    global MAX_INVOICE_REQ_NOT_COL
    PROB_UNPAID = prob_hack
    MAX_PERC_NOT_COLLATERALIZED = MIN_PERC_NOT_COLLATERALIZED = 1-invoice_col

def result():
    col = []
    imp = []
    total_loss = []
    pag = []
    total_to_col = []
    total_q = []
    total_prem = []
    total_vol = []
    array_q_vol = []
    array_prem = []
    array_vol = []
    un_days = []
    
    for i in range(0, NUM_SIM):    
        results = rkAMM.rkAMM()

        col.append(results[0])
        imp.append(results[1])
        total_loss.append(results[2])
        pag.append(results[3])
        total_to_col.append(results[4])
        total_q.append(results[5])
        total_prem.append(results[6])
        total_vol.append(results[7])
        array_q_vol.append(results[8]) 
        array_prem.append(results[9])
        array_vol.append(results[10])
        un_days.append(results[11])
    
    array_q_vol = [sum(x) for x in zip(*array_q_vol)]
    q_volume_values = [x / NUM_SIM for x in array_q_vol]

    array_prem = [sum(x) for x in zip(*array_prem)]
    prem_values = [x / NUM_SIM for x in array_prem]

    array_vol = [sum(x) for x in zip(*array_vol)]
    volume_values = [x / NUM_SIM for x in array_vol]

    data = [
        ["|", "Number of simulations" , "|", f"{NUM_SIM}", "|"],
        ["|", "Simulation time period" , "|", f"{MAX_DAYS_SIM} days", "|"],
        ["|", "Total of invoices" , "|", f"{MAX_NUMBER_INVOICES}", "|"],
        ["|", "Average of accepted invoices (collateralized)" , "|", f"{sum(col)/NUM_SIM} out of {MAX_NUMBER_INVOICES} invoices in {MAX_DAYS_SIM} days ({format((100*sum(col)/NUM_SIM)/MAX_NUMBER_INVOICES, '.2f')} %)", "|"],
        ["|", "Average of paid invoices (capital returned)" , "|", f"{sum(pag)/NUM_SIM} out of {sum(col)/NUM_SIM} collateralized invoices", "|"],
        ["|", "Average of unpaid invoices (capital not returned)" , "|", f"{sum(imp)/NUM_SIM} out of {sum(col)/NUM_SIM} collateralized invoices", "|"],
        ["|", "Average loss due to unpaid invoices" , "|",  f"{round(sum(total_loss)/NUM_SIM, 2)}", "|"],
        ["|", "Total collateral covered" ,  "|", f"{sum(total_to_col)/NUM_SIM} in {sum(col)/NUM_SIM} collateralized invoices", "|"],
        ["|", "Total collateral covered x (i.c.)" ,  "|", f"{format((sum(total_to_col)/NUM_SIM)/START_Q_LIQUIDITY, '.3f')} x initial collateral", "|"],
        ["|", "Total premium obtained" ,  "|", f"{round(sum(total_prem)/NUM_SIM, 2)} in {sum(col)/NUM_SIM} collateralized invoices", "|"],
        ["|", "Total premium obtained x (i.c.)" ,  "|", f"{format(round(sum(total_prem)/NUM_SIM, 2)/START_Q_LIQUIDITY, '.3f')} x initial collateral", "|"],
        ["|", "Total AMM volume" ,  "|", f"{round(sum(total_vol)/NUM_SIM, 2)} after {MAX_DAYS_SIM} days", "|"],
        ["|", "AMM profit percentage" ,  "|", f"{round((sum(total_vol)/NUM_SIM - INITIAL_TOTAL_VOLUME)*100 / INITIAL_TOTAL_VOLUME, 2)} %", "|"],
    ]

    print("".join([("-" * 105)] * 1))
    print("{:<0s} {:<50s} {:<0s} {:<48s} {:<0s}".format("|", "Description", "|", "Value", "|"))
    print("".join([("-" * 105)] * 1))
    for line in data:
        print("{:<0s} {:<50s} {:<0s} {:<48s} {:<0s}".format(*line))
    print("".join([("-" * 105)] * 1))