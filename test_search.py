from selene import browser, be, have, by


def test_search_positive():
    browser.open('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('b').should(have.text('Об этой странице'))


def test_search_negative():
    browser.open('https://google.com')
    if browser.element(by.text('Принять все')).matching(be.visible):
        browser.element(by.text('Принять все')).click()
    browser.element('[name="q"]').should(be.blank).type('yhhggtrf').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу yhhggtrf ничего не найдено.'))
