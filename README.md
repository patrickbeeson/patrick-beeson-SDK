# Lord of the Rings SDK

This SDK is a partial implementation of the [Lord of the Rings API](https://the-one-api.dev/).

## Installing the SDK

The LOTR SDK is installable from PyPi: `pip install -i https://test.pypi.org/simple/ lotr-sdk-patrick-beeson==0.0.1`

Dependencies are located in the `requirements.txt` file.

Note that you'll need to create a `.env` file and populate the required
values in order to use this package. This will require registering for a
bearer token at the source API website.

See the `.env.dev` file for what's expected.

## How to use this SDK

Once installed along with the dependecies, you can
import into your project and instantitate the rest client to request JSON
data from the LOTR API:

```
from rest import client

client = Client()
client.movie.get() # returns JSON payload for all LOTR movies
client.movie.get()['status'] # returns status code
```

Paramaters for drilling into individual content records and sorting,
filtering and limiting results is also supported:
* Individual record: `client.quote.get(id='5cd96e05de30eff6ebccf13f')`
* Sorting: `client.quote.get(params={'sort':'character:desc'})`
* Pagination: `client.quote.get(params={'page':2})`
* Limting: `client.quote.get(params={'limit': 1})`

## Running tests

Tests are available within the project `test` module and currently
cover happy-path cases. You can run them using Python's Unittest discover
method or individually.


## Additional document and resources

Please see the [https://the-one-api.dev/documentation](LOTR API documentation) for
more information and use restrictions.
