# coding: utf-8
import csv
import webbrowser

with open('papers.csv') as f:
    papers = list(csv.reader(f))

print(f'Proposing {len(papers)} papers')
print('')

for idx, (title, url) in enumerate(papers, start=1):
    print(f'Paper {idx:02d}/{len(papers)}')
    print('Title:')
    print(f'    "{title}"')
    response = input('Interested? (y/n) ')
    if response in ['y', 'Y', 'yes', 'Yes']:
        webbrowser.open(url)
    print('')

