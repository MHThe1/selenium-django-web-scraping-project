import time
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import numpy as np

np.set_printoptions(threshold=np.inf, precision=2)

f = open('links.txt', 'r')

text = f.read()

# Define a regex pattern to match URLs
url_pattern = re.compile(r'https?://\S+')

# Find all matches in the text
websites = re.findall(url_pattern, text)
print(websites)
player_stats = np.empty((0, 10))
for website in websites:
    try:
        options = DesiredCapabilities().CHROME
        options["pageLoadStrategy"] = "normal"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

        driver.get(website)
        print(driver.title)

        search = driver.find_element(By.PARTIAL_LINK_TEXT, "PLAYER STATS")
        search.click()

        time.sleep(5)

        stats = driver.find_element(By.ID, "player_ranking")
        fo = open("scrimstats.txt", "w")
        fo.writelines(f"{stats.text}\n")
        fo.writelines(f"end")
        fo.close()
        driver.quit()

        fr = open("scrimstats.txt", "r")
        i = "1"
        current_line = fr.readline().strip()
        while i!=current_line:
            current_line = fr.readline().strip()
            if i==current_line:
                i = str(int(i)+1)
                ign = fr.readline().strip()
                if ign not in player_stats:
                    stats_line = fr.readline().strip().split(" ")
                    matches = int(stats_line[0])
                    kills = int(stats_line[1])
                    damage = float(stats_line[2])
                    knock = int(stats_line[3])
                    assist = int(stats_line[4])
                    longest = int(stats_line[5].replace('m', ''))
                    travel = float(stats_line[6])
                    revive = int(stats_line[8])
                    accuracy = float(stats_line[9])

                    new_row = np.array([ign, matches, kills, damage, knock, assist, longest, travel, revive, accuracy])
                    player_stats = np.vstack((player_stats, [new_row]))
                
                else:
                    index = np.where(player_stats[:, 0] == ign)[0]
                    stats_line = fr.readline().strip().split(" ")
                    player_stats[index[0], 1] = int(player_stats[index[0], 1]) + int(stats_line[0])
                    player_stats[index[0], 2] = int(player_stats[index[0], 2]) + int(stats_line[1])
                    player_stats[index[0], 3] = float(player_stats[index[0], 3]) + float(stats_line[2])
                    player_stats[index[0], 4] = int(player_stats[index[0], 4]) + int(stats_line[3])
                    player_stats[index[0], 5] = int(player_stats[index[0], 5]) + int(stats_line[4])
                    player_stats[index[0], 6] = int(player_stats[index[0], 6]) + int(stats_line[5].replace('m', ''))
                    player_stats[index[0], 7] = float(player_stats[index[0], 7]) + float(stats_line[6])
                    player_stats[index[0], 8] = int(player_stats[index[0], 8]) + int(stats_line[8])
                    player_stats[index[0], 9] = (float(float(player_stats[index[0], 9])*(int(player_stats[index[0], 1]) - int(stats_line[0])))+(float(stats_line[9])*int(stats_line[0])))/float(player_stats[index[0], 1])

            if current_line=="end":
                break
        fr.close()

    except Exception as e:
        print(f"This url didn't work: {website}")
        continue
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        continue

np.set_printoptions()
print(player_stats)

fdata = open("finalstats.txt", "w")
sorted_indices = np.argsort(player_stats[:, 2].astype(float))[::-1]

sorted_array = player_stats[sorted_indices]

fdata.writelines(f"{sorted_array}")

fdata.close()
