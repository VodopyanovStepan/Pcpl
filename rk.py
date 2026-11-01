class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Browser:
    def __init__(self, id, name, size, computer_id):
        self.id = id
        self.name = name
        self.size = size          
        self.computer_id = computer_id   


class Installation:
    def __init__(self, browser_id, computer_id):
        self.browser_id = browser_id
        self.computer_id = computer_id   



computers = [
    Computer(1, "Компьютер учебный"),
    Computer(2, "Компьютер рабочий"),
    Computer(3, "Ноутбук"),
]

browsers = [
    Browser(1, "Архиватор", 120, 1),
    Browser(2, "Браузер", 350, 1),
    Browser(3, "Антивирус", 800, 2),
    Browser(4, "Редактор", 250, 2),
    Browser(5, "Плеер", 180, 3),
]

installations = [
    Installation(1, 1),
    Installation(1, 2),
    Installation(2, 1),
    Installation(3, 2),
    Installation(3, 3),
    Installation(5, 3),
]


def main():
    
    print("Запрос 1")
    for computer in computers:
        if "компьютер" in computer.name.lower():
            print(f"{computer.name}: ", end="")
            separator = ""
            for browser in browsers:
                if browser.computer_id == computer.id:
                    print(f"{separator}{browser.name}", end="")
                    separator = ", "
            print()
    print()

    print("Запрос 2")
    result = []
    for computer in computers:
        total_size = 0
        amount = 0
        for browser in browsers:
            if browser.computer_id == computer.id:
                total_size += browser.size
                amount += 1
        if amount > 0:                    
            average_size = round(total_size / amount, 2)
            result.append((computer.name, average_size))

    result.sort(key=lambda item: item[1])
    for name, average in result:
        print(f"{name}: {average:.2f} МБ")
    print()

   
    print("Запрос 3")
    for browser in browsers:
        if browser.name.lower().startswith("а"):
            print(f"{browser.name}: ", end="")
            separator = ""
            for installation in installations:
                if installation.browser_id == browser.id:
                    for computer in computers:
                        if computer.id == installation.computer_id:
                            print(f"{separator}{computer.name}", end="")
                            separator = ", "
            print()


if __name__ == "__main__":
    main()