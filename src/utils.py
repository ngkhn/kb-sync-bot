import re


def slugify(title: str) -> str:
    """
    Convert article title to filename.

    Example:
    'Using the Japan Earthquake App'
    ->
    'using-the-japan-earthquake-app'
    """

    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")

    return slug