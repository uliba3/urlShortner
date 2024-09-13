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
    GET_ORIGINAL_URL = 7

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
            case 'g':
                return ArgumentTypes.GET_ORIGINAL_URL  
    return ArgumentTypes.INVALID
    


def run(arguments: list[str]):
    number_of_arguments = len(arguments)
    
    argument_flag: str = arguments[0]
    
    match type_of_argument(argument_flag):
        case ArgumentTypes.PRINT_HASHES:
            return data.keys()
            
        case ArgumentTypes.PRINT_SHORTEN_URLS:
            ## TODO
            # Print all the shortened urls.
            return "All the shortened urls."
            
        case ArgumentTypes.PRINT_ORIGINAL_URLS:
            return data.values()
            
        case ArgumentTypes.PRINT_ALL:
            return data
        
        case ArgumentTypes.ORIGINAL_URL: 
            if len(arguments) < 2:
                return ("Please provide a vaild original url.")
                # quit()
            original_url: str = arguments[1]
            
            ## TODO
            # Add the hash and original url to the database.
            
            return original_url
        
        case ArgumentTypes.GET_ORIGINAL_URL:
            shortened_url = arguments[1]
            
            # Use the correct get_hash_from_url
            def get_hash_from_url(url):
                url.split('https://soobin.com/')[1]
            
            hash_value = get_hash_from_url(shortened_url)
            
            return data[hash_value]
            
        case ArgumentTypes.INVALID:
            return "Error! Please, enter a valid command"
    
    
    ## This case should never happpen
    return None

if __name__ == "__main__":
    
    # Name of the python script we are running
    python_script = sys.argv[0]
    
    # Run the script
    print(run(sys.argv[1:]))
