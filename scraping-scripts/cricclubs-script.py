import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the main fixtures page
base_url = "https://cricclubs.com/DMBIndoorCup2023/fixtures.do?league=15&year=2023&clubId=39889"

# Fetch the main page
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all match links (Assuming each match has a unique link)
match_links = []
for anchor in soup.find_all('a', href=True):
    if 'scorecard' in anchor['href']:  # Adjust keyword as per the link structure
        match_links.append(f"https://cricclubs.com{anchor['href']}")

# Placeholder for ball-by-ball data
all_ball_data = []

# Loop through each match link
for match_url in match_links:
    print(f"Scraping: {match_url}")
    match_response = requests.get(match_url)
    match_soup = BeautifulSoup(match_response.text, 'html.parser')

    # Find the ball-by-ball table (Inspect to find the table structure)
    table = match_soup.find('table', {'class': 'ball-by-ball-table'})  # Adjust the class or identifier
    if not table:
        continue

    # Extract rows
    for row in table.find_all('tr')[1:]:  # Skip header row
        cols = [col.text.strip() for col in row.find_all('td')]
        all_ball_data.append(cols)

# Convert to DataFrame and save to CSV
columns = ['Over', 'Ball', 'Batsman', 'Bowler', 'Runs', 'Extras', 'Commentary']  # Adjust columns as needed
df = pd.DataFrame(all_ball_data, columns=columns)
df.to_csv('../data/cricclubs_data/deliveries.csv', index=False)

print("Data saved to ball_by_ball.csv")
