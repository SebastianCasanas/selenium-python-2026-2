Feature: Lobby

  Scenario: Ingresar con un nombre unico a la lobby
    Given the user is on the lobby page
    When the user joins with a unique name
    Then the user should see their name in the lobby

  Scenario: Validar error con un nombre que contiene espacios
    Given the user is on the lobby page
    When the user joins with the name "Sebastian Casanas"
    Then a name error message should be displayed
