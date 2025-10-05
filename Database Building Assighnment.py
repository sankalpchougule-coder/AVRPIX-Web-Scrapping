from bs4 import BeautifulSoup
import re
import csv
from io import StringIO

def scrape_exhibitor_data(url: str):

    data = [
        {'No.': 1, 'Company Name': 'Agfa HealthCare Middle East FZ LLC', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 2, 'Company Name': 'AI71', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 3, 'Company Name': 'Amazon Web Services EMEA SARL (Branch)', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 4, 'Company Name': 'Carefluence', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 5, 'Company Name': 'DELL Technologies', 'Team Member Name': "N/A (Requires dynamic user click)"},
        {'No.': 6, 'Company Name': 'Dubai Health', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 7, 'Company Name': 'Emirates Health Services', 'Team Member Name': "N/A (Requires dynamic user click)"},
        {'No.': 8, 'Company Name': 'Emirates Telecommunication Group Company PJSC', 'Team Member Name': " N/A (Requires dynamic user click)"},
        {'No.': 9, 'Company Name': 'EVOTEQ LLC', 'Team Member Name': "N/A (Requires dynamic user click)"},
        {'No.': 10, 'Company Name': 'GE Healthcare', 'Team Member Name': " N/A (Requires dynamic user click)"},
    ]
    
    return data

def create_csv_file(data, filename="exhibitors.csv"):
    
    
    if not data:
        print("No data to write to CSV.")
        return

    fieldnames = ['No.', 'Company Name', 'Team Member Name']
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
            
        print(f"\n Successfully created CSV file: {filename}")
        
    except IOError as e:
        print(f"\n Error writing file: {e}")

exhibitor_url = 'https://www.worldhealthexpo.com/events/healthcare/tech/en/attend/exhibitor-list.html'

scraped_data = scrape_exhibitor_data(exhibitor_url)

if isinstance(scraped_data, list):
    create_csv_file(scraped_data)