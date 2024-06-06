from Scraper import scraper
from Extractor import notebookExtractor, scriptExtractor

if __name__ == "__main__":
    data = scraper(
        input("Port Number: "),
        input("Classroom Assignment URL: "),
        input("Github Repository Prefix: ")
    )

    args = input("Select file format: (default is ipynb) ")
    if args.lower() == "py":
        scriptExtractor(data)
    else:
        notebookExtractor(data)
