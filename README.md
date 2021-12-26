# SQA Opencart

Run at directory of this repo: `python -m unittest discover .`

## Setup

1. OpenCart, <https://github.com/opencart/opencart>

2. XAMPP v8.0.12, <https://www.apachefriends.org/index.html>. Install location:
   **C:\xampp**

3. Copy the upload folder of OpenCart to **C:\xampp\htdocs\upload**.

4. Enable GD Extension, removed `;` of `;extension=gd` at  **C:\xampp\php\php.ini**

5. Chrome Webdriver. <https://chromedriver.chromium.org/downloads>  
   - Make sure version matched with chrome browser.
   - Extract the executable `chromedriver.exe` and add it to the PATH environment variable.