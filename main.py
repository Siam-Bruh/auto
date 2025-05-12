import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init

init(autoreset=True)

# Show colorful ASCII Banner
def show_banner():
    banner = f'''
{Fore.CYAN}+=======================================+
{Fore.CYAN}|                                       |
{Fore.GREEN}|   ███████╗██╗ █████╗ ███╗   ███╗     |
{Fore.GREEN}|   ██╔════╝██║██╔══██╗████╗ ████║     |
{Fore.GREEN}|   █████╗  ██║███████║██╔████╔██║     |
{Fore.GREEN}|   ██╔══╝  ██║██╔══██║██║╚██╔╝██║     |
{Fore.GREEN}|   ██║     ██║██║  ██║██║ ╚═╝ ██║     |
{Fore.CYAN}|                                       |
{Fore.MAGENTA}|         Coded by: {Fore.YELLOW}SIAM              |
{Fore.CYAN}+=======================================+

{Fore.BLUE}+---------------------------------------+
{Fore.CYAN}| Owner: Md Siam                        |
{Fore.CYAN}| Facebook: fb.com/mdsiam.official      |
{Fore.CYAN}| Telegram: t.me/mdsiam_official        |
{Fore.BLUE}+---------------------------------------+{Style.RESET_ALL}
'''
    print(banner)

# Load accounts from accounts.txt
def load_accounts(file_path='accounts.txt'):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip().split('|') for line in lines if '|' in line]

# Prompt user for input
def get_user_input():
    print("""
===============================
   Facebook Auto React Tool
===============================
    """)
    accounts = load_accounts()
    print(f"Accounts Loaded: {len(accounts)}")

    print("Select React Type:")
    reactions = ['Like', 'Love', 'Haha', 'Wow', 'Sad', 'Angry']
    for i, react in enumerate(reactions, 1):
        print(f"{i}. {react}")

    choice = int(input("Enter choice [1-6]: "))
    react_type = reactions[choice - 1]

    post_url = input("Enter Facebook Post URL: ")

    return accounts, react_type, post_url

# Setup headless browser
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Perform login and react
def perform_react(email, password, post_url, react_type):
    driver = create_driver()
    driver.get("https://www.facebook.com/")
    time.sleep(3)

    try:
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        time.sleep(5)

        driver.get(post_url)
        time.sleep(5)

        react_xpath = "//div[@aria-label='React']"
        driver.find_element(By.XPATH, react_xpath).click()
        time.sleep(1)

        reaction_xpath = f"//div[@aria-label='{react_type}']"
        driver.find_element(By.XPATH, reaction_xpath).click()
        print(f"[{email}] Reacted with {react_type}")

    except Exception as e:
        print(f"[{email}] Failed: {e}")
    finally:
        driver.quit()

# Main
if __name__ == '__main__':
    show_banner()
    accounts, react_type, post_url = get_user_input()

    for email, password in accounts:
        perform_react(email, password, post_url, react_type)
        delay = random.randint(3, 7)
        print(f"Waiting {delay} seconds...")
        time.sleep(delay)

    print("\nAll done!")
