from selene import be, have, browser, command
import os


def test_demo_registration(browser_config):
    browser.open('automation-practice-form')
    browser.element('footer').execute_script('element.remove()')
    browser.element('#firstName').type('Maria')
    browser.element('#lastName').type('Ivanova')
    browser.element('#userEmail').type('MIvanova@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1983"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element('#subjectsInput').type('soc').press_enter()
    browser.driver.execute_script('window.scrollBy(0, 80)')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/image.jpg')
    browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('Maria Ivanova'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('MIvanova@gmail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Other'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('1234567890'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('17 December,1983'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Social Studies'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('image.jpg'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Haryana Karnal'))
    browser.element('[id="closeLargeModal"]').perform(command.js.click)

