url_basic = [
    "have_ip",
    "netloc_too_long",
    "have_unusual",
    "in_phish_tank",
    "have_redirect"
]
url_advance = [
    "low_pr",
    "create_less_3_month",
]
html = [
    "have_script",
]
plain = [
    "abnormal_time",
    "inducible_title",
    "inducible_content"
]
attached = [
    "unusual_size",
    "trick_type"
]

full_check_items = []
for items in [url_basic, url_advance, html, plain, attached]:
    full_check_items.extend(items)
