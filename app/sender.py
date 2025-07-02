from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from cprint import cprint


cprint.info("START")
# настраиваем браузер
options = webdriver.ChromeOptions()  # можно поменять на любой браузер
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=profile')  # Укажите путь к папке с профилем
options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

# авторизуемся в вотсапе
url = "https://web.whatsapp.com/"
driver.get(url)
sleep(45)  # У вас будет 45 секунд для сканирования QR-кода

# создаем список номеров и текст сообщения
numbers = ["+79999999999"]  # Замените на ваши номера
text = "Привет+мир!"  # Текст сообщения

# проходим по каждому номеру и отправляем на него сообщение с заданным текстом
for number in numbers:
    url = f"https://web.whatsapp.com/send?phone={number}&text={text}"
    driver.get(url)
    try:
        send_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                '/html/body/div[1]/div/div/div[3]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]/button'
            ))
        )
        send_button.click()
        cprint.ok(f"Сообщение отправлено на {number}")
    except Exception as e:
        cprint.err(f"Не удалось отправить сообщение на {number}: {e}")
    sleep(5)  # Задержка между отправками, можно указать любое, но лучше (1<)

# завершаем работу
driver.quit()
cprint.info('END')
