#Automation of google form 
#reference link : https://youtu.be/B5X2nyA8RlU
from selenium import webdriver
import time 

#loop
x=1
while x>0:
    #asking for data that will change
    a = input('Enter your destination: ')
    b = input('State purpose: ')
    d1 = input('Date from[dd/mm/yyyy]: ')
    d2 = input('Date to[dd/mm/yyyy]: ')

    #condition for date
    if d1 < d2:
        #object for webdriver
        web = webdriver.Chrome()
        web.get('https://docs.google.com/forms/d/e/1FAIpQLScJXHILJqFFIyEoobKUw5t-JsfWz8HAE-PokFG10U5dc2Q9VQ/viewform?vc=0&c=0&w=1&flr=0')
        web.maximize_window()
        time.sleep(4)

        #name section
        my_name = 'Tshering Phuntsho'
        name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name.send_keys(my_name)
        time.sleep(1)

        #student number section
        student_no = '02230310'
        std_no = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        std_no.send_keys(student_no)
        time.sleep(1)

        #course section
        course = 'SWE'
        programe = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        programe.send_keys(course)
        time.sleep(1)

        #semester section
        semester = 'I'
        sem = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        sem.send_keys(semester)
        time.sleep(1)

        #section section
        section = 'null'
        sec = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        sec.send_keys(section)
        time.sleep(1)

        #SSO name section
        sso_name = 'Dawa Gyeltshen'
        sso = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        sso.send_keys(sso_name)
        time.sleep(1)

        #councilor name section
        councilor_name = 'Sangay Tashi'
        councilor = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
        councilor.send_keys(councilor_name)
        time.sleep(1)

        #hostel name section
        hostel_name = 'H11 B'
        hostel = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
        hostel.send_keys(hostel_name)
        time.sleep(1)

        #room number section
        room_no= 'B1'
        room = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
        room.send_keys(room_no)
        time.sleep(1)

        #contact section
        contact_no= '77277687'
        contact = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input')
        contact.send_keys(contact_no)
        time.sleep(1)

        #purpose of leave section
        purpose_of_leave = b
        purpose = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea')
        purpose.send_keys(purpose_of_leave)

        #destination section
        distination = a
        distiny = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
        distiny.send_keys(distination)
        time.sleep(2)

        #date 'from' section
        date1 = d1
        From = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input')
        From.send_keys(date1)
        time.sleep(2)

        #date 'to' section
        date2 = d2
        to = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input')
        to.send_keys(date2)
        time.sleep(2)

        #guardian name section
        guardian_name= 'Leki Jamtsho'
        gname = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input')
        gname.send_keys(guardian_name)
        time.sleep(1)

        #relationship section
        relationship= 'Father'
        relation = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div/div[1]/input')
        relation.send_keys(relationship)
        time.sleep(1)

        #place section
        place = 'Panbang'
        p = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input')
        p.send_keys(place)
        time.sleep(1)

        #contact number of guardian
        phone_no = '17613773'
        phone = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div[1]/div/div[1]/input')
        phone.send_keys(phone_no)
        time.sleep(1)

        #submit
        submit = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()
        time.sleep(2)
    else:
        print('Invalid date. Your second date should be greater than first date')
        x+=1

        #the end



