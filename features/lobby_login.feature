Feature: Login Feature

  Scenario: Ingresar con un nombre único a la lobby
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con el nombre "SebasCasanas"
    Then El nombre del usuario "SebasCasanas" aparece en el dashboard

  Scenario: Validar mensaje de error con un nombre que contiene espacios
    Given El usuario se encuentra en la página de login
    When El usuario ingresa con el nombre "Sebas Casanas"
    Then Se muestra un mensaje de error
