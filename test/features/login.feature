Feature: Login promt

  Scenario: Login to site
     Given we have opened the browser for "http://ixion-tech.com.ar:8000/admin"
      When we input login data "seal|seal"
      Then we enter in the page with this title "Site administration | Django site admin"
      And we logout and close de browser

