import requests
import os
import pandas as pd
import json
import numpy as np
from dotenv import load_dotenv
load_dotenv()

class ApiFootball():
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.base_url = "https://v3.football.api-sports.io/"


    def get_leagues(self, leagues_ids=None, season=None, country=None, team=None, type=None):
        url = self.base_url + "leagues"
        payload={}
        headers = {
            'x-apisports-key': self.api_key
        }
        params = {
            'season': season,
            'country': country,
            'team': team,
            'type': type
        }
        if leagues_ids:
            ids = ','.join(map(str, leagues_ids))
            url += f"?id={ids}"

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_fixtures(self, league_id=None, season=None, fixture_id=None):
        url = self.base_url + "fixtures?"
        payload={}
        headers = {
            'x-apisports-key': self.api_key
        }
        params = {
            'league': league_id,
            'season': season,
            'id': fixture_id
        }

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_teams(self, league_id=None, season=None, country=None):
        url = self.base_url + "teams?"
        payload={}
        headers = {
            'x-apisports-key': self.api_key,
        }
        params = {
            'league': league_id,
            'season': season,
            'country': country
        }

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_fixture_statistics(self, fixture_id=None, team=None):
        url = self.base_url + f"fixtures/statistics?"
        payload={}
        headers = {
            'x-apisports-key': self.api_key,
        }
        params = {
            'fixture': fixture_id,
            'team': team
        }

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_h2h(self, teams_id=None, season=None, league_id=None, from_date=None, to_date=None, last=None):
        url = self.base_url + f"fixtures/headtohead?"
        payload={}
        headers = {
            'x-apisports-key': self.api_key,
        }
        params = {
            'h2h': '-'.join(map(str, teams_id)),
            'season': season,
            'league': league_id,
            'from': from_date,
            'to': to_date,
            'last': last
        }

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_injuries(self, league_id=None, season=None, fixture_id=None):
        url = self.base_url + f"injuries?"
        payload={}
        headers = {
            'x-apisports-key': self.api_key,
        }
        params = {
            'league': league_id,
            'season': season,
            'fixture': fixture_id
        }

        response = requests.request("GET", url, headers=headers, data=payload, params=params)
        res = response.json()
        return res
    
    def get_status(self):
        url = self.base_url + f"status"
        payload={}
        headers = {
            'x-apisports-key': self.api_key,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        res = response.json()
        return res