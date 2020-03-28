import requests
import json
from bs4 import BeautifulSoup
def parsePage():
    page = requests.get(
        "https://www.regionofwaterloo.ca/en/health-and-wellness/positive-cases-in-waterloo-region.aspx")
    soup = BeautifulSoup(page.content, 'html.parser')

    covid_table = soup.find("table", attrs={"class": "datatable"})
    # contains heading row, and data rows.
    covid_table_rows = covid_table.tbody.find_all("tr")

    # Get all the headings
    headings = []
    # in first row, get all column values
    for td in covid_table_rows[0].find_all("td"):
        # remove any newlines and extra spaces from left and right
        headings.append(td.p.text.replace('\n', '').strip())
    print(headings)
    covid_table_rows.pop(0)  # remove heading row
    # Get the cases:
    table_data = []
    for tr in covid_table_rows:
        t_row = {}
         # Each table row is stored in the form of
         #{
            #"Patient  (age and gender)": "Under 20s Male",
            #"Testing location": "Grand River Hospital",
            #"Status (self-isolating, hospitalized or resolved)": "Self-isolating at home",
            #"Transmission (community, travel or close contact)": "Close contact",
            #"Waterloo Region Case Number": "43*"
        #}

         # find all td's(5) in tr and zip it with t_header
        counter = 0
        for td, th in zip(tr.find_all("td"), headings):
            t_row[th] = td.text.replace('\n', '').strip()
            t_row["id"] = counter
            counter+=1
        table_data.append(t_row)
    return table_data
if __name__ == "__main__":
    print(json.dumps(parsePage(),indent=4))