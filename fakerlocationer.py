"""
    Used to set the geolocation of a webdriver
"""

class FakerLocationer(object):
    def __init__(self, driver):
        self.driver = driver

    ##
    # @brief Returns webdriver in use
    def returnDriver(self):
        return self.driver

    ##
    # @brief Sets geolocation of webdriver
    def setLocation(self, latitude, longitude):
        self.driver.execute_script(
            "navigator.geolocation.getCurrentPosition = (s, e) => {s({coords: {latitude: " + str(latitude) + ",longitude: " + str(longitude) + "}});};")
