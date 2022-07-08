"""
Created on 6/9/22

@author: qinyuzhu
"""

import pandas as pd
from datetime import datetime, timedelta

def type_conversion():
     """Function that do data type conversion for time features
    Parameters
    ----------
    column name of the time feature in the file as the parameter of the funtion named type_conversion
    
    Returns
    -------
    a new csv file with one new column of the converted start time
    
    Raises
    ------
    Exception
        raise exception when the initial time (ini_time) is not set or the format of initial time is not '%b %d %Y %I:%M%p'
        raise exception when the output csv file name is not written
    """
    df = pd.read_csv("")


    lst = []
    for date in df:
        new = datetime.strptime(date, '')
    df["new_date"] = datetime.strftime()

    ini_time =  ""
    ini_time_for_now = datetime.strptime(ini_time, '%b %d %Y %I:%M%p')
    
    lst=[]
    new_final_time = ini_time_for_now + timedelta(days=1)
    difference = new_final_time - ini_time_for_now
    lst.append(difference)
    
    lst.to_csv("")






if __name__ == '__main__':
    pass
