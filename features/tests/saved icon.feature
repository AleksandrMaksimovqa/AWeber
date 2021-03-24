# Created by Strel at 3/24/2021
Feature: Tests for AWeber

  Scenario: Verify that "Settings saved successfully!" icon appears after the change was made
    Given Open wordpress profile page
    When Put Kelly in 'First name' field
    Then Click on the 'Save profile details' button
    And Verify icon appears


  Scenario: Verify that "Settings saved successfully!" text appears after the change was made
    Given Open wordpress profile page
    When Put John in 'First name' field
    Then Click on the 'Save profile details' button
    And Verify text