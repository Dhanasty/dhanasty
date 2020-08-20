class finale():
    def netweb(self):
        usernames = []
        passwords = []
        
        import re
        path = "C:\\Users\\wrecker\\Documents\\netflix.txt"
        
        with open(path) as f:
            texts = f.read()  
        username=re.findall(r'Username-\S+.com',texts)   
        for user in username:
            usernames.append(user[9:])   
        password =re.findall(r'Password-\S+',texts)   
        for pas in password:
            passwords.append(pas[9:])
        
        up = dict(zip(usernames, passwords)) 

        print(up)
        from selenium import webdriver
        import time
        driver = webdriver.Chrome("c:\\Users\\wrecker\\Documents\\chromedriver_win32\\chromedriver.exe")
        
        for user,ppas in up.items():
            driver.get("https://www.netflix.com/in/login")
            assert "Netflix" in driver.title
            username = driver.find_element_by_id("id_userLoginId")
            username.clear()
            username.send_keys(user)
            
            password = driver.find_element_by_id("id_password")
            password.clear()
            password.send_keys(ppas)
            time.sleep(2)
            driver.find_element_by_class_name("login-button").click()
            time.sleep(2)
                   

finale.netweb()
