# 🎭 Mad Libs Generator in Python

def mad_libs():
    """
    A simple Mad Libs game.
    User provides words (noun, verb, adjective, etc.), and
    they are inserted into a funny story template.
    """

    print("🎉 Welcome to the Mad Libs Generator!")
    print("Please provide words as prompted, and I'll create a story for you.\n")

    # Asking user for different types of words
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (present tense): ")
    place = input("Enter a place: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    noun2 = input("Enter another noun: ")
    emotion = input("Enter an emotion: ")

    # Story template with placeholders
    story = f"""
    Once upon a time, in a {adjective1} land, there was a {noun1}.
    Every day, it loved to {verb1} at {place}.
    One day, it met a {adjective2} {animal} who was eating {food}.
    Together, they found a magical {noun2} that made them feel very {emotion}.
    And they lived happily ever after! 🎉
    """

    # Printing the final story
    print("\n--- Your Mad Libs Story ---")
    print(story)


# Run the game
if __name__ == "__main__":
    mad_libs()
