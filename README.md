# urlShortner

### Project Description

#### CS 230

#### Fall 24

#### Dr. Musgrave

#### In-Class Project

In a group of 2-3 people, build an application to store URL’s of any length and return a
shortened version of the URL in Python. Entering the shortened URL will return the full
URL. Your project should protect against invalid URL’s. The format of the shortened
URL should have a unique id that is less than 12 ASCII characters. You should decide
on a way to store the data, and this can be in a file with a specified format (CSV, JSON).
You should be able to count the number of URL’s that have been shortened so far. You
can accept user input as text given a prompt. If you feel comfortable with more
advanced methods, you can do that as well.

A valid URL looks like: “https://www.google.com/home?userId=12345&profile=abcdef”
A shortened URL could look something like: “https://myApp.com/short123”
Consider what happens as the application grows in size. What data structures and
algorithms will need to be used? There may be other application performance issues to
consider. Is there a limit to the number of URL’s that can be stored?
Decide on the number of application features that you can complete within the
timeframe.

After you have finished development, prepare a demo of your application to the class.


### Documentation

The script can be run as a command line tool. Add flags and arguments to control the behavior.

Eg.
python3 shortenurl.py -u "https://youtube.com/thebestyoutubevideointheworld"

Running the script with '-u' and an original url will save the original url and print the shortened version.

1. '-h'

Prints all the hashes.

2. '-s' 

Prints all the shortened urls.

3. '-o' 

Prints all the original urls.

4. '-a'

Prints all the hashes and original urls as python dictionary.

5. '-u' <long-url>

Prints the shoretened version of the url and saves the original url that was provided.

6. '-g' <short-url>

Prints the original url corresponding to the shortened url that was provided. Prints nothing if short-url was previously not saved.

7. '-c'

Prints the number of urls stored.

