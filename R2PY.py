from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd


def base_line_analysis(sub_id, date_of, st):
    
    # Inputs to Function:
    # ID of participant
    # Date of experiment (**Issue- would like to update so it pulls this from file)
    # Participant skin tone (**Issue- would like to update so it pulls this from file)

    # Outputs to Function:
    # .csv file with all timestamps for every participant in the study, which has all devices used in the study, skin tone, activity condition, and participant ID

    # Set filepath of folder with all subject data
    filepath = (Path('filepath') / sub_id).absolute()

    df = pd.read_csv('filepath\\skintonestudyTIMES.csv', header=True)
    time = df.loc[df['ï..Subject.ID'] == sub_id]
    f = lambda t: round(datetime.strptime('%m/%d/%Y %H:%M:%S', t).timestamp())
    for dst, src in (('R', 'Baseline'), ('A', 'Activity'), ('B', 'DB'), ('T', 'Type')):
        for i in range(1, 4):
            src_key, dst_key = f'{src}{i}', f'{dst}{i}'
            time[dst_key] = time[src_key].apply(f)

    date_num = datetime.strptime(f'%Y-%m_%d', date_of).timestamp()
    df_hr = pd.read_csv(filepath / 'HR.csv', header=False)
    df_hrt = pd.read_csv(filepath / 'HRT.csv', header=False)
    df_hrt = np.round_(df_hrt + date_num)
    df_ecg = pd.concat([df_hrt, df_hr], axis=1)
    df_ecg.rename(columns=dict(zip(df_ecg.columns, ('Time', 'ECG'))), inplace=True)

    df_e4: pd.DataFrame = pd.read_csv(filepath / 'Empatica/HR.csv', header=False)
    e4_start_time = df_e4.loc[:, 1]
    df_e4 = df_e4.loc[:, [-1, -2]]
    seconds_passed_e4 = df_e4.shape[0]
    e4_end_time = e4_start_time + seconds_passed_e4
    e4_time = [i for i in range(e4_start_time, e4_end_time)]
    df_e4 = pd.concat([e4_time, df_e4])
    df_e4.rename(columns=dict(zip(df_ecg.columns, ('Time', 'Empatica'))), inplace=True)

    df_aw = pd.read_csv(filepath / 'Apple Watch.csv', header=False)
    aw_start_time = df_aw.loc[1, 2]
    apple_hr = df_aw.loc[1:7, 2]
    apple_sec = df_aw.loc[1:7, 1] + aw_start_time
    df_apple_watch = pd.DataFrame([apple_sec, apple_hr], columns=['Time', 'AppleWatch'])

    df_fb = pd.read_csv(filepath / 'Fitbit.csv', header=False)
    fb_hr = df_fb.loc[-1, 2]
    fb_time = df_fb[-1, 1]
    df_fitbit = pd.DataFrame([fb_time, fb_hr], columns=["Time", "Fitbit"])

    if (filepath / 'garmin.tcx').exists():
        df_gm = pd.read_xml(filepath / 'garmin.tcx')
        df_ecg.rename(columns=dict(zip(df_gm.columns, ('Time', 'Garmin'))), inplace=True)
    else:
        df_gm = pd.DataFrame([], columns=['Time', 'Garmin'])

    if (filepath / 'Miband.xls').exists():
        df_miband = pd.read_xml(filepath / 'Miband.xls')
        df_miband.rename(columns=dict(zip(df_gm.columns, ('Time', 'Miband'))), inplace=True)
    else:
        df_miband = pd.DataFrame([], columns=['Time', 'Miband'])

    if (filepath / 'Biovotion\\BHR.csv').exists():
        df_biovotion = pd.read_xml(filepath / 'Biovotion\\BHR.csv')
        df_biovotion.rename(columns=dict(zip(df_gm.columns, ('Time', 'Biovotion'))), inplace=True)
    else:
        df_biovotion = pd.DataFrame([], columns=['Time', 'Biovotion'])

    df = pd.merge(df_ecg, df_apple_watch, on='Time')
    df = pd.merge(df, df_e4, on='Time')
    df = pd.merge(df, df_gm, on='Time')
    df = pd.merge(df, df_fitbit, on='Time')
    df = pd.merge(df, df_miband, on='Time')
    df = pd.merge(df, df_biovotion, on='Time')
    df['ID'] = sub_id
    df['ST'] = st
    df['Condition'] = ''

    for condition, count in (
            ('Activity', 300),
            ('Rest', 240),
            ('Breathe', 60),
            ('Type', 60),
    ):
        for i in range(1, 4):
            key = f'{condition[0]}{i}'
            df.loc[(df['Time'] > time[key]) & (df['Time'] < time[key] + count)] = condition
    df.to_csv('filename.csv', index=False, header=False)


if __name__ == '__main__':
    base_line_analysis('19-###', '2019-##-##', '#')
