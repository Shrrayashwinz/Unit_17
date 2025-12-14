"""
Program Name: lab17_ssrinivasan3-1.py

Author: Shrrayash Srinivasan

Purpose: I refactored the HN submission py to ensure it safely handles the missing data fields and prevents KeyError crashes.

Date: December 11, 2025 
"""

from operator import itemgetter
import requests

# 🔧 Fixed typo in comment
"""Get an API call and store the response."""

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

    # 🔧 Added status code check to skip failed requests
    if r.status_code != 200:
        print(f"Skipping submission {submission_id} — API call failed.")
        continue

    response_dict = r.json()

    # 🔧 Added check for empty or malformed response
    if not response_dict:
        print(f"Skipping submission {submission_id} — empty response.")
        continue

    """Build a dictionary for each submission."""
    submission_dict = {
        'title': response_dict.get('title', 'No Title'),  # 🔧 Uses .get() to avoid KeyError
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)  # 🔧 Uses .get() with default value
    }
    submission_dicts.append(submission_dict)

# 🔧 Filter out any entries missing 'comments' key before sorting
submission_dicts = [d for d in submission_dicts if 'comments' in d]

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

"""Print the top submissions."""
# 🔧 Optional: limit to top 10
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")











