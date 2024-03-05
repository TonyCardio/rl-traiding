from datetime import timedelta

from tinkoff.invest import Client, CandleInterval
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX
from tinkoff.invest.utils import now

from config import SANDBOX_TOKEN


class InvestClient:
    def __init__(self):
        self.token = SANDBOX_TOKEN
        self.target = INVEST_GRPC_API_SANDBOX

    def print_candles(self):
        with Client(token=self.token, target=self.target) as client:
            for candle in client.get_all_candles(
                instrument_id="BBG004730N88",
                from_=now() - timedelta(days=365),
                interval=CandleInterval.CANDLE_INTERVAL_HOUR,
            ):
                print(candle)
