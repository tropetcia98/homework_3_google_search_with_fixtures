from selene import browser, have


def test_positive_search_selene(browser_google):
    browser.open('')
    browser.element('[name=q]').type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search(browser_google):
    browser.open('')
    browser.element('[name=q]').type('asdfafdadsf12233фывалдж').press_enter()
    browser.element('.card-section').should(have.text('По запросу asdfafdadsf12233фывалдж ничего не найдено.'))
