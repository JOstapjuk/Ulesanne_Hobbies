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
    sorted_list = sorted(people_list, key=lambda person: (-len(person.hobbies), person.full_name))
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
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"], 46)
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"], 50)
    people = [person1, person2, person3]

    print(sort_by_most_hobbies(people))  # -> [JeffBezos, ElonMusk, MariKukk]
    print()
    print(sort_by_least_hobbies(people))   # -> [ElonMusk, MariKukk, JeffBezos]
    print()
    print(filter_by_hobby(people, "space"))  # -> [ElonMusk, JeffBezos]
    print()
    sorted_people = sort_people_and_hobbies(people)
    print(sorted_people)  # -> [ElonMusk, JeffBezos, MariKukk]
    for person in sorted_people:
        print(f"{person.full_name} hobbies: {person.hobbies}")
    print()
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']
    print()
    sorted_people_age = sort_people_by_age(people)
    print(sorted_people_age)
    for person in sorted_people_age:
        print(f"{person.full_name} age: {person.age}")
