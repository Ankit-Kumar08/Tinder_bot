from selenium import webdriver
from secret import username,password
from time import sleep

class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')

        sleep(2)

        privacy_accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        privacy_accept.click()

        login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        #login_btn.click()

        try:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
        except Exception:
            more_options = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_options.click()
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()



        #switch window
        base_win = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        log_in = self.driver.find_element_by_xpath(('//*[@id="u_0_0"]'))
        log_in.click()

        sleep(10)
        #switch back to base
        self.driver.switch_to.window(base_win)

        allow_location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location.click()

        #prevent notification
        prevent_notific = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        prevent_notific.click()

        #allow notification
        #allow_notific = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        #allow_notific.click()

    def like(self):
            like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_btn.click()

    def dislike(self):
            dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
            dislike_btn.click()

    def auto_swipe(self):
            while True:
                sleep(0.5)
                try:
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        pass
                    try:
                        self.close_match()
                    except Exception:
                        pass
                    try:
                        self.out_of_likes()
                    except Exception:
                        pass

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    #close ur window on out of likes
    def out_of_likes(self):
        popup_4 =self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        self.driver.close()
        exit()



bot = TinderBot()
bot.login()
sleep(10)
bot.auto_swipe()










