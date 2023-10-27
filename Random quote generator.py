"""
Random Quote Generator Script 
Start Time: 9:14pm
Finish Time:10:15pm

Objective: Create a Random Quote Generator with as much creativity as possible.

Chatgpt assisted with creating lists of nouns verbs and adjectives. everything else was written by me.

"""
import random


noun_list = [
    "Ability", "Access", "Accident", "Account", "Act", "Action", "Activity", "Actor", "Ad", "Addition",
    "Address", "Administration", "Advantage", "Advertising", "Advice", "Affair", "Age", "Agency", "Agreement",
    "Air", "Airport", "Alcohol", "Ambition", "Amount", "Analysis", "Analyst", "Animal", "Answer", "Anxiety",
    "Apartment", "Appearance", "Apple", "Application", "Appointment", "Area", "Argument", "Army", "Arrival",
    "Art", "Article", "Aspect", "Assignment", "Assistance", "Assistant", "Association", "Assumption", "Atmosphere",
    "Attempt", "Attention", "Attitude", "Audience", "Aunt", "Average", "Awareness"
]


adjective_list = [
    "attractive", "bald", "beautiful", "chubby", "clean", "dazzling", "drab", "elegant", "fancy", "fit",
    "flabby", "glamorous", "gorgeous", "handsome", "long", "magnificent", "muscular", "plain", "plump", "quaint",
    "scruffy"
]

def again():
    while True:
        user_cont = input("do you want to try again? (Y to continue, anything else to stop)")
        if user_cont == "Y":
            main()
        else:
            break

def random_adjective():
    rand_adjective = str(random.choice(adjective_list))
    return rand_adjective


def random_noun():
    rand_noun = str(random.choice(noun_list))
    return rand_noun


def mad_lib_one():
    print("Mad Lib 1: The Great Adventure Once upon a time, in a " + random_adjective() + " land, there lived a brave " + random_noun() + ". \n This " + random_noun() + " was known far and wide for their " + random_adjective() + " " + random_noun() + ". \n One day, they embarked on a " + random_adjective() + " adventure to find the legendary " + random_noun() + ".  \n Along the way, they encountered a " + random_adjective(
    ) + " lion, who offered to be their " + random_adjective() + " companion.\n Together, they faced many " + random_adjective() + " challenges and overcame obstacles.\n In the end, they found the " + random_noun() + ", and it was " + random_adjective() + " beyond their wildest dreams.")
    again()

def main():
    t = True
    while t:
        try:
            mad_lib_choice = int(input("Enter a number 1 ,2 or 3:"))
            if mad_lib_choice < 2 and mad_lib_choice > 0:
                if mad_lib_choice == 1:
                    mad_lib_one()
                    break
        except Exception as e:
            print("well the problem is that there is an " +
                  str(e) + " is not a number!")


if __name__ == "__main__":
    main()
