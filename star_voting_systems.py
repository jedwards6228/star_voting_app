from random import randint


def ballot_action_failed(reason=""):
    return print(f"Ballot action failed.\n{reason}")


# Check user input for incorrect values or data types
def check_user_input(choice_criteria=None, choice=None, value=None, dict_object=None):
    error_list = []
    combined_error_string = ""
    # Checks all the user input that may be used and returns a useful message for troubleshooting
    if choice_criteria is not None:
        if not isinstance(choice_criteria, str):
            error_list.append(f"Choice criteria provided was not a string: {choice_criteria}")
    if choice is not None:
        if not isinstance(choice, str):
            error_list.append(f"Choice provided was not a string: {choice}")
    if value is not None:
        if not isinstance(value, int):
            error_list.append(f"Value assigned to choice '{choice}' is not an integer.")
    if dict_object is not None:
        if not isinstance(dict_object, dict):
            error_list.append(f"A non-dictionary object was passed into a field that requires a dictionary")

    # Combine errors into a single string and return them if any
    for error in error_list:
        combined_error_string = combined_error_string + error + "\n"
    if len(error_list) == 0:
        return True
    else:
        ballot_action_failed(combined_error_string)
        return False


# Create a class to represent a ballot
class Ballot:
    def __init__(self, ballot_id, user_id='Anonymous'):
        # user id can be set or Anonymous will be used by default
        self.user_id = user_id
        # Ballot ID will allow multiple ballots to exist and sync choices/criteria
        self.unique_ballot_id = ballot_id
        # A dictionary to contain "questions" with the key being another dictionary {question: dict(answer:value)}
        self.choice_criteria_dict = {}
        # Min and Max STAR rating for
        self.value_parameters = (0, 5)

    # Add a question or framework for choices, can pass a dictionary of choices
    def add_choice_criteria(self, choice_criteria, choices=None):
        if choices is None:
            choices = {}
        if not isinstance(choices, dict):
            return ballot_action_failed(f"Choices must be entered as a dictionary containing the choice:value")
        if choice_criteria in self.choice_criteria_dict:
            return print(f"Cannot add {choice_criteria} to choice criteria as it already exists")
        self.choice_criteria_dict[str(choice_criteria)] = choices

    # Add a choice to the inner dictionary and provide a value or default to 0
    def add_choice(self, choice_criteria, choice, value=0):
        if not check_user_input(choice_criteria, choice, value):
            return
        # Check that the value is within the ballot's value parameters
        if not self.value_parameters[0] <= value <= self.value_parameters[-1]:
            return ballot_action_failed(f"Cannot assign a value below {self.value_parameters[0]} or above "
                                        f"{self.value_parameters[-1]}.")
        self.choice_criteria_dict[str(choice_criteria)][str(choice)] = value
        return

    # Change the value of an existing choice
    def assign_new_value(self, choice_criteria, choice, new_value):
        if not check_user_input(choice_criteria, choice, new_value):
            return
        self.choice_criteria_dict[choice_criteria][choice] = new_value
        return


# take all ballots and calculate the winner
def calculate_star_method(ballot_list):
    # Ballot_list should be a list of all ballots with the same id

    return
