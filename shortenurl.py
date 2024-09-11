from enum import Enum
import sys
import storage


data = storage.get_data()


class ArgumentTypes(Enum):
    PRINT_HASHES = 1
    PRINT_SHORTEN_URLS = 2
    PRINT_ORIGINAL_URLS = 3
    PRINT_ALL = 4
    INVALID = 5
    ORIGINAL_URL = 6

def type_of_argument(argument: str) -> ArgumentTypes:
    if argument[0] == '-':
        match argument[1]:
            case 'h':
                return ArgumentTypes.PRINT_HASHES
            case 's':
                return ArgumentTypes.PRINT_SHORTEN_URLS
            case 'o':
                return ArgumentTypes.PRINT_ORIGINAL_URLS
            case 'a':
                return ArgumentTypes.PRINT_ALL
            case 'u':
                return ArgumentTypes.ORIGINAL_URL
    return ArgumentTypes.INVALID
    

number_of_arguments = len(sys.argv)

python_script = sys.argv[0]

argument_flag: str = sys.argv[1]

match type_of_argument(argument_flag):
    case ArgumentTypes.PRINT_HASHES:
        print(data.keys())
        
    case ArgumentTypes.PRINT_SHORTEN_URLS:
        ## TODO
        # Print all the shortened urls.
        print("All the shortened urls.")
        
    case ArgumentTypes.PRINT_ORIGINAL_URLS:
        print(data.values())
        
    case ArgumentTypes.PRINT_ALL:
        print(data)
    
    case ArgumentTypes.ORIGINAL_URL: 
        if number_of_arguments < 3:
            print("Please provide a vaild original url.")
            quit()
        original_url: str = sys.argv[2]
        
        ## TODO
        # Add the hash and original url to the database.
        
        print(original_url)
        
    case ArgumentTypes.INVALID:
        print("Error! Please, enter a valid command")
