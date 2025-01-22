import requests
from bs4 import BeautifulSoup
import mysql.connector
import csv

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='testscarping'
    )

def insert_into_database(cursor, data):
    query = """
    INSERT INTO `scarpedata` (
        `Service ID`, `Service Name`, `Rate per Thousand`, `Minimum Quantity`,
        `Maximum Quantity`, `Average Time`, `provider`, `Category of the Service`, `Description`
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for row in data:
        cursor.execute(query, (
            row['Service ID'], row['Service Name'], row['Rate per Thousand'], row['Minimum Quantity'], row['Maximum Quantity'], 
            row['Average Time'], row['provider'], 
            row['Category of the Service'], row['Description']
        ))


def scrape_likesoutlet(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': 'table', 'id': 'service-table'})
        if not table:
            print(f"No table found in {url}.")
            return []

        rows = table.find_all('tr', {'data-filter-table-category-id': True})
        if not rows:
            print(f"No rows found in {url}.")
            return []

        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 7:
                continue
            
            data.append({
                'Service ID': columns[0].text.strip(),
                'Service Name': columns[1].text.strip(),
                'Rate per Thousand': columns[2].text.strip(),
                'Minimum Quantity': columns[3].text.strip(),
                'Maximum Quantity': columns[4].text.strip(),
                'Average Time': columns[5].text.strip(),
                'Category of the Service': columns[6].text.strip(),
                'Description': columns[7].text.strip() if len(columns) > 7 else 'N/A',
                'provider': 'likesoutlet.com'
            })
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

def scrape_godofpanel(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': 'table table-responsive', 'id': 'service-table'})
        if not table:
            print(f"No table found in {url}.")
            return []

        rows = table.find_all('tr', {'data-filter-table-category-id': True})
        if not rows:
            print(f"No rows found in {url}.")
            return []

        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 7:
                continue

            data.append({
                'Service ID': columns[0].text.strip(),
                'Service Name': columns[1].text.strip(),
                'Rate per Thousand': columns[2].text.strip(),
                'Minimum Quantity': columns[3].text.strip(),
                'Maximum Quantity': columns[4].text.strip(),
                'Average Time': columns[5].text.strip(),
                'Category of the Service': columns[6].text.strip(),
                'Description': columns[7].text.strip() if len(columns) > 7 else 'N/A',
                'provider': 'godofpanel.com'
            })
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

def scrape_followiz(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        service_container = soup.find('tbody', {'id': 'service_container_0', 'class': 'service_container'})

        if not service_container:
            print(f"No service container found in {url}")
            return []

        rows = service_container.find_all('tr', {'class': 'service-detail-row'})

        if not rows:
            print(f"No service rows found in container")
            return []

        data = []
        for row in rows:
            try:
                service_id = row.get('data-service_id', 'N/A')

                columns = row.find_all('td')
                if len(columns) < 7:
                    print(f"Skipping row {service_id} - insufficient columns")
                    continue

                data.append({
                    'Service ID': service_id,
                    'Service Name': columns[1].text.strip() if len(columns) > 1 else 'N/A',
                    'Rate per Thousand': columns[2].text.strip() if len(columns) > 2 else 'N/A',
                    'Minimum Quantity': columns[3].text.strip() if len(columns) > 3 else 'N/A',
                    'Maximum Quantity': columns[4].text.strip() if len(columns) > 4 else 'N/A',
                    'Average Time': columns[5].text.strip() if len(columns) > 5 else 'N/A',
                    'Category of the Service': columns[6].text.strip() if len(columns) > 6 else 'N/A',
                    'Description': columns[7].text.strip() if len(columns) > 7 else 'N/A',
                    'provider': 'followiz.com'
                })
                print(f"Successfully scraped service ID: {service_id}")

            except Exception as e:
                print(f"Error processing row {service_id}: {str(e)}")
                continue

        print(f"Total services scraped: {len(data)}")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error while scraping {url}: {e}")
        return []

def save_to_csv(data, filename):
    if not data:
        print(f"No data to save for {filename}.")
        return

    keys = ['Service ID', 'Service Name', 'Rate per Thousand', 'Minimum Quantity', 'Maximum Quantity', 'Average Time', 'Category of the Service', 'Description', 'provider']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}.")

def scrape_smmbind(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'class': 'table', 'id': 'service-table'})
        if not table:
            print(f"No table found in {url}.")
            return []

        rows = table.find_all('tr', {'data-filter-table-category-id': True})
        if not rows:
            print(f"No rows found in {url}.")
            return []

        data = []
        for row in rows:
            columns = row.find_all('td')
            if len(columns) < 7:
                continue

            data.append({
                'Service ID': columns[0].text.strip(),
                'Service Name': columns[1].text.strip(),
                'Rate per Thousand': columns[2].text.strip(),
                'Minimum Quantity': columns[3].text.strip(),
                'Maximum Quantity': columns[4].text.strip(),
                'Average Time': columns[5].text.strip(),
                'Category of the Service': columns[6].text.strip(),
                'Description': columns[7].text.strip() if len(columns) > 7 else 'N/A',
                'provider': 'smmbind.com'
            })
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

def main():
    connection = connect_to_database()
    cursor = connection.cursor()

    smmbind_url = 'https://smmbind.com/services'
    print(f"Scraping from {smmbind_url}...")
    smmbind_data = scrape_smmbind(smmbind_url)
    insert_into_database(cursor, smmbind_data)

    likesoutlet_url = 'https://likesoutlet.com/services'
    print(f"Scraping from {likesoutlet_url}...")
    likesoutlet_data = scrape_likesoutlet(likesoutlet_url)
    insert_into_database(cursor, likesoutlet_data)

    godofpanel_url = 'https://godofpanel.com/services'
    print(f"Scraping from {godofpanel_url}...")
    godofpanel_data = scrape_godofpanel(godofpanel_url)
    insert_into_database(cursor, godofpanel_data)

    followiz_url = 'https://followiz.com/services'
    print(f"Scraping from {followiz_url}...")
    followiz_data = scrape_followiz(followiz_url)
    insert_into_database(cursor, followiz_data)

    connection.commit()
    cursor.close()
    connection.close()

    combined_data = smmbind_data + likesoutlet_data + godofpanel_data + followiz_data
    save_to_csv(combined_data, 'services_combined.csv')

if __name__ == '__main__':
    main()
