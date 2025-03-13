import requests
from bs4 import BeautifulSoup
import time
import random

def scrape_sports_reference_stats(team_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(team_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        stats_table = soup.find('table', {'id': 'basic_school_stats'})
        if stats_table:
            headers_list = [th.text for th in stats_table.find('thead').find_all('th')][1:]
            rows = stats_table.find('tbody').find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    data.append([col.text for col in cols])

            if data:
                stats_dict = dict(zip(headers_list, data[0]))
                selected_stats = {
                    'PTS': stats_dict.get('PTS', '0'),
                    'Opp PTS': stats_dict.get('Opp PTS', '0'),
                    'FG%': stats_dict.get('FG%', '0'),
                    'Opp FG%': stats_dict.get('Opp FG%', '0'),
                    'TRB': stats_dict.get('TRB', '0'),
                    'AST': stats_dict.get('AST', '0'),
                    'STL': stats_dict.get('STL', '0'),
                    'BLK': stats_dict.get('BLK', '0')
                }
                return selected_stats
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {team_url}: {e}")
        return None

def scrape_kenpom_ratings(team_name):
    try:
        team_name_kenpom = team_name.lower().replace(' ', '')
        kenpom_url = f"https://kenpom.com/team.php?team={team_name_kenpom}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(kenpom_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        adj_o = soup.find('td', {'data-field': 'adjoe'}).text.strip()
        adj_d = soup.find('td', {'data-field': 'adjde'}).text.strip()
        adj_t = soup.find('td', {'data-field': 'adjtempo'}).text.strip()

        return {'AdjO': float(adj_o), 'AdjD': float(adj_d), 'AdjT': float(adj_t)}
    except requests.exceptions.RequestException as e:
        print(f"Error scraping KenPom for {team_name}: {e}")
        return None
    except AttributeError:
        print(f"Could not find kenpom data for {team_name}")
        return None

def scrape_net_rating(team_name):
    try:
        team_name_ncaa = team_name.lower().replace(' ', '-')
        ncaa_url = f"https://www.ncaa.com/teams/basketball-men/{team_name_ncaa}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(ncaa_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        net_rating_element = soup.find('div', class_='field--name-field-net')
        if net_rating_element:
            net_rating = net_rating_element.find('div', class_='field__item').text.strip()
            return {'NET': int(net_rating)}
        else:
            print(f"NET rating not found for {team_name}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error scraping NCAA for {team_name}: {e}")
        return None
    except AttributeError:
        print(f"Could not find ncaa data for {team_name}")
        return None
