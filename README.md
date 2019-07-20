# Facebook backend

This repository contains the back-end functionality for the 2019 Facebook-Adglow 
hackaton project my team presented to **win the hackaton!** 🎉


## How does it work?
The project backend comprises a [Flask][flask-webpage] WSGI that serves data
by mapping requests to SQL queries.

### Components integration
There is another developed software piece for this hackaton, which correspond
to the front-end interface used to represent data provided by this backend.
If interested, take a look to the [Hackaton front-end][frontend-repo], as the
combination of both repositories forms the complete hackaton submission.

### Server endpoints

#### Ad stats
- Host: `localhost:5000`
- Request: `GET`
- Endpoint: `/get_ad_stats`
- Arguments:
 - `ad_id`

#### Generic data
- Host: `localhost:5000`
- Request: `GET`
- Endpoint: `/get_data`
- Arguments:
 - `table_name`
 - `table_columns`
 - `table_conditions` (optional)
 
#### Tags stats
- Host: `localhost:5000`
- Request: `GET`
- Endpoint: `/get_tags_stats`
- Response:
	- avg(stats.STA_spent)
	- avg(stats.STA_IMPRESSIONS)
	- avg(stats.STA_CLICKS)
	- avg(stats.STA_CTR)
	- avg(stats.STA_AGV_CPM)
	- avg(stats.STA_AGV_CPC)
	- avg(stats.STA_CONVERSION)


## What is in the repository?
The repository contains a couple of Python modules related with the Flack web server,
in addition to a folder with all the SQL related stuff:
```yaml
app.py: main application entrypoint.
encoders.py: data transformations.
/database:
    # Files
    extractor.py: maps requests to Python functions.
    credentials.py: secrets to connect to the mySQL instance.
    
    # Folders
    /queries: contains the .sql.
        ...
```

## Usage
To start the web server, just execute:
```sh
python3 src/app.py
```


# Team
- [Daniel Fernández](https://github.com/ferreiro)
- [Jorge Ferreiro](https://github.com/ferreiro)
- [Sinclert Pérez](https://github.com/Sinclert)
- [Gloria Vazquez](https://github.com/GloriaVazquezVidal)
- Madeleine (No GitHub)


[flask-webpage]: https://palletsprojects.com/p/flask/
[frontend-repo]: https://github.com/ferreiro/facebook-hackathon
