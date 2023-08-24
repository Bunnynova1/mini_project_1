import random

# Templates for the Mad Libs stories
template_1 = ''' 
It was about {number} {measure of time} ago when I arrived at the hospital in a {mode of transportation}.
The hospital is a/an {adjective 1} place, there are a lot of {adjective 2} {noun 1} here. There are nurses here who have
{color} {part of the body}. If someone wants to come into my room I told them that they have to {verb 1} first.
I’ve decorated my room with {number 2} {noun 2}. Today I talked to a doctor and they were wearing a {noun 3} on their
{part of the body 2}. I heard that all doctors {verb 2} {noun 4} every day for breakfast. The most {adjective 3} thing
about being in the hospital is the {silly word} {noun 5}! 
'''

template_2 = ''' 
This weekend I am going camping with {person name}. I packed my lantern, sleeping bag, and {noun 1}.
I am so {adjective feeling 1} to {verb 1} in a tent. I am {adjective feeling 2} we might see a {animal},
I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb 2}.
I have heard that the {color 1} lake is great for {verb ing 3}. Then we will {adverb ly} hike through the forest
for {number 1} {measure of time}. If I see a {color 2} {animal} while hiking, I am going to bring it home as a pet!
At night we will tell {number 2} {silly word} stories and roast {noun 2} around the campfire!! 
'''

template_3 = ''' 
Dear {person name}, I am writing to you from a {adjective 1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective 2}
{magical creature(plural) 1} and {adjective 3} {magical creature(plural) 2} here! In the {room in a house}
there is a pool full of {noun 1}. I fall asleep each night on a {noun 2} of {noun(plural) 3} and dream of
{adjective 4} {noun(plural) 4}. It feels as though I have lived here for {number} {measure of time}.
I hope one day you can visit, although the only way to get here now is {verb(ending in ing)} on a {adjective 5}
{noun 5}!! 
'''


# Function to get user input
def get_input(prompt, placeholder):
    while True:
        user_input = input(f"Enter {prompt}: ")
        if user_input:
            return user_input
        else:
            print(f"You must provide input for {placeholder}. Try again.")


# Function to gather user input for all placeholders
def gather_input(placeholders):
    return {placeholder: get_input(placeholder, placeholder) for placeholder in placeholders}


# Main function to play the Mad Libs game
def madlibs_game(story):
    # Randomly select a story template
    selected_story = random.choice(['1', '2', '3'])

    if story == '1':
        selected_template = template_1
        placeholders = ['number', 'measure of time', 'mode of transportation', 'adjective 1', 'adjective 2', 'noun 1',
                        'color', 'part of the body', 'verb 1', 'number 2', 'noun 2', 'noun 3', 'part of the body 2',
                        'verb 2', 'noun 4', 'adjective 3', 'silly word', 'noun 5']
    elif story == '2':
        selected_template = template_2
        placeholders = ['person name', 'noun 1', 'adjective feeling 1', 'verb 1', 'adjective feeling 2', 'animal',
                        'verb 2', 'color 1', 'verb ing 3', 'adverb ly', 'number 1', 'measure of time', 'color 2',
                        'animal 2', 'number 2', 'silly word', 'noun 2']
    elif story == '3':
        selected_template = template_3
        placeholders = ['person name', 'adjective 1', 'color', 'animal', 'place', 'adjective 2',
                        'magical creature(plural) 1', 'adjective 3', 'magical creature(plural) 2',
                        'room in a house', 'noun 1', 'noun 2', 'noun(plural) 3', 'adjective 4', 'noun(plural) 4',
                        'number', 'measure of time', 'verb(ending in ing)', 'adjective 5', 'noun 5']

    else:
        print("Invalid story selection")
        return

    # Gather user input for placeholders
    template_placeholders = gather_input(placeholders)

    # Replace placeholders with user input in the selected template
    for placeholder, value in template_placeholders.items():
        selected_template = selected_template.replace(f'{{{placeholder}}}', value)

    # Print the filled Mad Libs story
    print(selected_template)


# Get user's selected story
selected_story = input("Choose a story (1, 2, or 3): ")
madlibs_game(selected_story)
