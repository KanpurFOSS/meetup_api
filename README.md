# Meetup API

Alternate API to get events from the Meetup website. Send a POST request with the URL of the event page of the meetup group for which you want the information.

## How to use

* Install the requirements using `pip install -r requirements.txt`

* Run the app using `gunicorn -b localhost:8000 app:app`

* Send POST request using:

```bash
curl -X POST http://localhost:8000/get_events -d "url=https://www.meetup.com/pydelhi/events/"
```

## Expected Resopnse

The API will return a JSON with `all_events` containing a list of all events. Example response is shown below:

```json
{
    "all_events": [
        {
            "link": ,
            "title": ,
            "datetime": ,
            "datetime_str": ,
            "location":
        }
    ]
}
```
