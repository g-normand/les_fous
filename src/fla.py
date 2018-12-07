import requests

def get_classement(championnat_id, saison_id=6):
    payload = {}
    payload['championnatId'] = championnat_id
    payload['saisonId'] = saison_id
    result = requests.post('http://www.football-loisir-amateur.com/Home/GetClassement/', data=payload)

    infos = []
    for team in result.json():
        infos.append(team)
    return dict(teams=sorted(infos, key=lambda team:team['Points'], reverse=True))

