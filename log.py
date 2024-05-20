import logging

# Створення логгерів для модулів `baseloader` та `coinbaseloader`
baseloader_logger = logging.getLogger('baseloader')
coinbaseloader_logger = logging.getLogger('coinbaseloader')

# Встановлення рівня логування за замовчуванням
baseloader_logger.setLevel(logging.INFO)
coinbaseloader_logger.setLevel(logging.INFO)

# Налаштування логування за замовчуванням
logging.basicConfig(
    level=logging.DEBUG,  # Рівень логування для всіх логгерів
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Формат лог-повідомлень
    filename="my_log.log",  # Файл для запису логів
    filemode="w",  # Режим відкриття файлу (w - перезапис)
)

# Створення власного форматера логування
class MyFormatter(logging.Formatter):
    def format(self, record):
        # Формування лог-повідомлення
        message = f"{record.asctime} - {record.name} - {record.levelname.upper()} - {record.message}"
        return message

# Створення логгера з власним форматером
my_logger = logging.getLogger()
if my_logger.handlers:
    my_logger.handlers[0].setFormatter(MyFormatter())

# Створення хендлера для запису логів у файл
file_handler = logging.FileHandler("my_log.log")

# Додавання хендлера до логгерів
file_handler.setFormatter(MyFormatter())
baseloader_logger.addHandler(file_handler)
coinbaseloader_logger.addHandler(file_handler)

# Додавання логування до коду
baseloader_logger.info("Початок завантаження даних")
coinbaseloader_logger.error("Помилка при завантаженні даних: {error_message}")

# Експерименти з налаштуваннями рівня логування
baseloader_logger.setLevel(logging.DEBUG)
coinbaseloader_logger.setLevel(logging.WARNING)
