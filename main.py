from invest_client import InvestClient


def main():
    client = InvestClient()
    client.print_candles()


if __name__ == '__main__':
    main()
