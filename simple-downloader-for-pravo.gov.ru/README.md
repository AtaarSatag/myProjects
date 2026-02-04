This python module is a simple downloader of PDF of publications from pravo.gov.ru. The main feature is batch downloading for a specific period (e.g., for 1.2.2016-23.4.2023). To perform that you should call `download_documents_for_period` and specify the following parameters:

- `from_date` is a start date from which you need to start batch downloading
- `to_date` is an end date of the period.

The date parameters are lists or tuples and their format is `[day: int, month: int, year: int]`. You can also specify a save path, a default value is `./` (a working directory).
