Feature: Playground UI Testing

  Scenario: Verify Button Click
    Given I navigate to the click page
    When I click the button
    Then the button class should change to "btn-success"


  Scenario: Verify Text Input
    Given I navigate to the text input page
    When  I set the text "New Button Name" into the input field
    And I press the button
    Then the button text should be changed to "New Button Name"
