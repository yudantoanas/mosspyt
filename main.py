from utils import Scraper, filesCopier, notebookExtractor

if __name__ == "__main__":
    scraper = Scraper(
        input("RDP Host: "),
        input("RDP Port: "),
        input("Local Directory: "),
    )

    data = scraper.play(
        input("Classroom Assignment URL: "),
        input("Github Repository Prefix: ")
    )

    args = input("Select file format: (default is ipynb) ")
    if args.lower() == "py":
        filesCopier(data)
    else:
        notebookExtractor(data)
