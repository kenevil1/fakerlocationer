# FakerLocationer

A simple class that can be used to fake Selenium Browser Geolocation

## Getting Started

Its very easy to get started with using fakerlocationer. A simple example is shown in usage.py or you can see it below:

'''
from fakerlocationer import FakerLocationer
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.mylocation.org")
f = FakerLocationer(driver)
f.setLocation(50, 50)
'''python

The only drawbacks of fakerlocationer are that in order for the geolocation to change the page must be fully loaded, and if the page refreshes/changes it'll reset the geolocation

### Prerequisites

Pretty much only need Selenium and Python 3

### Installing

Can be installed by using pip:

'''
pip3 install fakerlocationer
'''

Or just by literally downloading fakerlocationer.py and importing it into your project

## Built With

* [Selenium](https://selenium.dev/documentation/en/webdriver/) - Selenium Framework

## Authors

* **kenevil1** - [kenevil1](https://github.com/kenevil1)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* To Selenium for making the web testing suite :)
