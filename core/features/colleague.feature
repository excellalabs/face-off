Feature: Face Off

Scenario: Visit Face Off and Check
  Given the user is at the Face Off application
  Then they should be at the home screen

Scenario: Login and Logout
  Given the user is at the Face Off application
  When they sign into the application through yammer with a picture
  Then they logout

Scenario: User with Photo
  Given the user is at the Face Off application
  When they sign into the application through yammer with a picture
  Then they should arrive at the begin game screen

Scenario: User without photo
  Given the user is at the Face Off application
  When they sign into the application through yammer with no picture
  Then they should arrive at the no photo game screen

Scenario: check educational mode
  Given the user has logged into the Face Off application
  When they are in practice mode
  And the user clicks the first card
  Then all the cards should flip

Scenario: Play through educational mode
  Given the user has logged into the Face Off application
  When they play through the Educational Mode
  Then they should arrive at the results page

Scenario: Going to the Metrics page
  Given the user has logged into the Face Off application
  When they play through the Educational Mode
  Then they should arrive at the results page
  And they should be able to select metrics
  And they should arrive at the metrics page

Scenario: check competitive mode
  Given the user has logged into the Face Off application
  When they are in competitive mode
  And the user clicks the first card
  Then all the cards should not flip

Scenario: Full competitive game play
  Given the user has logged into the Face Off application
  When they are in competitive mode
  W
