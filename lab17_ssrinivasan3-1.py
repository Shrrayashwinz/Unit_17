"""
Program Name: lab17_ssrinivasan3-1.py

Author: Shrrayash Srinivasan

Purpose: I refactored the HN submission py to ensure it safely handles the missing data fields and prevents KeyError crashes.

Date: December 11, 2025 
"""

from operator import itemgetter
import requests

"""Get an API call and store the respone."""

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

"""Process information about each submission."""
submission_ids = r.json()
submission_dicts = []


for submission_id in submission_ids[:30]: 

    """Make a separate API call for each submission."""


    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"

    r = requests.get(url)

    response_dict = r.json()

    """Build a dictionary for each submission."""

    submission_dict = {
        'title': response_dict.get('title', 'No Title'),

        'link': f"http://news.ycombinator.com/item?id={submission_id}",

        """FIXED: Now avoids KeyError"""
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


"""Print the top submissions."""
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")




