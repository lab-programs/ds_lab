"""
Left and Right part of the URL we need to scrape from 
pmindia.gov.in from the number and the suffix.
"""
MKB_LEFT_URL = "https://www.pmindia.gov.in/en/news_updates/pms-address-in-the-"
MKB_RIGHT_URL = "-episode-of-mann-ki-baat/"

"""
Gets the suffix from the number
For eg.
1st : get_suffix(1) => st
2nd : get_suffix(2) => nd
10th : get_suffix(10) => th
"""
def get_suffix( number ):
    if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
        return "th"
    if number % 10 == 1:
        return "st"
    if number % 10 == 2:
        return "nd"
    if number % 10 == 3:
        return "rd"
    return "th"

"""
Generates the final scrapable url
"""
def generate_mkb_url( number ):
    return MKB_LEFT_URL + str(number) + get_suffix(number) + MKB_RIGHT_URL

