<h1 align="center">Resume Scraper 🎉</h1>
<h2 align="center">

<img src="https://img.shields.io/badge/Python-3.8.0-blue.svg">

<img src="https://img.shields.io/badge/made%20by-A9K5-green.svg" >

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >
</h2>
</h1>
This project is made to scrape a bunch of resumes appended together in a single pdf .
The source code can be easily modified to read a single file at a time or a bunch of different pdf's.

The program will read the pdf and write the data in a csv format to obtain usefull information 
such as User-Email, Mobile Number, Name of the candidate.

Most probably be usefull to the HR guys to go through a bunch of pdf's to extract contact details. 

The sample Resume file is Resume2.pdf.
The output csv file is List2.csv.

<hr>

#### Installation and Usage

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 7.py ./Resume2.pdf
```
<hr>

#### Input Filename
```
Resume2.pdf
```

#### Output filename

```
List2.csv
```

This project uses Python3.

## License
[MIT](https://choosealicense.com/licenses/mit/)