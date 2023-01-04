import requests
from bs4 import BeautifulSoup


def add_two_hours_to_time(time):
    hour = int(time[0]) + 2
    minutes = time[1]
    time_to_join = list()
    time_to_join.append(str(hour))
    time_to_join.append(str(minutes))
    time = ":".join(time_to_join)
    return time
# req = requests.get('https://www.prosoccer.gr/en/football/predictions/yesterday.html')

# req = requests.get('https://www.prosoccer.gr/en/football/predictions/')
# req = requests.get('https://www.prosoccer.gr/en/football/predictions/tomorrow.html')
# req = requests.get('https://www.prosoccer.gr/en/football/predictions/Friday.html')
req = requests.get('https://www.prosoccer.gr/en/football/predictions/Saturday.html')
# req = requests.get('https://www.prosoccer.gr/en/football/predictions/Sunday.html')
# req = requests.get('https://www.prosoccer.gr/en/football/predictions/Monday.html')

soup = BeautifulSoup(req.content, 'html.parser')

table = soup.find(id='tblPredictions')
rows = table.find_all('tr')[1:]
top_predictions = []
for row in rows:
    cols = row.find_all('td')
    league = cols[0].text
    # time = cols[1].text
    time = add_two_hours_to_time(cols[1].text.split(":"))
    match_game = cols[2].text
    prediction_for_1 = int(cols[3].text)
    prediction_for_x = int(cols[4].text)
    prediction_for_2 = int(cols[5].text)
    general_prediction = cols[6].text.strip('a')
    if cols[7].text and cols[8].text and cols[9].text:
        odds_1 = float(cols[7].text)
        odds_X = float(cols[8].text)
        odds_2 = float(cols[9].text)
        if odds_1 > 1.5 and odds_X > 1.5 and odds_2 > 1.5:
            if prediction_for_1 > 70 or prediction_for_x > 70 or prediction_for_2 > 70:
                prediction = {"league": {league},
                              "time": {time},
                              "match": {match_game},
                              "prediction_1": {prediction_for_1},
                              "prediction_X": {prediction_for_x},
                              "prediction_2": {prediction_for_2},
                              "PREDICTION": {general_prediction},
                              "odds_1": odds_1,
                              "odds_X": odds_1,
                              "odds_2": odds_1}

                top_predictions.append(prediction)
                print(
                    f'{league} | {time} | {match_game}: {prediction_for_1}|{prediction_for_x}|{prediction_for_2} || {general_prediction} || {odds_1} | {odds_X} | {odds_2}'
                )

for prediction in top_predictions:
    print(prediction)
