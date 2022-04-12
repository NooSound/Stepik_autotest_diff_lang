

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.find_element_by_xpath("//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
