Feature: visiting col-league

Scenario: visit col-league and check
  Given the user is at the Face Off application
  When they sign into the application through yammer
  Then they should arrive at the begin game screen