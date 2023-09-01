from datetime import timedelta
from typing import Dict, List

import requests_cache

api_key = "a4f75b4561msh61aa6186cbfd17dp108171jsnb1a516a21fd7"


def get_sources() -> List[Dict]:
    """Valid sources for Biztoc queries."""

    biztoc_session_sources = requests_cache.CachedSession(
        "OpenBB_Biztoc_Pages", expire_after=timedelta(days=7), use_cache_dir=True
    )
    headers = {
        "X-RapidAPI-Key": f"{api_key}",
        "X-RapidAPI-Host": "biztoc.p.rapidapi.com",
    }
    sources = biztoc_session_sources.get(
        "https://biztoc.p.rapidapi.com/sources", headers=headers, timeout=10
    )

    return sources.json()


def get_pages() -> List[str]:
    """Valid pages for Biztoc queries."""

    biztoc_session_pages = requests_cache.CachedSession(
        "OpenBB_Biztoc_Pages", expire_after=timedelta(days=7), use_cache_dir=True
    )
    headers = {
        "X-RapidAPI-Key": f"{api_key}",
        "X-RapidAPI-Host": "biztoc.p.rapidapi.com",
    }
    pages = biztoc_session_pages.get(
        "https://biztoc.p.rapidapi.com/pages", headers=headers, timeout=10
    )

    return pages.json()


def get_tags_by_page(page_id: str) -> List[str]:
    """Valid tags required for Biztoc queries."""

    biztoc_session_tags = requests_cache.CachedSession(
        "OpenBB_Biztoc_Tags", expire_after=timedelta(days=1), use_cache_dir=True
    )
    headers = {
        "X-RapidAPI-Key": f"{api_key}",
        "X-RapidAPI-Host": "biztoc.p.rapidapi.com",
    }
    tags = biztoc_session_tags.get(
        f"https://biztoc.p.rapidapi.com/tags/{page_id}", headers=headers, timeout=10
    )

    return tags.json()


def get_all_tags() -> Dict[str, List[str]]:
    tags: Dict[str, List[str]] = {}

    pages = get_pages()
    for page in pages:
        page_tags = get_tags_by_page(page)
        tags.update({page: [x["tag"] for x in page_tags]})

    return tags