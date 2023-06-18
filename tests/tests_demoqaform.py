import os
from selene import browser, have


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivan@example.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('89881234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="9"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2000"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Autotest')
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/Ivan.jpg'))
    browser.element('#currentAddress').type('Mira str., 5')
    browser.element('#state').click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('//*[.="NCR"]').click()
    browser.element('#city').click()
    browser.element('//*[.="Delhi"]').click()
    browser.element('#state').click()
    browser.element('#submit').click().press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
