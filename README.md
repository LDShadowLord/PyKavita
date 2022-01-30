# PyKavita
A Python Wrapper API for Kavita

A basic wrapper API for Kavita (kavitareader.com). Not feature complete, does not implement every possible API endpoint available. This is a MVP.

All you need is Requests, your API endpoint accessible (kavita.example.com/api/), and your API key.

In most instances the endpoints exposed via this wrapper are for a single method, either GET or POST.
If you want additional endpoints added, or additional methods added, then raise an issue or use a pull request to submit your own code.

Current Available Endpoints:
* /Server/server-info
* /Server/backup-db
* /Server/clear-cache

* /Series/*
* /Series/metadata
* /Series/scan

* /Library/scan
