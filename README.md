# Multi-Level Co-Surrogates

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


## Installation

```bash
git clone git@github.com:sjvrijn/deduplicate-scholar-alerts.git
cd deduplicate-scholar-alerts
python -m venv venv
source venv/bin/activate  # or source venv\Scripts\activate on Windows
pip install -r requirements.txt
```


## Usage

```bash
deduplicate-scholar-alerts$ python get_emails.py -h
usage: get_emails.py [-h] [--server SERVER] [--port PORT] [--folder FOLDER] [--username USERNAME]
                     [--password PASSWORD] [--delete] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --server SERVER       Address of the mailserver to use. Default: mail.campus.leidenuniv.nl
  --port PORT           At which port to connect to the mailserver. Default: 993
  --folder FOLDER       Mailbox folder containing all Scholar Alert emails. Default: "Papers/Scholar Alerts"
  --username USERNAME   Username of the email account to log into
  --password PASSWORD   Password of the email account to log into
  --delete, -d          Whether to delete emails after processing. Default: False
  --output OUTPUT, -o OUTPUT
                        Name of the output file. Default: papers.csv
```

### Example

```bash
deduplicate-scholar-alerts$ python get_emails.py
Username: rijnsjvan
Password:
Found 0 (0) papers in 0 emails
```
