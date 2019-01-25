#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
import requests
import datetime
from decimal import Decimal

def get_classement(championnat_id, saison_id=6):
    payload = {}
    payload['championnatId'] = championnat_id
    payload['saisonId'] = saison_id
    result = requests.post('http://www.football-loisir-amateur.com/Home/GetClassement/', data=payload)

    infos = []
    for team in result.json():
        team['Nb_Matchs'] = team['Victoire'] + team['Defaite'] + team['Egalite']
        if team['Nb_Matchs'] != 0:
            team['Pts_Matchs'] = (Decimal(team['Points']) / Decimal(team['Nb_Matchs'])).quantize(Decimal('0.01'))
        else:
            team['Pts_Matchs'] = '-'
        infos.append(team)
    return dict(teams=sorted(infos, key=lambda team:team['Points'], reverse=True))

def get_calendar(team_id):
    payload = {}
    payload['idEquipe'] = team_id
    result = requests.post('http://www.football-loisir-amateur.com/Home/GetRencontreDuneTeam/', data=payload)

    infos = []
    for journee in result.json():
        journee['Date'] = get_date(journee['Date'])
        dom = journee['Scoredom']
        ext = journee['Scoreext']
        html_class = 'grey'
        if dom is not None:
            #On regarde si victoire ou défaite
            if int(journee['IdEquipeDom']) == team_id:
                result, html_class = is_victory(dom, ext)
            else:
                result, html_class = is_victory(ext, dom)
            journee['Result'] = result
        journee['html_class'] = html_class
        infos.append(journee)
    return infos

def get_date(_date_str):
    try:
        _date = _date_str[6:-2]
    except TypeError:
        return 'inconnu'
    if len(_date) != 13:
        raise AssertionError(_date)
    return (
        datetime.datetime.fromtimestamp(
            int(_date) / 1000
        ).strftime('%Y-%m-%d %H:%M:%S')
    )

def is_victory(score_fous, score_others):
    if score_fous > score_others:
        return 'Victoire', 'green'
    elif score_fous == score_others:
        return 'Nul', 'grey'
    else:
        return 'Defaite', 'red'