#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
import os
import requests
import datetime
from decimal import Decimal
from collections import OrderedDict
import json


def get_classement(championnat_id, saison_id):
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
        journee['Date_str'] = get_date_str(journee['Date'])
        journee['Date_fr'] = get_date(journee['Date'])
        score_dom = journee['Scoredom']
        score_ext = journee['Scoreext']
        html_class = 'grey'
        if score_dom is not None:
            #On regarde si victoire ou défaite
            if int(journee['IdEquipeDom']) == team_id:
                result, html_class = is_victory(score_dom, score_ext)
            else:
                result, html_class = is_victory(score_ext, score_dom)
            journee['Result'] = result
        journee['html_class'] = html_class
        infos.append(journee)
    return infos


def get_date_str(_date_str):
    try:
        _date = _date_str[6:-2]
    except TypeError:
        return 'inconnu'
    if len(_date) != 13:
        raise AssertionError(_date)
    return (
        datetime.datetime.fromtimestamp(
            int(_date) / 1000
        ).strftime('%Y-%m-d %H:%M')
    )


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
        ).strftime('%A %d/%m/%Y %H:%M')
    )


def is_victory(score_fous, score_others):
    if score_fous is None:
        return 'Nul', 'grey'
    if score_fous > score_others:
        return 'Victoire', 'green'
    elif score_fous == score_others:
        return 'Nul', 'orange'
    else:
        return 'Defaite', 'red'


def fetch_opponents():
    '''
    On lit les fichiers JSON
    '''
    path_jsons = os.path.dirname(__file__) + '/json_infos/'

    dict_opponents = dict()
    for root, dirs, files in os.walk(path_jsons):
        for cur_file in files:
            json_raw = open(path_jsons + '/' + cur_file).read()
            add_opponents(dict_opponents, json_raw)

    for adv in dict_opponents:
        for journee in dict_opponents[adv]:
            journee['Date'] = get_date(journee['DateDebut'])
            dom = journee['NameDom']
            ext = journee['NameExt']
            score_dom = journee['ScoreDom']
            score_ext = journee['ScoreExt']

            if not_fous(dom):
                result, html_class = is_victory(score_ext, score_dom)
            else:
                result, html_class = is_victory(score_dom, score_ext)
            journee['Result'] = result
            journee['html_class'] = html_class
            journee['Equipedom'] = dom
            journee['Equipeext'] = ext
            journee['Scoredom'] = score_dom
            journee['Scoreext'] = score_ext
        
    od = OrderedDict(sorted(dict_opponents.items()))
    return dict(opponents=od)

def not_fous(name):
    if name == 'LES FOUS DU STADE FC':
        return False
    if name == 'LES FOUS 11 ':
        return False
    return True

def add_opponents(dict_opponents, json_raw):
    json_content = json.loads(json_raw)
    for journee in json_content:
        
        if not_fous(journee['NameDom']):
            name = journee['NameDom']
        else:
            name = journee['NameExt']
        
        #Ajout de l'adversaire
        if name not in dict_opponents:
            dict_opponents[name] = [journee]
        else:
            dict_opponents[name].append(journee)
