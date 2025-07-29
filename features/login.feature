Feature: SauceDemo Login

  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the inventory page

  Scenario: Login fails with invalid credentials
    Given I am on the SauceDemo login page
    When I login with username "invalid_user" and password "wrong_password"
    Then I should see a login error message

  Scenario: Error message for locked-out user
    Given I am on the SauceDemo login page
    When I login with username "locked_out_user" and password "secret_sauce"
    Then I should see a locked out error message

  Scenario: All products are displayed on inventory page
    Given I am logged in as "standard_user" with password "secret_sauce"
    Then I should see 6 products on the inventory page

  Scenario: Each product shows name, price, image, and add-to-cart button
    Given I am logged in as "standard_user" with password "secret_sauce"
    Then each product should display a name, price, image, and add-to-cart button