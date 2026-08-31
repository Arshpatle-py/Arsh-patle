import re

EMAIL_PATTERN = r'\w+(?:[.-]\w+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}'


def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


if __name__ == "__main__":

    sample_text = """
    Contact us at admin@company.com
    Support: help-desk@service.org
    Sales: sales.team@business.co.in
    Rahul: rahul_23@gmail.com
    Invalid: @example.com, user@site, hello@
    Offers: offers+today@shopping.net
    """

    print("Original text:")
    print(sample_text)

    found = find_emails(sample_text)

    print(f"Found {len(found)} email address(es) in the text:")

    for email in found:
        print(f"  - {email}")

    print("\nValidating individual strings:")

    test_cases = [
        "john.doe@gmail.com",
        "student_123@college.edu",
        "invalid-email",
        "user@site",
        "hello@",
        "rahul_23@company.co.in",
    ]

    for candidate in test_cases:
        result = "VALID" if is_valid_email(candidate) else "INVALID"
        print(f"  {candidate:30s} -> {result}")
