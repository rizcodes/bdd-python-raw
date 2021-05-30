# bdd-python-raw
BDD demo for python automation using Behave framework


```
behave features/covid_vaccination.feature 
Feature: Covid Vaccination. # features/covid_vaccination.feature:1
  Users should be able to receive Covid vaccination
  Where elder citizens are given priority than rest.
  Scenario: Elder users arriving for vaccination should receive vaccine shots without delay  # features/covid_vaccination.feature:5
    Given a user with age 55 and above                                                       # features/steps/covid_vaccination.py:8 0.000s
    When the user is moved to express counter                                                # features/steps/covid_vaccination.py:13 0.000s
    Then the user received vaccine shot                                                      # features/steps/covid_vaccination.py:18 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```
