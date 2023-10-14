from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Board
from .forms import Boardform
from .models import Stat
from .forms import Statform
from .forms import Updateform
from django.contrib.auth.hashers import check_password

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def home(request):
    all_boards = Board.objects.all
    return render(request, 'home.html', {'all':all_boards})

def create(request):
    if request.method == "POST":
        form = Boardform(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        return render(request, 'create.html')
    

# def update(request):
#     if request.method == "POST":
#         form = Updateform(request.POST or None)
#         if form.is_valid():
#             entered_id = form.cleaned_data['parent_id']
#             entered_password = form.cleaned_data['passw']
#             entered_link = form.cleaned_data['link']
#             board_instance = Board.objects.filter(id=entered_id).first()

#             try:
#                 board_instance = get_object_or_404(Board, pk=entered_id)
#                 if check_password(entered_password, board_instance.password):
#                     # Do something if the id and password match
#                     # For example, set a session variable, redirect to another page, etc.

#                     options = DesiredCapabilities().CHROME
#                     options["pageLoadStrategy"] = "normal"
#                     options = webdriver.ChromeOptions()
#                     driver = webdriver.Chrome(options=options)

#                     driver.get(entered_link)
#                     print(driver.title)

#                     search = driver.find_element(By.PARTIAL_LINK_TEXT, "PLAYER STATS")
#                     search.click()

#                     time.sleep(5)

#                     stats = driver.find_element(By.ID, "player_ranking")
#                     driver.quit()

#                     f = stats.text.splitlines()

#                     for line in f:
#                         if line.strip():
#                             ign = line.strip()
#                             if not Stat.objects.filter(ign=ign).exists():
#                                 stats_line = next(f).strip().split(" ")
#                                 matches, kills, damage, knocks, assists, longest, travel, revives, accuracy = map(
#                                     lambda x: int(x) if x.isdigit() else float(x.replace('m', '')), stats_line)

#                                 Stat.objects.create(
#                                     parent_id=entered_id,
#                                     ign=ign,
#                                     matches=matches,
#                                     kills=kills,
#                                     damage=damage,
#                                     knocks=knocks,
#                                     assists=assists,
#                                     longest=longest,
#                                     travel=travel,
#                                     revives=revives,
#                                     accuracy=accuracy
#                                 )

#                     return redirect('/update')
#                 else:
#                     # Password does not match
#                     # Handle the case where the password is incorrect
#                     pass
#             except:
#                 # Entered id does not exist
#                 # Handle the case where the id is not found
#                 pass

#     return render(request, 'update.html')


def updated(request):
    entered_link = 'https://esports.pubgrank.org/tournament/sunday-08-october-2023'
    entered_id = '1'

    options = ChromeOptions()
    options.add_argument("--pageLoadStrategy=normal")  # Add this line instead of options["pageLoadStrategy"] = "normal"
    driver = webdriver.Chrome(options=options)

    driver.get(entered_link)
    print(driver.title)

    search = driver.find_element(By.PARTIAL_LINK_TEXT, "PLAYER STATS")
    search.click()

    time.sleep(5)

    stats = driver.find_element(By.ID, "player_ranking")
    driver.quit()

    f = stats.text.splitlines()

    for i in range(1, len(f), 2):
        ign = f[i].strip()

        if not Stat.objects.filter(ign=ign).exists():
            stats_line = f[i + 1].strip().split(" ")

            matches, kills, damage, knocks, assists, longest, travel, revives, accuracy = map(
                lambda x: int(x) if x.isdigit() else float(x.replace('m', '')), stats_line)

            Stat.objects.create(parent_id=entered_id,
                                ign=ign,
                                matches=matches,
                                kills=kills,
                                damage=damage,
                                knocks=knocks,
                                assists=assists,
                                longest=longest,
                                travel=travel,
                                revives=revives,
                                accuracy=accuracy)

    return render(request, 'updated.html')