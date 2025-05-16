import re

# Sample text simulating API response
sample_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit https://www.example.com, http://site.org, or https://sub.example.org/page/.
Call us at (123) 456-7890, 123-456-7890, 123.456.7890, or +1 800 555 1212.
Credit cards used: 1234 5678 9012 3456, 1234-5678-9012-3456.
The meeting is scheduled at 14:30 and 2:30 PM.
Here is some HTML: <div class="box"><p>Hello!</p></div><img src="img.jpg" alt="img">
Check out #regex, #Python3 and #ThisIsAHashtag for updates!
Price: $19.99, $1,234.56 and $1000000.00.
"""

# Correct Regular Expressions
regex_patterns = {
    "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "urls": r"https?://[^\s,]+",
    "phone_numbers": r"(\+?\d{1,2}[\s-])?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
    "credit_cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[APMapm]{2})?\b",
    "html_tags": r"</?[a-zA-Z]+[^>]*>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:\.\d{2})?"
}

# Function to extract matches
def extract_data(text, patterns):
    results = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[key] = matches
    return results

# Display extracted results
def display_results(results):
    for data_type, values in results.items():
        print(f"\n{data_type.upper()}:")
        if values:
            for value in values:
                print(f" - {value}")
        else:
            print(" - No matches found.")

# Main entry point
if __name__ == "__main__":
    extracted_data = extract_data(sample_text, regex_patterns)
    display_results(extracted_data)

