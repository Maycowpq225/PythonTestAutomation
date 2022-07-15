#Feature: Login
#
#  Background:
#    Given user is on the logged out home page
#    And click on sign in button logged out home
#    Then validate the authentication page
#
#  Scenario: Login with valids credentials
#    When fill the fields email with "JoaoAlberto12345@gmail.com" and password "010203"
#    And click on sign button
#    Then validate my account page
#
#  Scenario: Login with invalids credentials
#    When fill the fields email with "JoaoAlberto12345@gmail.com" and password "090807"
#    And click on sign button
#    Then validate the message error "Password is required"
