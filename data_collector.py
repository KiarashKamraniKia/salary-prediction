from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

import csv
import time
import re

BASE_URL = "https://divar.ir/s/tehran/buy-residential/sadeghiyeh"
MAX_RECORDS = 320


def fa_to_en_digits(text: str) -> str:
    if not text:
        return text

    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    en_digits = "0123456789"
    trans_table = str.maketrans(fa_digits, en_digits)
    return text.translate(trans_table)


def extract_int_from_text(text: str):
    if not text:
        return None

    text = fa_to_en_digits(text)
    text = text.replace("،", "")
    numbers = re.findall(r"\d+", text)

    if numbers:
        return int(numbers[0])

    return None


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

def scroll_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


def collect_ad_links(driver, max_links):
    visited_links = set()

    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/v/']"))
    )

    scroll_attempts = 0

    while len(visited_links) < max_links and scroll_attempts < 100:

        elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='/v/']")

        for el in elements:
            try:
                href = el.get_attribute("href")
                if href:
                    visited_links.add(href)
            except StaleElementReferenceException:
                continue

        if len(visited_links) >= max_links:
            break

        previous_count = len(visited_links)
        scroll_page(driver)

        if len(visited_links) == previous_count:
            scroll_attempts += 1
        else:
            scroll_attempts = 0

    print(f"Collected {len(visited_links)} links.")
    return list(visited_links)[:max_links]


def scrape_ad_page(driver, link):
    data = {
        "Area": None,
        "Year Of Construction": None,
        "Room": None,
        "Floor Number": None,
        "Parking": False,
        "Warehouse": False,
        "Elevator": False,
        "Price": None
    }

    driver.get(link)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            price_el = driver.find_element(By.XPATH, "//*[contains(text(),'تومان')]")
            data["Price"] = extract_int_from_text(price_el.text)
        except:
            pass

        values = driver.find_elements(
            By.CSS_SELECTOR,
            "td.kt-group-row-item__value.kt-group-row-item--info-row"
        )

        numbers = [v.text.strip() for v in values if v.text.strip()]

        if len(numbers) >= 1:
            data["Area"] = extract_int_from_text(numbers[0])

        if len(numbers) >= 2:
            data["Year Of Construction"] = extract_int_from_text(numbers[1])

        if len(numbers) >= 3:
            room_value = numbers[2]
            if "بدون" in room_value:
                data["Room"] = 0
            else:
                data["Room"] = extract_int_from_text(room_value)


        floor_elements = driver.find_elements(
            By.CSS_SELECTOR,
            "div.kt-unexpandable-row__value-box > p.kt-unexpandable-row__value"
        )

        if floor_elements:
            floor_text = floor_elements[-1].text.strip()
            if 'از' in floor_text:
                data["Floor Number"] = extract_int_from_text(floor_text.split('از')[0])
            else:
                data["Floor Number"] = extract_int_from_text(floor_text)


        page_text = driver.page_source

        if "پارکینگ" in page_text and "پارکینگ ندارد" not in page_text:
            data["Parking"] = True

        if "انباری" in page_text and "انباری ندارد" not in page_text:
            data["Warehouse"] = True

        if "آسانسور" in page_text and "آسانسور ندارد" not in page_text:
            data["Elevator"] = True

    except Exception as e:
        print("Error scraping:", link, e)
        return None

    return data


def main():
    driver = create_driver()
    all_data = []

    try:
        links = collect_ad_links(driver, MAX_RECORDS)

        for index, link in enumerate(links, 1):
            print(f"[{index}/{len(links)}] Processing:", link)

            # retry mechanism
            for attempt in range(3):
                ad_data = scrape_ad_page(driver, link)
                if ad_data:
                    all_data.append(ad_data)
                    break
                else:
                    time.sleep(1)

        print("Finished collecting data.")

    finally:
        driver.quit()

        with open("my_output_chitgar.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "Area",
                    "Year Of Construction",
                    "Room",
                    "Floor Number",
                    "Parking",
                    "Warehouse",
                    "Elevator",
                    "Price"
                ]
            )
            writer.writeheader()
            writer.writerows(all_data)

        print("Data saved to my_output_chitgar.csv")


if __name__ == "__main__":
    main()