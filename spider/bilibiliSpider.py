from selenium import webdriver
import pandas as pd
import time
import re

# Specify Edge WebDriver path and options
edge_path = r'C:\Users\贺昱文\Downloads\edgedriver_win64\msedgedriver.exe'  # Adjust to your Edge WebDriver path
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Use Chromium-based Edge (if applicable)
edge_options.add_argument('--headless')  # Optional: Use headless mode
edge_options.add_argument('--disable-gpu')  # Optional: Disable GPU acceleration
edge_options.add_argument('blink-settings=imagesEnabled=false')  # Optional: Disable image loading
edge_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Create Edge browser object
driver = webdriver.Edge(edge_path, options=edge_options)

def fetch_page(url: str) -> str:
    # Open the webpage
    driver.get(url)

    # Wait for 3 seconds to ensure the page loads completely (adjust as needed)
    time.sleep(5)

    # Get the HTML source of the page
    html = driver.page_source

    return html

if __name__ == '__main__':
    # df = pd.DataFrame(columns=['url'])
    df = pd.read_csv('../data/每周必看.csv')
    for i in range(1,274):
        url = f'https://www.bilibili.com/v/popular/weekly/?num={i}'
        data=fetch_page(url)
        if data is not None:
            pattern = r'<a data-v-f372a95c="" href="(//[\w\./]+)" target="_blank">'
            match = re.findall(pattern, data)
            new_data = pd.DataFrame(match, columns=['url'])
            df = df.append(new_data, ignore_index=True)
            print(len(df))

    # Close the browser
    driver.close()

    df.to_csv('../data/每周必看.csv',index=False)