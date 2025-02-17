Agency now has:
astronauts (One-to-Many with Astronaut).
discovered_planets (One-to-Many with Planet).

Astronaut now has:
agency (Many-to-One with Agency).
spacecrafts (Many-to-Many with Spacecraft).

Planet now has:
discovered_by (Many-to-One with Agency).
spacecrafts (Many-to-Many with Spacecraft).

Mission now includes:
astronauts (Many-to-Many with Astronaut).

Spacecraft now has:
astronauts (Many-to-Many with Astronaut).
planets (Many-to-Many with Planet).
