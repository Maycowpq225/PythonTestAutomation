Feature: create account

  Background: Create user and go to authentication page
    Given a new user is created
    When user is on the logged out home page
    And click on sign in button on logged out home
    Then validate the authentication page

  @web @createAccount
  Scenario: Create an account with valid credentials
    When fill the field register email
    And click on create an account
    Then validate the cadastral page
    When fill fields personal information
    And fill fields your address
    And click on register button
    Then validate my account page

  @web @createAccount
  Scenario Outline: Create an account with invalid emails
    When fill the field email with <emails>
    And click on create an account
    Then validate the error message "Invalid email address."

    Examples: invalids emails
      | emails             |
      | joao16666gmail.com |
      | joao1666@gmailcom  |
      | @gmail.com         |
      | joao553235         |

  @web @createAccount
  Scenario: Create an account without fill registrations fields
    When fill the field register email
    And click on create an account
    Then validate the cadastral page
    When click on register button
    Then validate the error message "There are 8 errors"





