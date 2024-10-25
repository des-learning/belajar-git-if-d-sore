class POS:
    def __init__(self):
        pass

    def title(self):
        return "POS Application"

    def run(self):
        print(self.title())
        while True:
            stop = input("Stop(y/n): ")
            if stop == "y":
                break


if __name__ == "__main__":
    pos = POS()
    pos.run()
