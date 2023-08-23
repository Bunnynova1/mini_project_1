import random


template_1 = '''
    It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}.
    The hospital is a/an {adjective_1} place, there are a lot of {adjective_2} {noun_1} here.
    There are nurses here who have {color} {part_of_the_body}.
    If someone wants to come into my room I told them that they have to {verb_1} first.
    I’ve decorated my room with {number_2} {noun_2}.
    Today I talked to a doctor and they were wearing a {noun_3} on their {part_of_the_body_2}.
    I heard that all doctors {verb_2} {noun_4} every day for breakfast.
    The most {adjective_3} thing about being in the hospital is the {silly_word} {noun_5}!
    '''

template_2 = '''
    This weekend I am going camping with {person_name}.
    I packed my lantern, sleeping bag, and {noun_1}. I am so {adjective_feeling_1} to {verb_1} in a tent.
    I am {adjective_feeling_2} we might see a {animal}, I hear they’re kind of dangerous.
    While we’re camping, we are going to hike, fish, and {verb_2}.
    I have heard that the {color_1} lake is great for {verb_ing_3}.
    Then we will {adverb_ly} hike through the forest for {number_1} {measure_of_time}.
    If I see a {color_2} {animal} while hiking, I am going to bring it home as a pet!
    At night we will tell {number_2} {silly_word} stories and roast {noun_2} around the campfire!!
    '''

template_3 = '''
    Dear {person_name}, I am writing to you from a {adjective_1} castle in an enchanted forest.
    I found myself here one day after going for a ride on a {color} {animal} in {place}.
    There are {adjective_2} {magical_creature(plural)_1} and {adjective_3} {magical_creature(plural)_2} here!
    In the {room_in_a_house} there is a pool full of {noun_1}.
    I fall asleep each night on a {noun_2} of {noun(plural)_3} and dream of {adjective_4} {noun(plural)_4}.
    It feels as though I have lived here for {number} {measure_of_time}.
    I hope one day you can visit, although the only way to get here now is {verb(ending_in_ing)} on a {adjective_5} {noun_5}!!
    '''


def get_input(prompt, placeholder):
    return input(f"Enter {prompt}: ")


def gather_input(placeholders):
    return {placeholder: get_input(placeholder.replace('_', ' '), placeholder) for placeholder in placeholders}


def madlibs_game(story):
    if story == '1':
        selected_template = template_1
        placeholders = ['number', 'measure_of_time', 'mode_of_transportation', 'adjective_1', 'adjective_2', 'noun_1',
                        'color', 'part_of_the_body', 'verb_1', 'number_2', 'noun_2', 'noun_3', 'part_of_the_body_2',
                        'verb_2', 'noun_4', 'adjective_3', 'silly_word', 'noun_5']
    elif story == '2':
        selected_template = template_2
        placeholders = ['person_name', 'noun_1', 'adjective_feeling_1', 'verb_1', 'adjective_feeling_2', 'animal',
                        'verb_2', 'color_1', 'verb_ing_3', 'adverb_ly', 'number_1', 'measure_of_time', 'color_2',
                        'animal_2', 'number_2', 'silly_word', 'noun_2']
    elif story == '3':
        selected_template = template_3
        placeholders = ['person_name', 'adjective_1', 'color', 'animal', 'place', 'adjective_2',
                        'magical_creature(plural)_1', 'adjective_3', 'magical_creature(plural)_2',
                        'room_in_a_house', 'noun_1', 'noun_2', 'noun(plural)_3', 'adjective_4', 'noun(plural)_4',
                        'number', 'measure_of_time', 'verb(ending_in_ing)', 'adjective_5', 'noun_5']

    else:
        print("Invalid story selection")
        return

    template_placeholders = gather_input(placeholders)

    for placeholder, value in template_placeholders.items():
        selected_template = selected_template.replace(f'{{{placeholder}}}', value)

    print(selected_template)


selected_story = input("Choose a story (1, 2, or 3): ")
madlibs_game(selected_story)
