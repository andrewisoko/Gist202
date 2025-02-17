from seleniumbase import Driver
import pickle
import time
import random
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random



random_time_long = random.randrange(5,11)
random_time_short = random.randrange(3,5)


driver = Driver(uc=True)
url = "https://indeed.com//"

# Navigate to the page
driver.get(url)



# try: 
#     time.sleep(random_time_short)
#     driver.uc_gui_click_captcha()
# except:
#     print("not worked initial")
#     pass
    
    
    # Load cookies
with open("save-cookies.pkl", "rb") as file:
    cookies = pickle.load(file)

    # Print cookies to verify their content
    # print("Cookies to be added:", cookies)

    # Add cookies
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Error adding cookie: {cookie}")
            print(f"Error message: {str(e)}")

# Verify added cookies
added_cookies = driver.get_cookies()
# print("Cookies after adding:", added_cookies)

try:
    time.sleep(random_time_short)
    x_randomBtn = driver.find_element(By.CSS_SELECTOR, "button.css-yi9ndv.e8ju0x51")
    driver.execute_script("arguments[0].click();", x_randomBtn)
except:
    pass

# Refresh the page
driver.refresh()

    
# ============#
#             #
# automation  #
# section     #
#             #
# ============#




# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

jobname_options_list = [
    "Barista",
    # "Football manager",
    "Solicitor",
    "Cleaner",
]

location_options_list = [
    # "Sheffield",
    "Manchester",
    # "Salford",
]

# time.sleep(random_time_long)

try: 
    time.sleep(random_time_short)
    driver.uc_gui_click_captcha()
    
    time.sleep(random_time_short)
    Return_home_page = driver.find_element(
    By.XPATH, "/html/body/div[2]/main/div/button"
)
    Return_home_page.click()

      
except:
    print("not worked secondary")
    pass

input("Press Enter to close the browser...")
    
where = driver.find_element(
    By.CSS_SELECTOR,
    "#text-input-where",
)
where.send_keys(random.choice(location_options_list))

time.sleep(10)
what = driver.find_element(
    By.CSS_SELECTOR,
    "#text-input-what",
)

time.sleep(random_time_long)


what.send_keys(random.choice(jobname_options_list))



# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#


search_jobs = driver.find_element(
    By.CSS_SELECTOR, "button.yosegi-InlineWhatWhere-primaryButton"
)
time.sleep(random_time_long)
search_jobs.click()

try: 
    time.sleep(10)
    driver.uc_gui_click_captcha()
except:
    pass

try:
    time.sleep(random_time_short)
    x_randomBtn = driver.find_element(By.CSS_SELECTOR, "button.css-yi9ndv.e8ju0x51")
    driver.execute_script("arguments[0].click();", x_randomBtn)
except:
    pass


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

# last_24_hours = driver.find_element(
#     By.CSS_SELECTOR, "a.yosegi-FilterPill-dropdownListItemLink"
# )
# time.sleep(random_time)
# driver.execute_script("arguments[0].click();", last_24_hours)


# ============#
#             #
#   job       #
# selection   #
#             #
# ============#


loop_duration_time = timedelta(minutes=15)

title_spec_name = ""
location_spec_name = ""

what = driver.find_element(By.CSS_SELECTOR, "#text-input-what")
where = driver.find_element(By.CSS_SELECTOR, "#text-input-where")

what_value = what.get_attribute("value")
where_value = where.get_attribute("value")

if what_value == "Customer Service":
    title_spec_name = random.choice(["Customer Service"])
elif what_value == "It Support":
    title_spec_name = random.choice(
        [
            "First Line",
            "IT Support",
            "1st Line",
        ]
    )
elif what_value == "Helpdesk":
    title_spec_name = random.choice(["First Line", "Helpdesk"])
elif what_value == "Recruitment Consultant":
    title_spec_name = "Recruitment Consultant"

elif what_value == "Administrator":
    title_spec_name = "Administrator"

if where_value == "Manchester":
    # location_spec_name = random.choice(["Manchester","Altrincham","Warrington","Salford","Macclesfield","Chorley"])
    location_spec_name = random.choice(["Manchester",])
elif where_value == "Manchester City Centre":
    location_spec_name = random.choice(["Manchester", "Salford"])
elif where_value == "Salford Quays":
    location_spec_name = random.choice(["Manchester","Stockport", "Salford"])

print(
    f"this is the random values for job and location {title_spec_name},{location_spec_name}"
)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#


time.sleep(10)

    # slider_contanier = driver.find_elements(
    #     By.CSS_SELECTOR, "div.slider_container.css-12igfu2.eu4oa1w0"
    # )
slider_contanier = driver.find_elements(
    By.CSS_SELECTOR, "div.slider_container.css-nqpl5t.eu4oa1w0"
)

# input("Timeout..")

for item in slider_contanier:

    print(f"this is the tot amount of jobs today {len(slider_contanier)}")

    company_name = item.find_element(
        By.CSS_SELECTOR, 'span[data-testid="company-name"]'
    ).text

    time.sleep(random_time_long)
    driver.execute_script("arguments[0].scrollIntoView(true);", item)
    job_title = item.find_element(By.CSS_SELECTOR, '[id^="jobTitle-"]').text

    job_location = item.find_element(
        By.CSS_SELECTOR, 'div[data-testid="text-location"]'
    ).text

    try:
        job_salary = item.find_element(
            By.CSS_SELECTOR, "div.metadata.salary-snippet-container.css-5zy3wz.eu4oa1w0"
        ).text
    except Exception as exc:
        job_salary = "no salary"

    print(f" JW:{what_value} , LW: {where_value}")
    print(f"// job title and location TEXT: {job_title},{job_location}")

    # company_name_text = company_name.text
    # job_title_text = job_title.text
    # job_location_text = job_location.text
     
    try:
        time.sleep(random_time_short)
        x_randomBtn = driver.find_element(By.CSS_SELECTOR, "button.css-yi9ndv.e8ju0x51")
        driver.execute_script("arguments[0].click();", x_randomBtn)
    except:
        pass

    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    # if title_spec_name in job_title and location_spec_name in job_location:
    if (
        title_spec_name in job_title
        and location_spec_name in job_location
        and "Graduate" not in job_title
        and "Promotions" not in job_title
    ):

        print(
            f"company name : {company_name}"
            f" title of the job: {job_title}"
            f"job location : {job_location}"
            f" salary : {job_salary}"
        )

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        time.sleep(random_time_long)

        new_item = item.find_element(By.CSS_SELECTOR, 'div[data-testid="slider_item"]')

        new_item.click()

        print("item clicked")

        time.sleep(random.randint(10, 13))
        
        try:
            
            cookies_temp = driver.get_cookies()

            # Save cookies to a file
            with open("save-cookies_temp.pkl", "wb") as file_temp:
                pickle.dump(cookies_temp, file_temp)
            
        except:
            pass
        
        # input("Press Enter to close the browser...")
        
        
        try:
            
            # time.sleep(random_time_long)
            # apply_now = item.find_element(
            #     By.ID,
            #     "indeedApplyButton",
            # )
            
            apply_now = WebDriverWait(item, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@class = 'css-km0m34 e8ju0x50']"))
             )


            time.sleep(random_time_short)
            driver.execute_script("arguments[0].click();", apply_now)

            print("apply now clicked")
            
            

      
        except:

            try:
                
                apply_now = WebDriverWait(item, 10).until(
                EC.element_to_be_clickable((By.XPATH,"//button[@class = 'css-ayhgja e8ju0x50']"))
                )
        
                time.sleep(random_time_short)
                driver.execute_script("arguments[0].click();", apply_now)

                print("apply now second options clicked")

            except:

                print("apply button not found")
                
       
     
     

     

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        time.sleep(10)
        
        

        window_handles = driver.window_handles

        # driver.switch_to.window(window_handles[1])
        # print("Switched to new tab: " + driver.current_url)
        

        # input("Press Enter to close the browser...")
        
        # try:  
        #  time.sleep(random_time_short)
        #  driver.switch_to.window(window_handles[1])
        #  print("switching occured")
        # except:
        #     print("no need to be switching")
        
        
   
    
        # try:

        #     time.sleep(random_time_long)
        #     CVpdf = element = driver.find_element(By.CSS_SELECTOR, "input[data-testid='FileResumeCard-input']")
        #     print("CV element found")
        #     time.sleep(random_time_short)
        #     driver.execute_script("arguments[0].click();", CVpdf)

        # except:
            
#/////////////////////////////////////CHANGE AFTER TEST ////////////////////////////////////////////////           
            
        buttons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        ((By.CSS_SELECTOR, "button.e8ju0x50"))
                    )
                )
        print(f"this is the tot buttons:{len(buttons)}")
            
        for single_butt in buttons:
            try:
                    span_button =  WebDriverWait(single_butt, 10).until(
                    EC.presence_of_all_elements_located(
                        ((By.XPATH, "//span[text()='Continue']"))
                    )
                )
                    print("EXPERIMENT WORKED")
                    print(f"this is the tot buttons:{len(span_button)}")
            except:
                print("EXPERIMENT NOT WORKED")
        

#/////////////////////////////////////CHANGE AFTER TEST /////////////////////////////////////////////////           

            # driver.close()

            time.sleep(10)

            driver.switch_to.window(window_handles[0])
            
            try:
                time.sleep(random_time_short)
                x_randomBtn = driver.find_element(By.CSS_SELECTOR, "button.css-yi9ndv.e8ju0x51")
                driver.execute_script("arguments[0].click();", x_randomBtn)
            except:
                pass

            time.sleep(random_time_long)

            three_dots_btn = item.find_element(
                By.CSS_SELECTOR,
                "td.css-llg4dc.eu4oa1w0",
            )

            three_dots_btn.click()

            try:

                reach_portal = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div[data-reach-popover]")
                    )
                )

                print("reach portal appeared")

            except:

                print("reach portal naahhh appeared")

                time.sleep(random_time_long)

                try:

                    save_job = item.find_element(
                        By.XPATH,
                        '//div[@data-valuetext="Save job"]',
                    )

                    time.sleep(random_time_long)

                    # driver.execute_script("arguments[0].click();", save_job)

                    save_job.click()

                    print("saved job clicked")

                except:

                    print("save button not clicked")

                    # driver.close()

        
     # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
        
        try: 
            time.sleep(10)
            driver.uc_gui_click_captcha()
        except:
            pass
        
        

    
        pre_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-u74ql7.eu4oa1w0"))
        )
        
        
 
        buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    ((By.CSS_SELECTOR, "button.e8ju0x50"))
                )
            )
        
        print(f"this is the tot buttons:{len(buttons)}")
        
        try:
    
            span_element = buttons.find_element(By.XPATH, "//span[text()='Continue']")
            print("EXPERIMENT WORKED")
        
        except:
            print("EXPERIMENT NOT WORKED")

        
            
        
            
            # filtered_buttons = [btn for btn in buttons if btn.find_element(By.CSS_SELECTOR, "span").text.strip() == "Continue"]
            
            # print(f"here is the button: {buttons}")
                
            # # print("pre button found")
            
            # input("Press Enter to close the browser...")
        

    

        
        
        try: 
            time.sleep(10)
            driver.uc_gui_click_captcha()
        except:
            pass

        try:

            submit_app = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "button.css-1vqpayy.e8ju0x50",
                    )
                )
            )
            submit_app.click()

            # driver.close()
        except:
            print("submit button not yet")

            time.sleep(random.randint(10, 13))
            continue_btn2 = driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/main/div[3]/div/button",
            )

            time.sleep(random_time_long)
            continue_btn2.click()

            try:

                time.sleep(random_time_long)

                submit_app = driver.find_element(
                    By.CSS_SELECTOR,
                    "button.css-1vqpayy.e8ju0x50",
                )

                submit_app.click()

            except:

                # driver.close()

                time.sleep(10)

                driver.switch_to.window(window_handles[0])
                
                try: 
                    time.sleep(10)
                    driver.uc_gui_click_captcha()
                except:
                    pass
                
                try:
                    time.sleep(random_time_short)
                    x_randomBtn = driver.find_element(By.CSS_SELECTOR, "button.css-yi9ndv.e8ju0x51")
                    driver.execute_script("arguments[0].click();", x_randomBtn)
                except:
                    pass

                time.sleep(random_time_long)

                three_dots_btn = item.find_element(
                    By.CSS_SELECTOR,
                    "td.css-llg4dc.eu4oa1w0",
                )

                three_dots_btn.click()

                try:

                    reach_portal = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "div[data-reach-popover]")
                        )
                    )

                    print("reach portal appeared")

                except:

                    print("reach portal naahhh appeared")

                    time.sleep(10)

                    try:

                        save_job = item.find_element(
                            By.XPATH,
                            '//div[@data-valuetext="Save job"]',
                        )

                        time.sleep(random_time_long)

                        # driver.execute_script("arguments[0].click();", save_job)

                        save_job.click()

                        print("saved job clicked")

                    except:

                        print("save button not clicked")

                        # driver.close()


    # # Check if you're logged in or if the cookies had the desired effect
    # # You might need to check for a specific element that indicates you're logged in
    # try:
    #     logged_in_element = driver.find_element("css selector", "selector_for_logged_in_element")
    #     print("Successfully logged in!")
    # except:
    #     print("Not logged in or element not found.")

    # # Keep the browser open

# except:
#     print("cloudlflare layer")
#     driver.uc_gui_click_captcha()
    
input("Press Enter to close the browser...")