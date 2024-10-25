class POS:
    def __init__(self):
        pass

    def title(self):
        return "POS Application"

    def run(self):
        print(self.title())
        while True:
            self.menu()
            stop = input("Stop(y/n): ")
            if stop == "y":
                break

    def menu(self):
        for i in ["menu1", "menu2", "menu3"]:
            print(i)


if __name__ == "__main__":
    pos = POS()
    pos.run()
