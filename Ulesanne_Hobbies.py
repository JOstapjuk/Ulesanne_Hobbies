"""Hobbies but OOP."""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list, age: int):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        :param age: age of the person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies
        self.age = age

    @property
    def full_name(self) -> str:
        """
        Get person's full name.

        Combination of first and last name.
        """
        return str(self.first_name) + " " + str(self.last_name)

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    filtered_list = []
    for person in people_list:
        if hobby in person.hobbies:
            filtered_list.append(person)
    return filtered_list



def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_list = sorted(people_list, key=lambda person: (-len(person.hobbies), person.full_name))   #key=lambda https://blogboard.io/blog/knowledge/python-sorted-lambda/
    return sorted_list
    




def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_list = sorted(people_list, key=lambda person: (len(person.hobbies), person.full_name))
    return sorted_list


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return the list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_people = sorted(people_list, key=lambda person: person.full_name)
    
    for person in sorted_people:
        person.hobbies.sort()
    
    return sorted_people

# Добавила свой метод

def sort_people_by_age(people_list: list) -> list:
    """
    Return list of peoples names sorted ascending by their age

    :param people_list: list of people to sort
    :return: sorted list of people
    """
    sorted_people = sorted(people_list, key=lambda person: person.age)
    return sorted_people


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"], 18)
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"], 60)
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"], 52)
    person4 = Person("Kati", "Vuuola", ["programming","skiing","sleeping","eating"],25)
    people = [person1, person2, person3,person4]

    print("People sorted by most hobbies")
    print(sort_by_most_hobbies(people))  # -> [Jeff Bezos, Elon Musk, Mari Kukk]
    print()

    print("People sorted by least hobbies")
    print(sort_by_least_hobbies(people))   # -> [Elon Musk, Mari Kukk, Jeff Bezos]
    print()

    print("People who have a given hobbie in their list")
    print(filter_by_hobby(people, "space"))  # -> [Elon Musk, Jeff Bezos]
    print()

    print("People sorted by their full names and hobbies")
    sorted_people = sort_people_and_hobbies(people)
    print(sorted_people)  # -> [Elon Musk, Jeff Bezos, Mari Kukk]
    for person in sorted_people:
        print(f"{person.full_name} hobbies: {person.hobbies}")
    print()

    print("Hobbies of a person")
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']
    print()

    print("People sorted by their age")
    sorted_people_age = sort_people_by_age(people)
    print(sorted_people_age)
    for person in sorted_people_age:
        print(f"{person.full_name} age: {person.age}")
