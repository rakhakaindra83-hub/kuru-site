from pathlib import Path
from playwright.sync_api import sync_playwright

url = 'https://rakhakaindra83-hub.github.io/kuru-ocean-studio/'
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.route(url, lambda route: route.fulfill(body='Commission destination verified'))
    page.goto(Path('index.html').resolve().as_uri())
    page.locator('#splash').click()
    page.locator('#ocean-commission-link').scroll_into_view_if_needed()
    page.wait_for_timeout(1200)
    page.screenshot(path='portal-preview.png')
    page.locator('#ocean-commission-link').click()
    page.wait_for_selector('.ocean-transition.active')
    assert page.url != url
    page.wait_for_url(url)
    reduced = browser.new_page(reduced_motion='reduce', viewport={'width': 390, 'height': 844})
    reduced.route(url, lambda route: route.fulfill(body='Reduced motion destination verified'))
    reduced.goto(Path('index.html').resolve().as_uri())
    reduced.locator('#splash').click()
    reduced.locator('#ocean-commission-link').focus()
    reduced.keyboard.press('Enter')
    reduced.wait_for_url(url)
    print('PASS: commission portal effect precedes navigation; keyboard/reduced-motion navigation works.')
    browser.close()
