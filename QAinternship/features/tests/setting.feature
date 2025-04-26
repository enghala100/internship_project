# Created by engha at 4/25/2025
Feature:testing setting page


  Scenario: User can go to settings and see the right number of UI elements
    Given Open the main page
    When Log in to the page
    And Click on the settings option
    Then Verify the right page opens
    And Verify there are 13 options for the settings
    And Verify the “connect the company” button is available
