import random

def generate_story():
    characters = ['Alice', 'Bob', 'Charlie', 'David']
    actions = ['found a treasure', 'went on an adventure', 'discovered a hidden cave', 'solved a mystery']
    places = ['in a magical forest', 'underneath the old oak tree', 'on top of a mountain', 'by the riverbank']

    story_length = random.randint(50, 100)  # Generate a story with up to 100 words
    story = []

    for _ in range(story_length):
        character = random.choice(characters)
        action = random.choice(actions)
        place = random.choice(places)

        sentence = f"{character} {action} {place}."
        story.append(sentence)

    return ' '.join(story)

if __name__ == "__main__":
    story = generate_story()
    print(story)
