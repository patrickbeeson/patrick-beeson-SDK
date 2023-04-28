# SDK Design

This SDK for the Lord of the Rings API implements GET requests for the following endpoints:

* `/movie`
* `/movie/{id}`
* `/movie/{id}/quote`
* `/quote`
* `/quote/{id}`

It also supports querystring params for pagination, sorting and filtering.

And although it was designed for a specific set of requirements, it can be extended to
support additional content requests.

To do this would require the addition of additional content class objects that extend the
abstract content type class. There would also be a need to expand how these content types
are defined when building the URL paths.

Allowing for more request methods would be as simple as extending class attributes and
adding the appropriate methods in the client.

The structure of the SDK is similar to the source API with some abstractions in terms
of querystring handling.
