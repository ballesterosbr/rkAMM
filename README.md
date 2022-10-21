# Reverse Kelly AMM (rkAMM)

This repository aims to offer the performance and simulation of the rkAMM based on different scenarios.

# Index
- [Requirements](#requirements)
- [How to test the rkAMM](#how-to-test-the-rkamm-simulator)
    - [Option 1 - Jupyter Notebook](#option-1---jupyter-notebook)
    - [Option 2 - Running from `test.py` file](#option-2---running-from-testpy-file)
- [FAQs](#faqs)
- [Can I change the parameters of the simulation?](#can-i-change-the-parameters-of-the-simulation)
- [Can I create my own scenario?](#can-i-create-my-own-scenario)

## Requirements

Recommended Python version: `3.10`

Libraries:
- `matplotlib 3.5.3`
- `numpy 1.23.2`

## How to test the rkAMM simulator

There two possible options to test the rkAMM simulator

### Option 1 - Jupyter Notebook

A Jupyter Notebook has been developed to facilitate the simulation of the rkAMM. Please check that you have the above libraries installed.

**IMPORTANT** In case you cannot execute any simulation, the notebook is offered with an execution already carried out so that you can observe the results obtained.

See the [rkAMM Jupyter Notebook]()

### Option 2 - Running from `test.py` file

#### Clone this repository

`$ git clone https://github.com/ballesterosbr/rkAMM.git`

#### Navigate to the repository root folder

`$ cd rkAMM`

#### Run the simulator

`$ python test.py`

In the menu shown you will need to enter the number of the scenario to simulate:

```
Choose an scenario to simulate: 
 1. Scenario 1 
 2. Scenario 2 
 3. Scenario 3 
 4. Scenario 4 
 5. Scenario 5 
 6. Hack Scenario 
 Scenario: 
```

Below is provided a brief explanation of the scenarios:

- *Scenario 1 - There is a contribution of collateral by liquidity providers (LP) based on a growing rate concerning the volume of collateral ($Q$) in the AMM.*

- *Scenario 2 - Non-collateralized amount of a set of invoices is not repaid to the AMM.*

- *Scenario 3 - Increasing delay in invoice payments.* 

- *Scenario 4 - Amount to be collateralized depends on a variable percentage of the initial volume of collateral ($Q_0$) in the AMM.*

- Scenario 5 - *Different % to be collateralized  with the same amount of invoices.*

- *Hacking scenario - These scenarios foresee a hack of the AMM, that is, there is a high number of false, bogus invoices. A false invoice is considered one for which the collateral given away by the AMM will never be paid back. The purpose of this hack from the attacker's point of view is to drain the AMM liquidity.*

#### Results

After selecting a scenario, the simulation will run resulting in a set of tables and figures. An example if offered below:

```
Simulating scenario 2, please wait...
---------------------------------------------------------------------------------------------------------
| Description                                        | Value                                            |
---------------------------------------------------------------------------------------------------------
| Number of simulations                              | 10                                               |
| Simulation time period                             | 650 days                                         |
| Total of invoices                                  | 500                                              |
| Average of accepted invoices (collateralized)      | 102.4 out of 500 invoices in 650 days (20.48 %)  |
| Average of paid invoices (capital returned)        | 99.4 out of 102.4 collateralized invoices        |
| Average of unpaid invoices (capital not returned)  | 3.0 out of 102.4 collateralized invoices         |
| Average loss due to unpaid invoices                | 1913.6                                           |
| Total collateral covered                           | 60837.2 in 102.4 collateralized invoices         |
| Total collateral covered x (i.c.)                  | 6.084 x initial collateral                       |
| Total premium obtained                             | 10422.25 in 102.4 collateralized invoices        |
| Total premium obtained x (i.c.)                    | 1.042 x initial collateral                       |
| Total AMM volume                                   | 18508.65 after 650 days                          |
| AMM profit percentage                              | 85.09 %                                          |
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
| Description                                        | Value                                            |
---------------------------------------------------------------------------------------------------------
| Number of simulations                              | 10                                               |
| Simulation time period                             | 650 days                                         |
| Total of invoices                                  | 500                                              |
| Average of accepted invoices (collateralized)      | 104.5 out of 500 invoices in 650 days (20.90 %)  |
| Average of paid invoices (capital returned)        | 100.4 out of 104.5 collateralized invoices       |
| Average of unpaid invoices (capital not returned)  | 4.1 out of 104.5 collateralized invoices         |
| Average loss due to unpaid invoices                | 2294.6                                           |
| Total collateral covered                           | 59975.2 in 104.5 collateralized invoices         |
| Total collateral covered x (i.c.)                  | 5.998 x initial collateral                       |
| Total premium obtained                             | 9964.43 in 104.5 collateralized invoices         |
| Total premium obtained x (i.c.)                    | 0.996 x initial collateral                       |
| Total AMM volume                                   | 17669.83 after 650 days                          |
| AMM profit percentage                              | 76.7 %                                           |
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
| Description                                        | Value                                            |
---------------------------------------------------------------------------------------------------------
| Number of simulations                              | 10                                               |
| Simulation time period                             | 650 days                                         |
| Total of invoices                                  | 500                                              |
| Average of accepted invoices (collateralized)      | 67.5 out of 500 invoices in 650 days (13.50 %)   |
| Average of paid invoices (capital returned)        | 53.2 out of 67.5 collateralized invoices         |
| Average of unpaid invoices (capital not returned)  | 14.3 out of 67.5 collateralized invoices         |
| Average loss due to unpaid invoices                | 8097.6                                           |
| Total collateral covered                           | 34706.3 in 67.5 collateralized invoices          |
| Total collateral covered x (i.c.)                  | 3.471 x initial collateral                       |
| Total premium obtained                             | 6021.14 in 67.5 collateralized invoices          |
| Total premium obtained x (i.c.)                    | 0.602 x initial collateral                       |
| Total AMM volume                                   | 7923.54 after 650 days                           |
| AMM profit percentage                              | -20.76 %                                         |
---------------------------------------------------------------------------------------------------------
```


## FAQs

## Can I change the parameters of the simulation?

Yes. In case you want to explore new possible situations based on the proposed scenarios, you can modify the values used in different scenarios in the `test.py` file.

We highly recommend read the paper before changing the parameters.

## Can I create my own scenario?

Currently, rkAMM is not prepared to support arbitrary cases. You would need to implement your scenario based on the rkAMM defined in the `aux.py` file. Then, in order to correctly simulate the scenario you would need to enter valid values.

We highly recommend you contact us if you want to verify any particular scenario.