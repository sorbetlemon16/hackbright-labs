"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    species = set()

    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[str]: a list of names
    """

    villagers = []

    data = open(filename)

    for line in data:
        name, species = line.rstrip().split("|")[:2]

        if search_string in ("All", species):
            villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    data = open(filename)

    for line in data:
        # The `_` is a way to say, "Hey don't worry about this variable
        # because we'll never use it --- we only care about `first`,
        # `last`, and `cohort_name`.
        #
        # Python doesn't handle underscores in a special way or anything ---
        # it's still just a variable name.
        name, _, _, hobby, _ = line.rstrip().split("|")

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(fashion),
        sorted(play),
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).
    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data = open(filename)

    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Arguments:
      - filename (str): the path to a data file
      - villager_name (str): a person's full name

    Return:
      - str: the person's motto or None
    """

    for name, _, _, _, motto in all_data(filename):
        if name == villager_name:
            return motto


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
      - filename (str): the path to a data file
      - villager_name (str): a person's full name

    Return:
      - set: the set of the names of villagers with the same personality as the
      given villager.
    """

    likeminded = set()

    target_personality = None
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]

        if name == villager_name:
            target_personality = personality
            break

    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == target_personality:
                likeminded.add(name)

    return likeminded
