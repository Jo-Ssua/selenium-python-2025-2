Feature: Buscar una película y validar su nombre y rating
  Scenario: Validar el nombre y rating de la película inception
    Given el usuario esta en el home page de imdb
    When el usuario busca la película "inception"
    And el usuario selecciona el primer resultado de la busqueda
    Then el nombre de la película debe ser "Origen"
    And el rating de la película debe ser "8,8"