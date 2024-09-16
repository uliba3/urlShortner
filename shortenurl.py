from enum import Enum
import sys
import storage
from urllib.parse import urlparse
import url_shortener

data = storage.get_data()


class ArgumentTypes(Enum):
    PRINT_HASHES = 1
    PRINT_SHORTEN_URLS = 2
    PRINT_ORIGINAL_URLS = 3
    PRINT_ALL = 4
    INVALID = 5
    GET_SHORT_URL_FROM_ORIGINAL = 6
    GET_ORIGINAL_URL_FROM_SHORT = 7
    GET_COUNT = 8

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
                return ArgumentTypes.GET_SHORT_URL_FROM_ORIGINAL
            case 'g':
                return ArgumentTypes.GET_ORIGINAL_URL_FROM_SHORT 
            case 'c':
               return ArgumentTypes.GET_COUNT 
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
            return [url_shortener.shorten_url(url)[0] for url in data.values()]
            
        case ArgumentTypes.PRINT_ORIGINAL_URLS:
            return data.values()
            
        case ArgumentTypes.PRINT_ALL:
            return data
        
        case ArgumentTypes.GET_SHORT_URL_FROM_ORIGINAL: 
            if len(arguments) < 2:
                return "Please provide a vaild original url."
                # quit()
            original_url: str = arguments[1]
            
            if not url_shortener.is_valid_url(original_url):
                return "Please provide a valid url."
            
            ## TODO
            # Add the hash and original url to the database and return the short version
            shortened_url, hash_of_the_url, _ = url_shortener.shorten_url(original_url)
            
            # storage.save_data(original_url, hash_of_the_url)
            
            return shortened_url
        
        case ArgumentTypes.GET_ORIGINAL_URL_FROM_SHORT:
            if len(arguments) < 2:
                return "Please provide a valid short url."
            
            shortened_url = arguments[1]
            
            o_url = url_shortener.expand_url(shortened_url)
            
            return url_shortener.shorten_url(o_url)[1]
            
        case ArgumentTypes.INVALID:
            return "Error! Please, enter a valid command"
        
        case ArgumentTypes.GET_COUNT:
            return len(data)
    
    ## This case should never happpen
    return None

if __name__ == "__main__":
    
    # Name of the python script we are running
    python_script = sys.argv[0]
    
    # Run the script
    print(run(sys.argv[1:]))
