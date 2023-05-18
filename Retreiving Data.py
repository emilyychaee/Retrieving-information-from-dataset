from typing import IO, Tuple, List, Dict, Any

ARTIST_INFO = "1"
LIST_OF_ARTISTS_BY_GENRE = "2"
LIST_OF_ARTISTS_BY_NATIONALITY = "3"
LIST_OF_ARTISTS_BY_YEAR = "4"
ARTIST_BIO = "5"
ARTIST_REFERENCES = "6"
TOTAL_NUM_PAINTINGS = "7"

LINE = "\n--------------------------------------------------------------\n"


class Artist:
    def __init__(self, artist_id: int,
                 name: str,
                 years: str,
                 genre: str,
                 nationality: str,
                 biography: str,
                 reference: str,
                 total_paintings: int):
        self.artist_id = artist_id
        self.name = name
        self.years = years
        self.genre = genre
        self.nationality = nationality
        self.biography = biography
        self.reference = reference
        self.total_paintings = total_paintings


def artist_info(artist: Dict[str, Any]) -> str:
    """
    This function takes in a dictionary containing information about an artist and returns a string with details on the artist. The dictionary must have the following keys:

    'Name': a string containing the name of the artist
    'Years': a string indicating the years the artist was active
    'Genre': a string specifying the artist's genre
    'Nationality': a string indicating the artist's nationality
    'Biography': a string containing a brief biography of the artist
    'Reference': a string with a reference link to the artist's Wikipedia page
    'Total Paintings': an integer indicating the total number of paintings by the artist
    The function returns a string with the above information formatted for display.
    """
    general_info = f"Details on {artist['Name']}:\n" \
              f"Years: {artist['Years']}\n" \
              f"Genre: {artist['Genre']}\n" \
              f"Nationality: {artist['Nationality']}\n" \
              f"Bio: {artist['Biography']}\n" \
              f"Wikipedia Link: {artist['Reference']}\n" \
              f"Number of Paintings: {artist['Total Paintings']}\n"

    return general_info


def open_file(file_name: str) -> IO:
    """Return the file and open the file from the user input and read the file.
           Return an error message when the file cannot be read."""
    file_pointer = None
    while file_pointer is None:
        try:
            file_pointer = open(file_name, "r")
            return file_pointer
        except IOError:
            print("Error opening file")

    return file_pointer


def create_artist_list(artists_file: IO) -> List[Dict[str, Any]]:
    """Return the list of dictionary after reading the csv file and putting it into a list of dictionary.  """
    list_of_artists = []
    artists_file.readline()
    line = artists_file.readline().strip()
    artist_lst = line.split(',')

    while line is not None:
        if len(artist_lst) == 8:
            artists = Artist(int(artist_lst[0].strip()),
                             artist_lst[1].strip(),
                             artist_lst[2].strip(),
                             artist_lst[3].strip(),
                             artist_lst[4].strip(),
                             artist_lst[5].strip(),
                             artist_lst[6].strip(),
                             int(artist_lst[7].strip()))
            artist_dictionary = {
                "ID": artists.artist_id,
                "Name": artists.name,
                "Years": artists.years,
                "Genre": artists.genre,
                "Nationality": artists.nationality,
                "Biography": artists.biography,
                "Reference": artists.reference,
                "Total Paintings": artists.total_paintings
            }

            list_of_artists.append(artist_dictionary)
        line = artists_file.readline().strip()
        artist_lst = line.split(',')
    artists_file.close()
    return list_of_artists


def artists_genre_list(artists_file: IO) -> List[str]:
    """return the list of artists in a genre"""
    genre = create_artist_list(artists_file)
    genre_input = input("Enter a genre: ")
    artists_by_genre = []
    genre_exists = False

    for artist in genre:
        if artist["Genre"].upper() == genre_input.upper():
            artists_by_genre.append(artist["Name"])
            genre_exists = True
        if not genre_exists:
            print("There are no artists under that genre. Please try again.")

    return artists_by_genre


def artists_nationality_list(artists_file: IO) -> Tuple[Any]:
    nationalities = create_artist_list(artists_file)
    nationality_input = input("Enter a nationality: ")
    artists_by_nationality = []
    for artist in nationalities:
        if artist["Nationality"] == nationality_input:
            artists_by_nationality.append(artist["Name"])

    return tuple(artists_by_nationality)


def artists_by_year(artists_file: IO) -> List[str]:
    years = create_artist_list(artists_file)
    try:
        year_input = int(input("Enter year: "))
    except ValueError:
        print("Please enter a valid year.")
        return []
    artists_in_era = []
    for year in years:
        if '-' in year["Years"]:
            birth_year, death_year = year["Years"].split('-')
            if int(birth_year) <= year_input <= int(death_year):
                artists_in_era.append(year["Name"])
        elif int(year["Years"]) == year_input:
            artists_in_era.append(year["Name"])
    artists_file.close()
    return artists_in_era


def artists_bio(artists_file: IO) -> None:
    artists = create_artist_list(artists_file)
    name = input("Enter artist name: ")
    for art_name in artists:
        if art_name["Name"].upper() == name.upper():
            print(art_name["Biography"])
    artists_file.close()


def artists_references(artists_file: IO) -> None:
    artists = create_artist_list(artists_file)
    name = input("Enter artist name: ")
    for art_name in artists:
        if art_name["Name"].upper() == name.upper():
            print(art_name["Reference"])
    artists_file.close()


def totals_paintings(artists_file: IO) -> None:
    artists = create_artist_list(artists_file)
    name = input("Enter artist name: ")
    for art_name in artists:
        if art_name["Name"].upper() == name.upper():
            print(art_name["Total Paintings"])
    artists_file.close()


def display_menu():
    """Return the menu selection to the user for which function they want to execute """
    print("\nPlease select one of the following options.\n")
    print(ARTIST_INFO + ". Show an artist's general information.\n" +
          LIST_OF_ARTISTS_BY_GENRE + ". Show a list of artists by genre.\n" +
          LIST_OF_ARTISTS_BY_NATIONALITY + ". Show a list of artists by nationality.\n" +
          LIST_OF_ARTISTS_BY_YEAR + ". Show a list of artists by year.\n" +
          ARTIST_BIO + ". Show the artist's biography.\n" +
          ARTIST_REFERENCES + ". Show an external link for more information about the artist.\n" +
          TOTAL_NUM_PAINTINGS + ". Show the total number of the artist's paintings.\n"
          )

    return input("Press any other key to exit.\n")


# add parameters to the function later
def main() -> None:
    selection = display_menu()
    print(LINE)
    artists_file = open_file("artists.csv")

    if selection == ARTIST_INFO:
        user_int = input("Enter the artist's full name: ")
        artists = create_artist_list(artists_file)
        for artist in artists:
            if artist["Name"].upper() == user_int.upper():
                print(artist_info(artist))

    elif selection == LIST_OF_ARTISTS_BY_GENRE:
        artists_genre = artists_genre_list(artists_file)
        if artists_genre:
            print("Artists by Genre:")
            for artists in artists_genre:
                print(artists)

    elif selection == LIST_OF_ARTISTS_BY_NATIONALITY:
        artists_nationality = artists_nationality_list(artists_file)
        if artists_nationality:
            print("Artists by Nationality:")
            for artist in artists_nationality:
                print(artist)

    elif selection == LIST_OF_ARTISTS_BY_YEAR:
        artists_era = artists_by_year(artists_file)
        if artists_era:
            print("Artists by Year:")
            for artist in artists_era:
                print(artist)

    elif selection == ARTIST_BIO:
        artists_bio(artists_file)

    elif selection == ARTIST_REFERENCES:
        artists_references(artists_file)

    elif selection == TOTAL_NUM_PAINTINGS:
        totals_paintings(artists_file)

    else:
        return "Exit"

    print(LINE)
    artists_file.close()
    return "Continue"


if __name__ == '__main__':
    main()

