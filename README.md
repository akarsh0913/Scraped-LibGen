# Scraped-LibGen
A low-key web scraper for LibGen

This Python code performs web scraping to search for book links on the Library Genesis website (libgen.li) based on user-provided book names. Here's a breakdown of the code:

1. Import necessary libraries:
   - requests: Used for sending HTTP requests to web servers and receiving responses.
   - BeautifulSoup from the bs4 library: Used for parsing HTML and XML documents and extracting information.

2. User Input:
   - The user is prompted to enter a book name.
   - The input is split into individual words (tags) using the split() function.
   - The tags are then formatted by joining them with '+' characters using the join() function.
   - This formatting is used for constructing the search query URL.
     
3. Constructing the Query URL:
   - The base URL is set to `https://libgen.is/index.php?req=`
   - The formatted tags are added to the base URL to create the complete query URL.
     
4. Sending a Request and Parsing the Page:
   - The requests.get() function is used to send an HTTP GET request to the constructed query URL.
   - The response content is parsed using BeautifulSoup with the 'html.parser' to create a BeautifulSoup object called soup.
   
5. Extracting Book Links:
   - The soup.select() function is used to select specific elements from the parsed HTML content.
   - In this case, it looks for all `<a>` tags within `<td>` elements within `<tr>` elements.
   - The selected anchor tags are stored in the links list.
     
6. Filtering and Displaying Links:
   - The code selects the first 1000 links from the links list (or fewer if there are fewer than 1000 links).
   - For each anchor tag in the first 1000 links, it retrieves the 'href' attribute (the URL) using the .get('href') method.
   - It checks if the retrieved URL contains the string `library.lol`.
   - If the condition is met, it prints the URL and a line of hyphens to visually separate the links.
     
The code is essentially searching for book links related to the user's input on the Library Genesis website and printing the links that match the `library.lol` domain.
