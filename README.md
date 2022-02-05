# PyKavita
## A Python Wrapper API for Kavita

A basic wrapper API for Kavita (kavitareader.com). Not feature complete, does not implement every possible API endpoint available. This is a MVP.

All you need is Requests, your API endpoint accessible (kavita.example.com/api/), and your API key.

In most instances the endpoints exposed via this wrapper are for a single method, either GET or POST. If you want to see what endpoints are currently supported, check [EndPoints.md](EndPoints.md)
If you want additional endpoints added, or additional methods added, then raise an issue or use a pull request to submit your own code.

### Example Code
It's super simple to use this wrapper. Just import it like a normal function.
Depending on how you're using the wrapper, your import statement might be slightly different.
```
from PyKavita import Kavita
kav = Kavita.Kavita(your_url_endpoint,your_apikey)
if kav.libraryScan(5)[0]:
    d.print("Succesfully initiated Library Scan")
else:
    d.print("Failed to initiate Library Scan")
```
