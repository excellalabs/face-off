Feature: visiting col-league

Scenario: visit col-league and check
  Given the user is at the Face Off application
  When they sign into the application through yammer
  Then they should arrive at the begin game screen

Scenario: check educational mode
  Given the user has logged into the Face Off application
  When they are in practice mode
  And the user clicks the first card
  Then all the cards should flip