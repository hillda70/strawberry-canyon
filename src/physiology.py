"""
Strawberry Canyon — Volatility & Momentum Mechanics
Component: Fragility Ratio Core (30-Minute Interval Execution)
"""

import numpy as np
import pandas as pd


class MarketPhysiology:
    def __init__(self, roc_period: int = 13, atr_period: int = 14):
        self.roc_period = roc_period
        self.atr_period = atr_period

    def calculate_atrp(self, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
        """
        Calculates ATRP (Average True Range Percentage) over 14 periods.
        Normalizes the true range against close price to keep ratios stable across price regimes.
        """
        tr1 = high - low
        tr2 = (high - close.shift(1)).abs()
        tr3 = (low - close.shift(1)).abs()
        
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = true_range.rolling(window=self.atr_period).mean()
        
        atrp = (atr / close) * 100
        return atrp

    def calculate_fragility_ratio(self, close: pd.Series, atrp: pd.Series) -> pd.Series:
        """
        Fragility Ratio = ROC(13) / ATRP(14) on a 30-minute bar.
        Measures the efficiency of directional thrust per unit of normalized volatility.
        """
        roc = close.pct_change(periods=self.roc_period) * 100
        fragility_ratio = roc / atrp.replace(0, np.nan)
        return fragility_ratio


if __name__ == "__main__":
    np.random.seed(101)
    intervals = 40
    
    base_price = 420.0
    price_changes = np.random.normal(0.1, 0.4, intervals)
    closes = base_price + np.cumsum(price_changes)
    highs = closes + np.random.uniform(0.2, 0.8, intervals)
    lows = closes - np.random.uniform(0.2, 0.8, intervals)
    
    df_30m = pd.DataFrame({'high': highs, 'low': lows, 'close': closes})
    
    mp = MarketPhysiology()
    df_30m['ATRP_14'] = mp.calculate_atrp(df_30m['high'], df_30m['low'], df_30m['close'])
    df_30m['FRAGILITY_RATIO'] = mp.calculate_fragility_ratio(df_30m['close'], df_30m['ATRP_14'])
    
    print("--- 30-MINUTE INTERVAL FRAGILITY TAPE ---")
    print(df_30m[['close', 'ATRP_14', 'FRAGILITY_RATIO']].tail(8))
