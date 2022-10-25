from scenarios.scenario_1 import aux_scenario1
from scenarios.scenario_2 import aux_scenario2
from scenarios.scenario_3 import aux_scenario3
from scenarios.scenario_4 import aux_scenario4
from scenarios.scenario_5 import aux_scenario5
from scenarios.hack_scenario import aux_hack_scenario
import sys

def main():
    while True:
        try:
            option = int(input("Choose an scenario to simulate: \n"
                                " 1. Scenario 1 - Increasing Liquidity Through Time \n"
                                " 2. Scenario 2 - More and more Unpaid Invoices \n"
                                " 3. Scenario 3 - More and more Delay in the Invoice Payments \n"
                                " 4. Scenario 4 - Playing with Growing Invoices, therefore growing demanded collateral \n"
                                " 5. Scenario 5 - Playing with Growing % of Collateral with a Same Invoice amount \n"
                                " 6. Hack Scenario \n"
                                " Scenario: "
            ))
        except KeyboardInterrupt:
            print("User has interrupted the simulation.")
            sys.exit()
        except:
            print("You must enter a valid scenario number.")
        else:
            if(option == 1):
                print("Simulating scenario 1, please wait...")
                values_scenario1 = [(0.5, 0.01), (0.5, 0.1), (0.5, 0.25), (0.1, 0.05), (0.5, 0.05), (1.0, 0.05)]
                aux_scenario1(values_scenario1)
                break
            elif(option == 2):
                print("Simulating scenario 2, please wait...")
                values_scenario2 = [0.02, 0.05, 0.2]
                aux_scenario2(values_scenario2)
                break
            elif(option == 3):
                print("Simulating scenario 3, please wait...")
                values_scenario3 = [(30, 60), (60, 90), (90, 120)]
                aux_scenario3(values_scenario3)
                break
            elif(option == 4):
                print("Simulating scenario 4, please wait...")
                values_scenario4 = [0.01, 0.1, 0.25]
                aux_scenario4(values_scenario4)
                break
            elif(option == 5):
                print("Simulating scenario 5, please wait...")
                values_scenario5 = [0.5, 0.7, 0.9]
                aux_scenario5(values_scenario5)
                break
            elif(option == 6):
                print("Simulating hack scenario, please wait...")
                values_hack_scenario = [(0.1, 0.5), (0.1, 0.7), (0.1, 0.9), (0.5, 0.5), (0.5, 0.7), (0.5, 0.9), (1.0, 0.5), (1.0, 0.7), (1.0, 0.9)]
                aux_hack_scenario(values_hack_scenario)
                break
            else:
                print("Entered number does not corrrespond to any scenario.")

main()