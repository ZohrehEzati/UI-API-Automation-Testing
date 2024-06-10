Feature: Petstore API Testing

  Scenario: Add A New Pet To The Store
    Given a new pet with ID 20, name "babi", and status "available"
    When I send a POST request to the /pet endpoint
    Then The response status code should be 200
    And the response body should be equal to pet's details


  Scenario: Find Pets By ID
    Given a pet with ID of 20 exists
    When I send the GET request to the /pet/20 endpoint
    Then The response status code should be 200
    And the response body should be equal to the pet details

