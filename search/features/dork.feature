Feature: My Lists
  As a logged-in user
  I want to create dorks
  So that I can see them all after I've created them

  Scenario: Create a dork and see it on "My dork page"

    Given I am a logged-in user

    When I create a dork "LinuxFr" with "inurl:linuxfr.org"

    Then I will see a link to "LinuxFr"

    When I click the link to "LinuxFr"
    Then I will see the dork name "LinuxFr"
    And  I will see the dork content "inurl:linuxfr.org"
