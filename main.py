template = """
   In the magical land of Narnia, there was a brave (adjective_1) (occupation_1) named (Name), 
   who was known throughout the realm for (pronoun_possessive) impressive (trait). One day, an urgent message 
   arrived from the (adjective_2) (royal_family_member) who ruled the neighboring kingdom of (Kingdom_name). The 
   message spoke of a (adjective_3) (creature) terrorizing the Land and causing chaos. (Name) knew (Pronoun_subject) 
   had to embark on a perilous journey to save the kingdom. Equipped with (pronoun_possessive) trusty (weapon) and 
   accompanied by (pronoun_possessive) loyal (Animal), (Pronoun_subject) set off at (time) towards the (direction) 
   mountains where the (creature) was said to reside. After days of traveling, (Pronoun_subject) reached the summit 
   of the mountain and confronted the (adjective_4) (creature). A fierce battle ensued, and with great courage, 
   (Name) managed to defeat the (creature). The kingdom of (Kingdom_name) celebrated (Name)'s bravery and awarded (
   pronoun_object) the hero of the realm. As a token of gratitude, the ruler gifted (pronoun_object) a (item) that 
   held unimaginable powers. With (pronoun_possessive) quest complete, (Name) returned to (pronoun_possessive) 
   homeland, forever remembered as a true hero."""



def replace_placeholders(template, replacements):
    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)
    return result


def madlib_story(story):
    pronouns = {"male": {"subject": "he", "object": "him", "possessive": "his"},
                "female": {"subject": "she", "object": "her", "possessive": "her"}}

    gender = input("Enter gender (male/female): ")
    if gender.lower() in pronouns:
        gender_pronouns = pronouns[gender.lower()]
    else:
        print("Gender not recognized. Using neutral pronouns.")
        gender_pronouns = {"subject": "they", "object": "them", "possessive": "their"}

    replacements = {
        "(Pronoun_subject)": gender_pronouns["subject"],
        "(pronoun_possessive)": gender_pronouns["possessive"],
        "(pronoun_object)": gender_pronouns["object"],
        "(adjective_1)": input('Enter an adjective: '),
        "(occupation_1)": input('Enter an occupation: '),
        "(Name)": input("Enter a person's name: ").capitalize(),
        "(trait)": input('Enter a trait/skill: '),
        "(adjective_2)": input('Enter an adjective: '),
        "(royal_family_member)": input('Enter a royal family member: ').capitalize(),
        "(Kingdom_name)": input('Enter a Kingdom name: ').capitalize(),
        "(adjective_3)": input('Enter an adjective: '),
        "(creature)": input('Enter a creature: ').capitalize(),
        "(weapon)": input('Enter a weapon: '),
        "(Animal)": input('Enter an animal: ').capitalize(),
        "(time)": input('Enter a time: '),
        "(direction)": input('Enter direction: '),
        "(adjective_4)": input('Enter an adjective: '),
        "(item)": input('Enter an item: ')
    }

    result = replace_placeholders(story, replacements)

    print("\nThe Story:")
    print(result)


if __name__ == "__main__":
    madlib_story(template)
