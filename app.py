from url_shortener import shorten_url, expand_url, count_urls

def main():
    while True:
        print("\n1. Shorten URL")
        print("2. Expand URL")
        print("3. Count URLs")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_url, error = shorten_url(long_url)
            if error:
                print(f"Error: {error}")
            else:
                print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the shortened URL: ")
            original_url, error = expand_url(short_url)
            if error:
                print(f"Error: {error}")
            else:
                print(f"Original URL: {original_url}")
        elif choice == '3':
            print(f"Number of shortened URLs: {count_urls()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



