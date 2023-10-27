"""
Random Quote Generator Script 
Start Time: 9:14pm
Finish Time:

Objective: Create a Random Quote Generator with as much creativity as possible.

Chatgpt assisted with creating lists of nouns verbs and adjectives. everything else was written by me.

"""
import random
import pytest


noun_list = [
    "Ability", "Access", "Accident", "Account", "Act", "Action", "Activity", "Actor", "Ad", "Addition",
    "Address", "Administration", "Advantage", "Advertising", "Advice", "Affair", "Age", "Agency", "Agreement",
    "Air", "Airport", "Alcohol", "Ambition", "Amount", "Analysis", "Analyst", "Animal", "Answer", "Anxiety",
    "Apartment", "Appearance", "Apple", "Application", "Appointment", "Area", "Argument", "Army", "Arrival",
    "Art", "Article", "Aspect", "Assignment", "Assistance", "Assistant", "Association", "Assumption", "Atmosphere",
    "Attempt", "Attention", "Attitude", "Audience", "Aunt", "Average", "Awareness"
]


verb_list = [
    "Accept", "Ache", "Acknowledge", "Act", "Add", "Admire", "Admit", "Admonish", "Adopt", "Advise",
    "Affirm", "Afford", "Agree", "Ail", "Alert", "Allege", "Allow", "Allude", "Amuse", "Analyze",
    "Announce", "Annoy", "Answer", "Apologize", "Appeal", "Appear", "Applaud", "Appreciate", "Approve", "Argue",
    "Arrange", "Arrest", "Arrive", "Articulate", "Ask", "Assert", "Assure", "Attach", "Attack", "Attempt",
    "Attend", "Attract", "Auction", "Avoid", "Avow"
]

adjective_list = [
    "attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit",
    "flabby", "glamorous", "gorgeous", "handsome", "long", "magnificent", "muscular", "plain", "plump", "quaint",
    "scruffy"
]


"""
Mad Lib 1: The Great Adventure

Once upon a time, in a [adjective] land, there lived a brave [noun].
This [noun] was known far and wide for their [adjective] [plural noun]. One day, they embarked on a [adjective] adventure to find the legendary [noun]. 
Along the way, they encountered a [adjective] [animal], who offered to be their [adjective] companion. Together, they faced many [adjective] challenges and overcame [number] obstacles. 
In the end, they found the [noun], and it was [adjective] beyond their wildest dreams.

Mad Lib 2: The Surprise Party

It was [day of the week], and [name] was planning a surprise party for [friend's name]. [Name] secretly invited [number] [adjective] friends to the party and bought a [color] [noun] as a gift. They decorated the [adjective] [place] with [plural noun] and [adjective] streamers. [Friend's name] was [adjective] surprised when they walked into the room and saw their friends yelling, "Happy [adjective] birthday!" The party was a [adjective] success, and everyone had a [adjective] time.

Mad Lib 3: The Haunted House

One [season], a group of [number] [adjective] friends decided to visit a [adjective] haunted house. 
As they entered, they heard [spooky sound] coming from the [room]. The [adjective] walls were covered in [noun], and there were [number] [adjective] [animal] roaming around. 
They cautiously made their way to the [room] where they found a [color] [noun]. 
Suddenly, the [noun] started [verb ending in -ing], and they all screamed and ran out of the house as fast as their [body part] could carry them.

"""
def mad_lib_one():
    print("")

def mad_lib_two():
    print("")

def mad_lib_three():
    print("")


def main():
    t = True
    while t == True:
        mad_lib_choice = input("Enter a number 1 ,2 or 3:")
        if mad_lib_choice is int and mad_lib_choice < 4 and mad_lib_choice > 0:
            if mad_lib_choice == 1:
                mad_lib_one()
                t = False
            elif mad_lib_choice == 2:
                mad_lib_two()
                t = False
            else:
                mad_lib_three()
                t = False



if __name__ == "__main__":
    main()