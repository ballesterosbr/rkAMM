# Reverse Kelly AMM (rkAMM)

This repository aims to offer the performance and simulation of the rkAMM based on different scenarios.

# Index
- [Requirements](#requirements)
- [Simulated Scenarios](#simulated-scenarios)
- [How to test the rkAMM](#how-to-test-the-rkamm-simulator)
- [FAQs](#faqs)
    - [Can I change the parameters of the simulation?](#can-i-change-the-parameters-of-the-simulation)
    - [Can I create my own scenario?](#can-i-create-my-own-scenario)

## Requirements

Recommended Python version: `3.10`

Libraries:
- `matplotlib 3.5.3`
- `numpy 1.23.2`
- `pandas 1.4.3`

## Simulated scenarios

The rkAMM simulates the following scenarios:

 1. Scenario 1 – Increasing Liquidity Through Time
 2. Scenario 2 – More and more Unpaid Invoices
 3. Scenario 3 – More and more Delay in the Invoice Payments
 4. Scenario 4 – Playing with Growing Invoices, therefore growing demanded collateral 
 5. Scenario 5 – Playing with Growing % of Collateral with a Same Invoice amount
 6. Hack Scenario 

Below is provided a brief explanation of them:

- *Scenario 1 - There is a contribution of collateral by liquidity providers (LP) based on a growing rate concerning the volume of collateral (Q) in the AMM.*

- *Scenario 2 - Non-collateralized amount of a set of invoices is not repaid to the AMM.*

- *Scenario 3 - Increasing delay in invoice payments.* 

- *Scenario 4 - Amount to be collateralized depends on a variable percentage of the initial volume of collateral (Q_0) in the AMM.*

- Scenario 5 - *Different % to be collateralized  with the same amount of invoices.*

- *Hacking scenarios - These scenarios foresee a hack of the AMM, that is, there is a high number of false, bogus invoices. A false invoice is considered one for which the collateral given away by the AMM will never be paid back. The purpose of this hack from the attacker's point of view is to drain the AMM liquidity.*

The following list shows the specific values ​​used for each scenario simulation.

```
- Scenario 1: Increasing Liquidity Through Time with prob. 50.0 % of adding 1.0 % of initial liquidity
- Scenario 1: Increasing Liquidity Through Time with prob. 50.0 % of adding 5.0 % of initial liquidity
- Scenario 1: Increasing Liquidity Through Time with prob. 50.0 % of adding 10.0 % of initial liquidity
- Scenario 1: Increasing Liquidity Through Time with prob. 50.0 % of adding 25.0 % of initial liquidity

- Scenario 2: More and more Unpaid Invoices. 2.0 % of unpaid invoices
- Scenario 2: More and more Unpaid Invoices. 5.0 % of unpaid invoices
- Scenario 2: More and more Unpaid Invoices. 20.0 % of unpaid invoices

- Scenario 3: More and more Delay in the Invoice Payments. Min delay: 30 days, Max delay: 60 days
- Scenario 3: More and more Delay in the Invoice Payments. Min delay: 60 days, Max delay: 90 days
- Scenario 3: More and more Delay in the Invoice Payments. Min delay: 90 days, Max delay: 120 days

- Scenario 4: Playing with Growing Invoices, therefore growing demanded collateral. Demanded collateral: 1.0 % of initial Q
- Scenario 4: Playing with Growing Invoices, therefore growing demanded collateral. Demanded collateral: 10.0 % of initial Q
- Scenario 4: Playing with Growing Invoices, therefore growing demanded collateral. Demanded collateral: 25.0 % of initial Q

- Scenario 5: Playing with Growing % of Collateral with a Same Invoice amount. 55.0 % collateralized
- Scenario 5: Playing with Growing % of Collateral with a Same Invoice amount. 75.0 % collateralized
- Scenario 5: Playing with Growing % of Collateral with a Same Invoice amount. 90.0 % collateralized
```

## How to test the rkAMM simulator

A set of Jupyter Notebooks have been developed to facilitate the simulation of the rkAMM. Please check that you have all the above libraries installed.

**IMPORTANT** In case you cannot execute the simulation, a set of simulated notebooks are offered with an execution already carried out so that you can observe the results obtained. Check out the [rkAMM Jupyter Simulated Notebooks](/notebooks/simulated/).

## FAQs

## Can I change the parameters of the simulation?

Yes. In case you want to explore new possible situations based on the proposed scenarios, you can modify the values used in different scenarios in notebook cell below the **Values for each scenario** title.

We highly recommend read the article before changing the parameters.

## Can I create my own scenario?

Currently, rkAMM is not prepared to support arbitrary cases. You would need to implement your own scenario based on the ones defined in the rkAMM notebooks. Then, in order to correctly simulate the scenario you would need to enter valid values.

Also, if you want to verify any particular scenario, we are available at:
- peplluis@byppay.com
- alberto.ballesterosr@uah.es
