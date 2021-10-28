# coding: utf-8
"""Inspired by
https://medium.com/@sdoshi579/to-read-emails-and-download-attachments-in-python-6d7d6b60269
"""

from collections import namedtuple
import csv
import email
from getpass import getpass
import imaplib
from pathlib import Path

from bs4 import BeautifulSoup
from more_itertools import flatten
import parse


Paper = namedtuple('Paper', 'title url')
direct_url_format = parse.compile('http{s}://scholar.google.nl/scholar_url?url={url}&hl=en&{garbage}')
indirect_url_format = parse.compile('{url}&hist={garbage}')


def main():
    emails = get_and_delete_all_emails_from('Papers/Scholar Alerts')
    all_papers = list(flatten(get_papers_from_email(mail) for mail in emails))
    unique_papers = set(all_papers)

    print(f'Found {len(unique_papers)} ({len(all_papers)}) papers in {len(emails)} emails')

    write_papers_to_csv(unique_papers)


def get_and_delete_all_emails_from(folder, server='mail.campus.leidenuniv.nl', port=993, delete=False):
    if ' ' in folder:
        folder = f'"{folder}"'

    with imaplib.IMAP4_SSL(server, port) as mail:
        mail.login(input("Username: "), getpass("Password: "))

        mail.select(folder)
        res, data = mail.search(None, 'ALL')
        emails = [get_email(num, mail) for num in data[0].split()]

        if delete:
            # delete all emails once successfully fetched
            for num in data[0].split():
                mail.store(num, '+FLAGS', '\\Deleted')
            mail.expunge()

    return emails


def get_papers_from_email(mail, link_class='gse_alrt_title'):
    msg = email.message_from_string(mail.decode('utf-8'))
    if msg.is_multipart():
        mail_html = msg.get_payload(0).get_payload(decode=True)
    else:
        mail_html = msg.get_payload(decode=True)

    if mail_html is None:
        raise TypeError("'msg' incorrectly parsed, None returned")

    soup = BeautifulSoup(mail_html, 'html.parser')
    return [
        Paper(link.text.title(), clean_url(link.get('href')))
        for link in soup.find_all('a', link_class)
    ]


def write_papers_to_csv(unique_papers, fname='papers.csv'):
    with open(fname, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(unique_papers)


def get_email(num, mailclient):
    status, ((code, data), flags) = mailclient.fetch(num, '(RFC822)')
    return data


def clean_url(url):
    try:
        return direct_url_format.parse(url)['url']
    except TypeError:
        return indirect_url_format.parse(url)['url']


if __name__ == '__main__':
    main()
