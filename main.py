from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium_recaptcha.components import find_until_clicklable, find_until_located
from time import sleep
from acc import acc


d = print


def print(*a, **kw):
    kw["flush"] = True
    return d(*a, **kw)


def do_jobs(cookie):
    def intercepter(request):
        if request.url.__contains__("aviso.bz"):
            request.headers["Cookie"] = cookie

    print("Openning Browser")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("prefs", {
    "translate_whitelists": {"ru":"en"},
    "translate":{"enabled":"true"}
    })
    driver = webdriver.Chrome(options=options)
    driver.request_interceptor = intercepter
    driver.maximize_window()
    
    print("Starting Web Serfing Jobs")
    driver.get("https://aviso.bz/work-serf")
    driver.execute_script("[...document.querySelectorAll('.work-serf')].forEach(function(item){item.style.display='table'})")
    all_work_serf = driver.find_elements(By.CSS_SELECTOR, ".work-serf")
    print(f"Found {len(all_work_serf)} Web Surfing Jobs")
    for work_serf in all_work_serf:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", work_serf)
            sleep(1)
            time_to_stay = int(work_serf.find_element(By.CSS_SELECTOR, 'div[style="margin-top:5px;"] .serf-text').text.split(" ")[0])
            cost_to_visit = float(work_serf.find_element(By.CSS_SELECTOR, 'span[title="Стоимость просмотра"]').text.split(" ")[0].split("o")[0])
            print(f"Doing Job... [Time: {time_to_stay} sec | Cost: {cost_to_visit} rub]")
            find_until_clicklable(work_serf, By.CSS_SELECTOR, "a").click()
            find_until_clicklable(work_serf, By.CSS_SELECTOR, "a.start-yes-serf").click()
            sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            driver.switch_to.frame(driver.find_element(By.NAME, "frminfo"))
            find_until_clicklable(driver, By.CSS_SELECTOR, ".btn_capt", time_to_stay + 30).click()
            driver.switch_to.default_content()
            for i, tabs in enumerate(driver.window_handles):
                if i != 0:
                    driver.switch_to.window(driver.window_handles[i])
                    driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            import traceback
            print(traceback.format_exc())
            print("Skipping This Job...")
    '''
    print("Starting Youtube Watching Jobs")
    driver.get("https://aviso.bz/work-youtube")
    driver.execute_script("[...document.querySelectorAll('.work-serf')].forEach(function(item){item.style.display='table'})")
    all_work_serf = driver.find_elements(By.CSS_SELECTOR, ".work-serf")
    print(f"Found {len(all_work_serf)} Youtube Jobs")
    for work_serf in all_work_serf:
        driver.execute_script("arguments[0].scrollIntoView();", work_serf)
        sleep(1)
        time_to_stay = int(work_serf.find_element(By.CSS_SELECTOR, 'div[style="margin-top:5px;"] .serf-text').text.split(" ")[0])
        cost_to_visit = float(work_serf.find_element(By.CSS_SELECTOR, 'span[title="Стоимость просмотра"]').text.split(" ")[0].split("o")[0])
        print(f"Doing Job... [Time: {time_to_stay} sec | Cost: {cost_to_visit} rub]")
        find_until_clicklable(work_serf, By.CSS_SELECTOR, "span").click()
        find_until_clicklable(work_serf, By.CSS_SELECTOR, "span.go-link-youtube").click()
        sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.switch_to.frame(driver.find_element(By.ID, "video-start"))
        find_until_clicklable(driver, By.CSS_SELECTOR, 'button[aria-label="Play"]').click()
        sleep(50)
        driver.switch_to.default_content()
        break
        '''

    sleep(10)
    driver.close()

for ck in acc:
    print("Doing Jobs On a Account")
    do_jobs(ck)

print("All Done")