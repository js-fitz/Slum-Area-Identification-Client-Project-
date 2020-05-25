#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from currency_converter import CurrencyConverter

# read in rent index from https://www.numbeo.com/cost-of-living/rankings.jsp
rent_index = pd.read_csv('../classifying/city_rent_index.csv')
# updated 2/20/2020
rent_index.dropna(inplace=True)



def RentIndexAdjust(prices, # np array 
                    city, # str
                    original_currency, # eg INR
                    target_currency='USD', # eg USD
                    log_transform=False
                   ):
        
    # apply city rent index factor
    index_type = 'Rent Index'
    city_factor = 100/rent_index[rent_index['City']==city][index_type].values[0]
    
    
    prices = city_factor*prices


    # convert to USD
    cc = CurrencyConverter()
    def ConvertCurrency(x):
        try: return round(cc.convert(x, original_currency, target_currency))
        except: return np.nan
    
    
    prices = prices.apply(ConvertCurrency)

    
    # log transform
    if log_transform==True:
        prices = prices.apply(np.log)
        
    return prices

