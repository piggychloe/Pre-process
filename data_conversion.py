"""
Created on 6/9/22

@author: qinyuzhu
"""
import flirt
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv("test_conversion.csv")
print(df)

# the codes below is for further use of conversion
"""
# class conversion:
#
#     def __init__(self, data) -> None:
#         self.data = data
#     def convert_integer(self, data):
#         return int(self.data)
#     def convert_daytime(self, data):
#         delta = timedelta(microseconds=-1)
#         return delta
#     def convert_string(self,data):
#         return str()
#     def convert_list(self, data):
#         return list()
#     def convert_tuple(self, data):
#         return tuple()
#     def convert_set(self, data):
#         return set()
"""
lst = []
for date in df:
    new = datetime.strptime(date, '')
df["new_date"] = datetime.strftime()

ini_time =  "Jul 17 2019 11:49AM"
# print("initial_date", str(ini_time_for_now))

# ini_time_for_now = datetime.strptime(ini_time, '%b %d %Y %I:%M%p')
#
#
# lst=[]
# new_final_time = ini_time_for_now + timedelta(days=1)
# difference = new_final_time - ini_time_for_now
# lst.append(difference)
#
#
# df["converted_time"] = lst




if __name__ == '__main__':
    print(df)
