"""
Copyright: Copyright (C) 2016 Baruch College - Systematic Trading
Description: Functions to get data from data sets
Author: Hongchao Pan, Yu Sun
"""

# Local imports

# Load packages
import pandas as pd
import numpy as np


# Define a function to read the data for Equation 4 in the paper
def df_eq4():
    '''
    Grasp the following data for equation 4: MKT, BOND, GSCI, SMB, HML, UMD
    '''
    MKT = pd.read_excel(io='../Data/MSCI_world.xlsx', sheetname=0, parse_cols='A:B', skiprows=4)
    BOND = pd.read_excel(io='../Data/BarclaysBondIndex.xlsx', sheetname=0, parse_cols='A:B', skiprows=4)
    GSCI = pd.read_excel(io='../Data/GSCI.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    SMBHML = pd.read_excel(io="../Data/F-F_Research_Data_Factors_daily.xlsx", sheetname=0, parse_cols='F:H',
                           skiprows=3)
    UMD = pd.read_excel(io='../Data/F-F_Momentum_Factor_daily.xlsx', sheetname=0, parse_cols='C:D', skiprows=11)

    # Merge the dateframes
    # Use dropna to drop all NaN elements when merge
    df = MKT.merge(BOND, on='Date', how='inner').dropna()
    df = df.merge(GSCI, on='Date', how='inner').dropna()
    df = df.merge(SMBHML, on='Date', how='inner').dropna()
    df = df.merge(UMD, on='Date', how='inner').dropna()

    return df

# Define a function to read all the bonds data
def df_bonds():
    '''
    Get the 2Y, 5Y, 10Y, 30Y bonds data
    :return: data frame contains all bonds data
    '''

    b2y=pd.read_excel(io='../Data/2ybond.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    b5y=pd.read_excel(io='../Data/5ybond.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    b10y = pd.read_excel(io='../Data/10ybond.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    b30y = pd.read_excel(io='../Data/30ybond.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)

    # Use dropna to drop all NaN elements when merge
    df=b2y.merge(b5y, on='Date', how='inner').dropna()
    df=df.merge(b10y, on='Date', how='inner').dropna()
    df=df.merge(b30y, on='Date', how='inner').dropna()

    return df

# Define a function to read currencies data
def df_currency():
    '''
    EUR/USD, JPY/USD, GBP/USD
    :return: data frame contains all data of selected currencies
    '''

    EU=pd.read_excel(io='../Data/EURUSD.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    JU=pd.read_excel(io='../Data/JPYUSDBOE.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    GU=pd.read_excel(io='../Data/GBPUSD.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)

    # Use dropna to drop all NaN elements when merge
    df=EU.merge(JU, on='Date', how='inner').dropna()
    df=df.merge(GU, on='Date', how='inner').dropna()

    return df

# Define a function to read equity data (S&P500)
def df_equity():
    '''
    S&P500, TOPIX(Japan), FTSE100(UK)
    :return: data frame contains equity data
    '''

    SP500=pd.read_excel(io='../Data/SP500.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    TOPIX=pd.read_excel(io='../Data/TOPIX.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    FTSE100=pd.read_excel(io='../Data/FTSE100.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)

    # Use dropna to drop all NaN elements when merge
    df=SP500.merge(TOPIX, on='Date', how='inner').dropna()
    df=df.merge(FTSE100, on='Date', how='inner').dropna()

    return df

# Define a function to read commodity data
def df_commodity():
    '''
    Cotton, Sugar, NATGAS, CRUDE, GOLD, SILVER
    :return: data frame contains commodity data
    '''

    cotton=pd.read_excel(io='../Data/cotton.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    sugar=pd.read_excel(io='../Data/sugar.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    natgas=pd.read_excel(io='../Data/natural_gas.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    crude=pd.read_excel(io='../Data/crude.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    gold=pd.read_excel(io='../Data/gold.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)
    silver=pd.read_excel(io='../Data/silver.xlsx', sheetname=0, parse_cols='A:B', skiprows=1)

    # Use dropna to drop all NaN elements when merge
    df=cotton.merge(sugar, on='Date', how='inner').dropna()
    df=df.merge(natgas, on='Date', how='inner').dropna()
    df=df.merge(crude, on='Date', how='inner').dropna()
    df=df.merge(gold, on='Date', how='inner').dropna()
    df=df.merge(silver, on='Date', how='inner').dropna()

    return df

# Define a function to combine all dataframes and separate the data to test_data and validation_data

def df_test_validation(Ts,Te, Vs,Ve):
    '''
    Test: 1998-2012
    Validation: 2009-2016
    :param Ts: Test start date with unit year
    :param Te: Test end date with unit year
    :param Vs: Validation start date with unit year
    :param Ve: Validation end date with unit year
    :return: test_data, validation_data
    '''

#    eq4=df_eq4()
#    bonds=df_bonds()
    equity=df_equity()
#    currency=df_currency()
#    commodity=df_commodity()

    # Use dropna to drop all NaN elements when merge
#    df=eq4.merge(bonds, on='Date', how='inner').dropna()
#    df=eq4.merge(equity,on='Date',how='inner').dropna()
#    df=df.merge(equity, on='Date', how='inner').dropna()
#    df=df.merge(currency, on='Date', how='inner').dropna()
#    df=df.merge(commodity, on='Date', how='inner').dropna()

    # Add a new column with converted the "Date" to datetime objects
    # for future slice
    df=equity # Speed up computation by using equity
    df['datetime']=[df.iloc[i,0].date() for i in range(len(df.iloc[:,0]))]

    # Get the index of test data
    ind_test=[Ts <= df.iloc[i]['datetime'].year <= Te for i in range(len(df.iloc[:, 0]))]
    # Get the index of validation data
    ind_validation=[Vs <= df.iloc[i]['datetime'].year <= Ve for i in range(len(df.iloc[:, 0]))]

    # Get the test data
    df_test=df[ind_test]
    # Get the validation data
    df_validation=df[ind_validation]

    return df_test, df_validation

# Define a function to read risk-free rates
def df_rf():
    '''

    :return: risk-free rates
    '''

    df=pd.read_excel(io='../Data/RiskFreeRate.xlsx', sheetname=0, parse_cols='A:F', skiprows=0)[['Date','rf']]
    # rf: is x.xx% not decimal format

    return df


# Define a function to compute the excess return
def excess_return():
    '''
    excess return = percentage return - risk free rate
    :return: excess return
    '''

    # Use pandas.pct_change to compute percentage of the test_data and validation_data
    # Test start/end year
    Ts = 1998
    Te = 2012
    # Validation start/end year
    Vs = 2013
    Ve = 2016
    # Let test df be validation df to avoid change notations
#    Ts=2010
#    Te=2016

    df_test, df_validation = df_test_validation(Ts, Te, Vs, Ve)

    # Change the 'datetime' and 'Date' to the index for pct_change()
    df_test.set_index(inplace=True, keys=['Date', 'datetime'])
    df_test = df_test.pct_change()[1:]
    df_test.reset_index(inplace=True)

    df_validation.set_index(inplace=True, keys=['Date', 'datetime'])
    df_validation = df_validation.pct_change()[1:]
    df_validation.reset_index(inplace=True)

    # Compute the excess return
    dfrf=df_rf()
    dfrf['rf']=dfrf['rf'].astype(float)
    dfrf['rf']=dfrf['rf']/100/261 # Convert to decimal format
    df_test=df_test.merge(dfrf, on='Date', how='inner').dropna()
    df_validation=df_validation.merge(dfrf,on='Date', how='inner').dropna()

    df_test_excess=df_test
    df_validation_excess=df_validation

    for i in range(2,(len(df_test_excess.columns)-1)):
        df_test_excess.iloc[:,i]=df_test_excess.iloc[:,i]-df_test.iloc[:,(len(df_test.columns)-1)]

    for i in range(2,(len(df_validation_excess.columns)-1)):
        df_validation_excess.iloc[:, i] = df_validation_excess.iloc[:, i] - \
                                          df_validation.iloc[:, (len(df_test.columns) - 1)]

    return df_test_excess, df_validation_excess

# Define a function to compute the annulized excess return
def excess_return_annu():
    # Get the excess return for test and validation data
    # Start/end date had been encoded in the Get_data.py file
    # Change it over there if you need
    df_excess_test, df_excess_validation = excess_return()
    # Annulized
    for j in range(2, (len(df_excess_test.columns) - 1)):
        df_excess_test.iloc[:, j] = df_excess_test.iloc[:, j]
        df_excess_validation.iloc[:, j] = df_excess_validation.iloc[:, j]
    # Drop 1st Date column
    df_excess_test = df_excess_test.drop('Date', axis=1)
    df_excess_validation = df_excess_validation.drop('Date', axis=1)

    return df_excess_test, df_excess_validation

# Define a function to compute annulized volatility
def vol_annu():

    # Get the annulized excess return
    df_excess_test, df_excess_validation = excess_return_annu()

    # ex ante volatility estimate in the paper (Eq 1 in the paper)
    delta = 60 / 61
    sLength = len(df_excess_test['datetime'])
    # Get the column names of excess return for future use
    colnames = df_excess_test.columns.values
    # C
    ind_vol = range(sLength)
    df_vol = pd.DataFrame(index=ind_vol, columns=colnames)
    df_vol = df_vol.fillna(0)
    df_vol['datetime'] = df_excess_test['datetime']

    # Compute the vol matrix of all derivatives
    for k in range(1, (len(df_vol.columns) - 1)):
        rbar_list = [0] * sLength
        for j in range(1, sLength - 299):
            for i in range(0, 300):
                rbar_list[sLength - j] = rbar_list[sLength - j] + df_excess_test[colnames[k]][sLength - j - i] * (
                1 - delta) * np.power(delta, i)
        df_excess_test['rbar'] = rbar_list

        vol_list = [0] * sLength
        for j in range(1, sLength - 299):
            for i in range(0, 300):
                vol_list[sLength - j] = vol_list[sLength - j] + np.power(
                    (df_excess_test[colnames[k]][sLength - j - 1 - i] - df_excess_test['rbar'][sLength - j - i]), 2) * (
                                                                1 - delta) * np.power(delta, i)
            vol_list[sLength - j] = np.sqrt(261 * vol_list[sLength - j])

        df_vol[colnames[k]] = vol_list


    return df_vol

if __name__ == "__main__":
    # Test data frame for equation 4
    #df1=df_eq4()
    #print(df1.iloc[0:10,:])

    # Test bonds data
    #df2=df_bonds()
    #print(df2.iloc[0:10,:])

    # Test currencies data
    #df3=df_currency()
    #print(df3.iloc[:10,:])

    # Test equity data
    #df4=df_equity()
    #print(df4.iloc[:10,:])

    # Test commodity data
    #df5 = df_commodity()
    #print(df5.iloc[:10, :])

    # Test whole combined datasets
    #Ts=1998
    #Te=2012
    #Vs=2013
    #Ve=2016
    #df_test, df_validation=df_test_validation(Ts, Te, Vs, Ve)
    #print(df_test.iloc[-10:,:])
    #print(df_validation.iloc[-10:, :])

    # Test risk free rate
    #df6=df_rf()
    #print(df6.head())

    # Test the excess return
    # Test excess return
    #print("Test excess return")
    #df_excess_test, df_excess_validation = excess_return()
    #print(df_excess_test.head())

    # Test the annulized excess return
    # Test excess return
    print("Test annulized excess return")
    df_excess_test, df_excess_validation = excess_return_annu()
    print(df_excess_test.head())