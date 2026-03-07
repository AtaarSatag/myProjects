It is a downloader for documents from Issuu ([issuu.com](https://issuu.com)). To use it run [main.py](https://github.com/AtaarSatag/myProjects/blob/main/issuuDownloader/main.py), then enter a URL of document what you want to download, press "Enter" and wait for the finish, e.g.:

```bash
python main.py
Enter a document URI (URL) like https://issuu.com/europan/docs/doc-on-a-topic: https://issuu.com/lapthornmedia/docs/architect_projects_-_march_2026
Response: 200 OK

Document title: Architect Projects - March 2026
Pages: 49
Start the task

URI: https://svg.issuu.com/260226110712-0ad321a8324b6956644e947c5a2c1934/page_1.svg
Number of page: 1/49
Downloading
[66183:66199:0308/014430.208652:ERROR:net/cert/ev_root_ca_metadata.cc:161] Failed to decode OID: 0
654134 bytes written to file /home/yankie/vool/dev/downloading-files/oSpRAgKNgG/1.pdf
Downloaded

URI: https://svg.issuu.com/260226110712-0ad321a8324b6956644e947c5a2c1934/page_2.svg
Number of page: 2/49
Downloading
[66320:66339:0308/014431.182020:ERROR:net/cert/ev_root_ca_metadata.cc:161] Failed to decode OID: 0
346059 bytes written to file /home/yankie/vool/dev/downloading-files/oSpRAgKNgG/2.pdf
Downloaded
...
```

The downloaded document will be in a working directory.

# Dependencies

To run the downloader you need:
- requests (`pip install requests`) 
- beautifulsoup4 (`pip install beautifulsoup4`)
- chrome/chromium (the downloader uses a CLI utility to perform PDF render)(to get chromium: [https://www.chromium.org/getting-involved/download-chromium/](https://www.chromium.org/getting-involved/download-chromium/), to get chrome: [https://www.google.com/chrome/](https://www.google.com/chrome/))
- pdfunite (to use this utility you will need poppler:
-- windows (maybe): [https://github.com/oschwartz10612/poppler-windows](https://github.com/oschwartz10612/poppler-windows)
-- linux: use your package manager (the package may be called as poppler-utils or poppler (you should clarify it)
