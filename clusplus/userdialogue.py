'''Functions used to communicate with the user in terminal '''
from . import database 
from typing import Tuple, Literal, Dict, List, Any, Optional, Iterable
import time

Point = Tuple[int | float, int | float]
Labels = List[int]
def choose_dataset(dbase : Optional[Dict[Any, Any]] = None, options : List[str] | Literal['All'] = 'All') -> Tuple[str, Tuple[List[Point], Labels]]:
    '''
    Allows user to select a dataset in terminal.
    Keeps asking until gets valid input
    '''

    if dbase is None:
        dbase = database.database
    #Possible sets to select from
    if options == 'All':
        options = list(dbase.keys())

    #Choosing process            
    while True:
        choose = get_yes_or_no('Do you want to choose a set of points?')
        time.sleep(0.4)
        if choose == 'yes':
            print('Here are your options: ')
            time.sleep(0.2)
            for option in options:
                print(option)

            while True:
                sset_name = input('Enter the set name: ')
                time.sleep(0.2) 
                try:
                    sset = dbase[sset_name]
                except KeyError:
                    print('There is no such set. Check spelling.')
                else: 
                    print('Successfully selected a set.')
                    return sset_name, sset

        elif choose == 'no':
            print('Ok, proceeding with a random set')
            time.sleep(0.09)
            sset_name , sset = database.load_random_dataset(dbase = dbase, options = options)
            print('This time it is', sset_name)
            return sset_name, sset


def get_integer_hyperparameter(parameter_name : str , min_value : int = 2, max_value : int = 20) -> int:
    '''
    Allows user to select an integer in terminal.
    If input is not interger or isn't in range [min_value, min_value]
    asks user to try again
    '''
    while True:
        value = input(f"Enter a value of {parameter_name}: ")
        time.sleep(0.4)
        try:
            value = int(value)
            if not min_value <= value <= max_value:
                print(f'{parameter_name} should be between {min_value} and {max_value}')
                continue
            return value
        except (TypeError, ValueError):
            print(f'{parameter_name} should be integer')


def get_discrete_parameter(parameter_name : str, possible_values : Iterable[str]) -> str:
    '''
    Allows user to select an string hyperparameter in terminal.
    If input is not one of possible values
    asks user to try again
    '''
    print(f'Select {parameter_name} from given options: {possible_values}')
    while True:
        time.sleep(0.3)
        value = input(f"Enter {parameter_name}: ")
        value = value.strip().lower()
        if not value in possible_values:
            print(f'{parameter_name} should be one of the following: {possible_values}')
            continue
        return value
    

def get_yes_or_no(message: str) -> Literal['yes', 'no']:
    print(message)
    print("You can leave the data field empty instead of 'no'.")
    while True:
        choice = input("Enter 'yes' or 'no': ").strip().lower()
        if choice in ('yes', 'no'):
            return choice
        if not choice:
            return 'no'


def main():
    a = choose_dataset()

