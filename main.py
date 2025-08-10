import sys

from stats import get_book_text
from stats import char_report

def main():

    if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        else: 
            print("|:.  BOOKBOT  .:|\n")
            print("Analyzing book provided at " f"{sys.argv[1]}" "\n")
            print("|:.  Word Count\n")
            print("Found " f"{len(get_book_text())} total words\n")
            print("|:.  Character Count\n")
            print(char_report() + "\n")
            print("|:.  END  .:|")
   

            
main()