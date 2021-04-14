from services import QBO


def main():
    qbo = QBO()
    qbo.read("purchase", 742)


if __name__ == "__main__":
    main()
