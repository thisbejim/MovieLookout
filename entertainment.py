import movies
import fresh_tomatoes

# Create movie classes
master_and_commander = movies.Movie("Master and Commander",
                                    "assets/mc_poster.jpg",
                                    "https://www.youtube.com/watch?v=5kLoPYkYs9I",
                                    "Russell Crowe",
                                    "Paul Bettany",
                                    "Billy Boyd",
                                    "Peter Weir",
                                    "3")

lord_of_the_rings = movies.Movie("Lord of the Rings",
                                 "assets/l_poster.jpg",
                                 "https://www.youtube.com/watch?v=Pki6jbSbXIY",
                                 "Elijah Wood",
                                 "Ian McKellen",
                                 "Viggo Mortensen",
                                 "Peter Jackson",
                                 "4")

monsters_inc = movies.Movie("Monsters Inc",
                            "assets/m_poster.jpg",
                            "https://www.youtube.com/watch?v=8IBNZ6O2kMk",
                            "John Goodman",
                            "John Goodman",
                            "Steve Buscemi",
                            "Pete Docter",
                            "4")

hercules = movies.Movie("Hercules",
                        "assets/h_poster.jpg",
                        "https://www.youtube.com/watch?v=NDMZHhcBHaQ",
                        "Tate Donovan",
                        "Danny DeVito",
                        "James Woods",
                        "Ron Clements",
                        "3")

the_darjeeling_limited = movies.Movie("The Darjeeling Limited",
                                      "assets/d_poster.png",
                                      "https://www.youtube.com/watch?v=aO1bYukdvLI",
                                      "Owen Wilson",
                                      "Adrien Brody",
                                      "Jason Schwartzman",
                                      "Wes Anderson",
                                      "3")

v_for_vendetta = movies.Movie("V for Vendetta",
                              "assets/v_poster.jpg",
                              "https://www.youtube.com/watch?v=6rRn8kM4-ds",
                              "Natalie Portman",
                              "Hugo Weaving",
                              "John Hurt",
                              "James McTeigue",
                              "4")


shows = [master_and_commander, lord_of_the_rings, monsters_inc, hercules, the_darjeeling_limited, v_for_vendetta]
fresh_tomatoes.open_movies_page(shows)
