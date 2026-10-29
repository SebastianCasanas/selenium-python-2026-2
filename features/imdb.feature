Feature: Buscar pelicula en IMDb

  Scenario: Buscar Pulp Fiction y validar su calificacion
    Given the user is on the IMDb home page
    When the user searches for the movie "Pulp fiction"
    And the user opens the first result
    Then the movie rating should be displayed
