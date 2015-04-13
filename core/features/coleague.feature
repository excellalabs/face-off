Feature: visiting col-league

#Scenario: visit col-league and check
#  When we visit col-league
#  Then it should have the title "Sign In"

Scenario: In practice mode, a user clicking a card should cause all the cards to flip
  Given the user has logged into the Face Off application
  And they are in practice mode
  When the user clicks the first card
  Then all the cards should flip