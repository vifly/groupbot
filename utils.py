from urlextract import URLExtract


def get_urls(message: str) -> list:
    extractor = URLExtract()
    urls = extractor.find_urls(message)
    return urls


def add_to_db(url: str, db_path: str):
    pass


def is_in_db(url: str) -> bool:
    return False
