import requests
def foot11():
    payload = {}
    payload['championnatId'] = 1144
    payload['saisonId'] = 5
    result = requests.post('http://www.football-loisir-amateur.com/Home/GetClassement/', data=payload)
    
    infos = []
    for team in result.json():
        infos.append(team)
    return sorted(infos, key=lambda team:team['Points'], reverse=True)

print(foot11())
