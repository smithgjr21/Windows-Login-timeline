#!/usr/bin/env python3
"""Analyze simplified CSV exports of Windows Security events 4624/4625."""
import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path

def analyze(csv_path, threshold=3):
    events=[]
    with Path(csv_path).open(newline='',encoding='utf-8-sig') as f:
        for i,row in enumerate(csv.DictReader(f),start=2):
            if row['event_id'] not in {'4624','4625'}: continue
            try:when=datetime.fromisoformat(row['timestamp'].replace('Z','+00:00'))
            except ValueError as e:raise ValueError(f'Invalid timestamp at CSV line {i}') from e
            if when.tzinfo is None:raise ValueError(f'Missing timezone at CSV line {i}')
            events.append({'timestamp_utc':when.astimezone(timezone.utc).isoformat(), 'event_id':row['event_id'],
                           'account':row['account'],'source_ip':row['source_ip'],'host':row['host']})
    events.sort(key=lambda e:e['timestamp_utc'])
    failures=defaultdict(int)
    for event in events:
        if event['event_id']=='4625':failures[(event['source_ip'],event['account'])]+=1
    flags=[{'source_ip':ip,'account':account,'failed_login_count':count} for (ip,account),count in sorted(failures.items()) if count>=threshold]
    return {'timeline':events,'repeated_failures':flags,'notes':'Training heuristic: counts failures across full supplied dataset; does not establish brute force or account compromise.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('csv_file');parser.add_argument('--threshold',type=int,default=3);parser.add_argument('--output');a=parser.parse_args()
    if a.threshold<1:parser.error('threshold must be >= 1')
    result=json.dumps(analyze(a.csv_file,a.threshold),indent=2)
    if a.output:Path(a.output).write_text(result+'\n',encoding='utf-8')
    print(result)
if __name__=='__main__':main()
