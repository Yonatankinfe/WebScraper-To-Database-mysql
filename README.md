# WebScraper-To-Database-mysql
WebScraperDatabase is a Python-based web scraping project that collects data from multiple service provider websites, stores the data in a MySQL database, and provides a structured REST API to retrieve the data. The repository also includes a lightweight HTML front-end for viewing the scraped data.
## Features
- **Multi-website scraping:** Supports multiple service providers like LikesOutlet, GodOfPanel, Followiz, and SMMBind.
- **MySQL Integration:** Stores scraped data in a structured MySQL database for analysis and usage.
- **CSV Export:** Combines and exports scraped data to CSV format.
- **REST API:** Provides a REST API for fetching the data.
- **Web Viewer:** A simple HTML page for displaying scraped data.
- ## Prerequisites
- **Python 3.7 or higher**
- **MySQL Server**
- **requests==2.28.2**
- **beautifulsoup4==4.12.0**
- **mysql-connector-python==8.0.33**
## Setup

### 1. Clone the repository

git clone https://github.com/yourusername/WebScraper-To-Database-mysql.git
cd WebScraperDatabase
### 2. Install Dependencies
Install the required Python packages using the command below:
+ pip install -r requirements.txt
### 3. Configure MySQL Database
+ Create a database named testscarping.
+ Update the connect_to_database function in the Python script with your MySQL credentials.
+ Usage
### Fetch Data
Send a GET request to the  with the following parameters:
+ page: Page number (default: 0)
+ limit: Number of records per page (default: 2000)
# Some Images 
![Image](https://github.com/user-attachments/assets/c8f3af20-94e9-4c04-b8dd-6f96500de2fc)

![Image](https://github.com/user-attachments/assets/75918694-c55e-4bf0-b4b1-fb794f723488)

