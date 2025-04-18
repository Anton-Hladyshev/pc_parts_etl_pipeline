import re
from app.constants import STOPWORDS, FILTERS


def is_corresponding_to_category(product: str, cat: str) -> bool:
    cat = cat.replace(' ', '_')
    assert cat.lower() in ["cpu", "graphics_card", "ram"], "Error: no such category"
    pattern_manufacturer = "|".join(FILTERS[cat.lower()]["manufacturers"])
    pattern_keywords = "|".join(FILTERS[cat.lower()]["keywords"])

    if re.search(pattern_manufacturer, product.lower()) or re.search(pattern_keywords, product.lower()):
        return True

    else:
        return False


def has_not_stopwords(product: str, cat: str) -> bool:
    cat = cat.replace(' ', '_')
    product = product.split(',')[0]
    pattern_stopwords = "|".join(FILTERS[cat.lower()]["stopwords"])

    if not re.search(pattern_stopwords, product, re.IGNORECASE):
        return True
    else:
        return False


def is_targeted_product(product_name: str, cat: str) -> bool:
        if is_corresponding_to_category(product_name, cat) and has_not_stopwords(product_name, cat):
            print("It is targeted product")
            return True
        else:
            print(f"No: {product_name}")
            return False
