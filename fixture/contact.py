#ein Klass für Hilfsmethoden

from model.contact import Contact
import re
import time


class ContactHelper:

    def __init__(self,app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        #self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def change_field_value_in_contact(self, field_name, contact_text):
        wd = self.app.wd
        if contact_text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(contact_text)

    def fill_contact_form(self, contact):
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

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count_contact(self):                                               # wie viele Kontakten haben wir auf der Seite
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):                       # список строк с информацией о контактах
                cells = row.find_elements_by_tag_name("td")                              #список ячеек для каждой строки
                firstname_of_contact = cells[2].text
                lastname_of_contact = cells[1].text
                id = row.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text                # у ячейки берем текст, затем делим на кусочки
                                                          # (у web элемента нет метода splitlines())
                                                          # этот метод используем только если текст выделен специальными тегами

                all_emails = cells[4].text
                adress = cells[3].text
                self.contact_cache.append(Contact(firstname_of_contact=firstname_of_contact, lastname_of_contact=lastname_of_contact, id=id,
                                                all_phones = all_phones, all_emails=all_emails, contactaddress=adress))

        return list(self.contact_cache)

    '''1) получить список строк, которые содержат информацию о контактах
        2) устроить цикл по строкам
        3) для каждой строки получить список ячеек
        cells = row.find_elements_by_tag_name("td")
        4) теперь можно брать текст нужных ячеек
    '''
    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # open edit form
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index+2) + "]/td[8]/a/img").click()
        ##wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % (index+2)).click()
        wd.find_elements_by_xpath("//form[@name='MainForm']//img[@title='Edit']")[index].click()

        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        #wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contact_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_id(id)

        #self.select_contact_by_id(id)
        # open edit form
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(index+2) + "]/td[8]/a/img").click()
        ##wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % (index+2)).click()
        #wd.find_elements_by_xpath("//form[@name='MainForm']//img[@title='Edit']")[index].click()

        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit edit
        wd.find_element_by_name("update").click()
        #wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.open_contact_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):                            # открываем форму редактирования контакта
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self,id):  # открываем форму редактирования контакта

        wd = self.app.wd
        self.open_contact_page()

        checkbox = wd.find_element_by_css_selector("input[value='%s']" % id)
        row = checkbox.find_element_by_xpath("./../..")
        cell = row.find_elements_by_tag_name("td")[7]
        # time.sleep(5)
        cell.find_element_by_tag_name("a").click()
        '''1) найти чекбокс, который имеет нужный модификатор
           2) сложная часть -- от чекбокса подняться вверх к строке, тут помогает xpath
              row = checkbox.find_element_by_xpath("./../..")
           3) внутри строки найти ссылку-кнопку, которая открывает форму модификации
        '''
        '''
        rows = wd.find_elements_by_name("entry")
        tr = 2
        for row in rows:
            tr = tr + 1
            if row == id:
                break
        row = wd.find_elements_by_name("entry")[tr-3]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        # контакты редактируются по порядку , поэтому не работает проверка по id
        '''

    def open_contact_view_by_index(self, index):                                         # просмотр детальной информации
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_conact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname_of_contact= wd.find_element_by_name("firstname").get_attribute("value")
        lastname_of_contact = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homenumber = wd.find_element_by_name("home").get_attribute("value")
        worknumber = wd.find_element_by_name("work").get_attribute("value")
        mobilenumber = wd.find_element_by_name("mobile").get_attribute("value")
        contact_phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        adress = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname_of_contact=firstname_of_contact, lastname_of_contact=lastname_of_contact,
                       mobilenumber=mobilenumber,                 id=id,
                       worknumber=worknumber,                     homenumber=homenumber,
                       contactaddress=adress,
                       contact_email=email,
                       contact_email2=email2,
                       contact_email3=email3,
                       contact_phone2=contact_phone2)

    def get_conact_from_view_page(self, index): # получаем информацию о контактах с обзорной страницы
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text).group(1) # (.*) - группа с произвольными символами до конца строки
                                                         # group()- method - Return the string matched by the RE

        #mobilenumber = re.search("M: (.*)", text).group(1)
        #worknumber = re.search("W: (.*)", text).group(1)
        #contact_phone2 = re.search("P: (.*)", text).group(1)
        return Contact( homenumber=homenumber)
                      # mobilenumber=mobilenumber
                      # worknumber=worknumber,
                       #contact_phone2=contact_phone2)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        # click Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()  # клик на форму подтверждающую удаление контакта
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # click Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()  # клик на форму подтверждающую удаление контакта
        self.contact_cache = None

    def add_contact_to_group(self, contacts_id, groups_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contacts_id)
        #wd.find_element_by_xpath("//input[@id='%s']"% groups_id).click() # не надежный
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % groups_id).click()
        wd.find_element_by_name("add").click()
        self.open_contact_page()

    def remove_contact_from_group (self,contacts_id, groups_id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//form[@id='right']/select//option[@value='%s']" % groups_id) # выбирается группа в выпадающем списке
        wd.find_element_by_xpath("//input[@id='%s']" % contacts_id).click() #выбирается удаляемый контакт
        #wd.find_element_by_css_selector("input[value='Remove from'%s']" % groups_id).click()
        wd.find_element_by_name("remove").click() # нажимается кнопка удаления контакта
        self.open_contact_page()


