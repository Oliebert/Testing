#ein Klass für Hilfsmethoden

class ContactHelper:

    def __init__(self,app):
        self.app=app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # click Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        #self.open_contact_page()
        #self.select_first_contact()
        # open edit form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        #wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.app.navigation.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value_in_contact("firstname", contact.firstname_of_contact)
        self.change_field_value_in_contact("middlename", contact.middlename_of_contact)
        self.change_field_value_in_contact("lastname", contact.lastname_of_contact)
        self.change_field_value_in_contact("nickname", contact.contactnickname)
        self.change_field_value_in_contact("title", contact.contacttittle)
        self.change_field_value_in_contact("company", contact.contactcompany)
        self.change_field_value_in_contact("address", contact.contactaddress)
        self.change_field_value_in_contact("home", contact.homenumber)
        self.change_field_value_in_contact("mobile", contact.mobilenumber)
        self.change_field_value_in_contact("work", contact.worknumber)
        self.change_field_value_in_contact("fax", contact.contact_fax)
        self.change_field_value_in_contact("email", contact.contact_email)
        self.change_field_value_in_contact("email2", contact.contact_email2)
        self.change_field_value_in_contact("email3", contact.contact_email3)
        self.change_field_value_in_contact("homepage", contact.contact_homepage)
        self.change_field_value_in_contact("address2", contact.contact_address2)
        self.change_field_value_in_contact("phone2", contact.contact_phone2)
        self.change_field_value_in_contact("notes", contact.contact_notes)

        '''wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename_of_contact)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname_of_contact)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.contactnickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.contacttittle)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.contactcompany)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.contactaddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homenumber)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilenumber)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.worknumber)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.contact_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.contact_email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.contact_email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.contact_email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.contact_homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.contact_address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.contact_phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.contact_notes)
    '''

    def change_field_value_in_contact(self, field_name, contact_text):
        wd = self.app.wd
        if contact_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(contact_text)

    def create_contact(self,  contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)

        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_home_page()

    def count_contact(self):  # wie viele Gruppen haben wir auf der Seite
        wd = self.app.wd
        self.open_contact_page()

        return len(wd.find_elements_by_name("selected[]"))
