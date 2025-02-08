

def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL для проверки"
    )
    parser.addoption(
        "--status_code", action="store", default=200, type=int, help="Ожидаемый статус-код"
    )