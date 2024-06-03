from Scraper import scraper
from Extractor import notebookExtractor, scriptExtractor

if __name__ == "__main__":
    args = input("Select file format: (default is ipynb) ")
    
    data = scraper()
    
    if args.lower() == "py":
        scriptExtractor(data)
    else:
        notebookExtractor(data)
    