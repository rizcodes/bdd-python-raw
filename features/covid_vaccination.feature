Feature: Covid Vaccination.
  Users should be able to receive Covid vaccination
  Where elder citizens are given priority than rest.

  Scenario: Elder users arriving for vaccination should receive vaccine shots without delay
    Given a user with age 55 and above
    When the user is moved to express counter
    Then the user received vaccine shot
