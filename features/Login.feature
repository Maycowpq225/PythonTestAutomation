Feature: Login

  Background: Going to authentication page
    Given user is on the logged out home page
    And click on sign in button on logged out home
    Then validate the authentication page

  @web @login
  Scenario: Login with valids credentials
    When fill the login fields email with JoaoAlberto12345@gmail.com and password 010203
    And click on sign in button
    Then validate my account page

  @web @login
  Scenario: Login with invalids credentials
    When fill the login fields email with JoaoAlberto12345@gmail.com and password 090807
    And click on sign in button
    Then validate the error message "Authentication failed."
