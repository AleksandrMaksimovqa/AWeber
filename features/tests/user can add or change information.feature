# Created by Aleksandr at 3/23/2021
Feature: Tests for AWeber
#NOTE!!! Do not launch test twice with the same name.


  Scenario: Verify that user can add or change First Name
    Given Open wordpress profile page
    When Put Aleksandr in 'First name' field
    Then Click on the 'Save profile details' button
    And Verify first name saved successfully!


    Scenario: Verify that user can add or change Last Name
      Given Open wordpress profile page
      When Put Maksimov21 in 'Last name' field
      Then Click on the 'Save profile details' button
      And Verify last name saved successfully!


    Scenario: Verify that user can add or change Public display name
      Given Open wordpress profile page
      When Put Luke21 in 'Public display name' field
      Then Click on the 'Save profile details' button
      And Verify Public display name saved successfully!


    Scenario: Verify that user can add or change About me field
      Given Open wordpress profile page
      When Put I am a QA Engineer!21 in 'About me' field
      Then Click on the 'Save profile details' button
      And Verify About me field saved successfully!


    Scenario: Verify that user can add URL
      Given Open wordpress profile page
      When Click on 'Add' button
      And Click on 'Add URL' button
      Then Enter www.google.com and Google21
      And Click 'Add site' button


    Scenario: Verify 'Cancel' button functionality in profile links section
      Given Open wordpress profile page
      When Click on 'Add' button
      And Click on 'Add URL' button
      Then Enter www.google.com and Google21
      And Click 'Cancel' button


    Scenario: Verify that user can remove URL
      Given Open wordpress profile page
      Then Click on 'Remove' button

    Scenario: Verify that user can add WordPress Site
      Given Open wordpress profile page
      When Click on 'Add' button
      And Click on 'Add WordPress Site' button
      Then Click on checkbox
      And Click 'Add sites' button


    Scenario: Verify that user can remove WordPress Site
      Given Open wordpress profile page
      Then Click on 'Remove' button


    Scenario: Verify 'your profile' link
      Given Open wordpress profile page
      Then Click on 'your profile' link


    Scenario: Verify 'Gravatar Hovercards' link
      Given Open wordpress profile page
      Then Click on 'Gravatar Hovercards' link