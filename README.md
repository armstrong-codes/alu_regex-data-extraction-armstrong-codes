## Project Overview

This Python project uses **Regular Expressions (regex)** to extract structured data from large string responses. It's ideal for parsing API responses or large blocks of web data to find specific structured content.

---

## Features

This tool extracts the following data types:
- Email addresses  
- URLs  
- Phone numbers (various formats)  
- Credit card numbers  
- Time (12-hour and 24-hour formats)  
- HTML tags  
- Hashtags  
- Currency amounts  

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/armstrong-codes/alu_regex-data-extraction-armstrong-codes.git
cd alu_regex-data-extraction-armstrong-codes
```
### 2. Run the Code

Make sure you have Python 3 installed. Then run:
- python main.py

## Sample Output

EMAILS:
 - user@example.com
 - firstname.lastname@company.co.uk

URLS:
 - https://www.example.com
 - http://site.org
 - https://sub.example.org/page/

PHONE_NUMBERS:
 - (123) 456-7890
 - 123-456-7890
 - 123.456.7890
 - +1 800 555 1212

CREDIT_CARDS:
 - 1234 5678 9012 3456
 - 1234-5678-9012-3456

TIMES:
 - 14:30
 - 2:30 PM

HTML_TAGS:
 - <div class="box">
 - <p>
 - </p>
 - </div>
 - <img src="img.jpg" alt="img">

HASHTAGS:
 - #regex
 - #Python3
 - #ThisIsAHashtag

CURRENCY:
 - $19.99
 - $1,234.56
 - $1000000.00

## Testing (Optional)

To test individual patterns, you can create a test file like test_main.py and write pattern-based checks. Let me know if you'd like that setup.

## Author

Hirwa Armstrong
ALU Email: a.hirwa2@alustudent.com
