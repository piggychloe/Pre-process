# Pre-processing pipeline

The pre-processing pipeline generates a processed .CSV file for data from wearable devices.

Currently, the pipeline is capable of pre-processing raw data from the following devices/formats:
1. Time series data from ibeat [(Dynamic Time Warping algorithm to align Biomedical Signals of Non Uniform Sampling)](https://github.com/DigitalBiomarkerDiscoveryPipeline/Pre-process/tree/master/Signal-Alignment)
2. Apple Watch
3. Fitbit Watch
4. Garmin Watch
5. Miband
6. ECG data stored as a EDF file
7. Biovotion
8. Empatica
9. Data stored as a JSON file

### Collaborator Repositories: 
* FLIRT: a repository that assists with preprcessing data, see repository
    for instructions: 
    https://github.com/DigitalBiomarkerDiscoveryPipeline/flirt
    
    * FLIRT functions include: 
        * zip_file_path : Receive the path of the zip file containing the data to process
        * flirt.with_.empatica: reads and transforms the Empatica .zip file into features directly. 
        Calculates features for each time window (parameter window_length), and shifts each window 
        by the step size (parameter window_step_size)
        * flirt.reader.empatica.read_acc_file_into_df : reads the ACC sensor modality into a DataFrame
        * flirt.reader.empatica.read_ibi_file_into_df : reads the IBI sensor modality into a DataFrame
        * flirt.reader.empatica.read_eda_file_into_df : reads the EDA sensor modality into a DataFrame
        * flirt.reader.empatica.read_bvp_file_into_df : reads the BVP sensor modality into a DataFrame
        * flirt.reader.empatica.read_hr_file_into_df : reads the HR sensor modality into a DataFrame
        * flirt.reader.empatica.read_temp_file_into_df : reads a temporary file sensor modality into a DataFrame
        * flirt.get_hrv_features: reads and processes data to get HRV features from HRV DataFrame
        * flirt.get_acc_features: reads and processes data to get ACC features from ACC DataFrame
        * flirt.get_eda_features : reads and processes data to get EDA features from EDA DataFrame

* devicely: a python package for reading, de-identifying and writing data from 
    various health monitoring sensors. Designed to make reading, accessing, and 
    sharing sensor data more convenient while maintaining privacy. See 
    repository for instructions: 
    https://github.com/hpi-dhc/devicely
    
    * devicely getting started can be found here: 
        https://hpi-dhc.github.io/devicely/examples.html#
    * devicely can access and manipulate data for the following devices: 
        * Empatica E4
        * Spacelabs Blood Pressure Monitor
        * Bittium Faros
        * Biovotion Everion
        * Shimmer
        * Muse
        
        
### Steps to use the pipeline

#### <ins> Aligning Biomedical Signals </ins>

#### If you want to align biomedical signals of non-uniform sampling, please look into the ['Signal_Alignment'](https://github.com/DigitalBiomarkerDiscoveryPipeline/Pre-process/tree/master/Signal-Alignment) folder and follow the steps.


#### <ins> Data from watches </ins>

The pipeline requires the pandas, numpy, pytz, datetime, os, sys, json, rowingdata, mne, and re packages.

```
$ git clone https://github.com/DigitalBiomarkerDiscoveryPipeline/Pre-process.git
In your local machine go to :
$ cd /Pre-process/pipeline
Run `Complete - Browse file` file or 'Complete - User path`

```
#### If using the `Complete - Browse file` version of the code
1. The pipeline provides an option to browse the raw file in case of `Apple`, `Fitbit`, `Garmin`, `miband` and `ECG`. Please make sure to use these keywords when prompted to enter the `Type of watch`.

2. For `biovotion` and `empatica`, please provide the path to the folder where all the raw files are stored.

3. In case of `biovotion`, you will be prompted to enter the Device ID, you can find the same in the file name right after the vital sign name.
   For instance : If the filename is bop_1566404978515_BHR_5cda2e5e70116a01001eb098_1563897600_1563903059.csv, the Device ID is 5cda2e5e70116a01001eb098

4. The processed .csv file will be stored in the current working directory.

#### If using the `Complete - User path` version of the code
1. Please provide the path to the file / folder for the watch selected.

2. For `biovotion` and `empatica`, please provide the path to the folder where all the raw files are stored.

3. In case of `biovotion`, you will be prompted to enter the Device ID, you can find the same in the file name right after the vital sign name.
   For instance : If the filename is bop_1566404978515_BHR_5cda2e5e70116a01001eb098_1563897600_1563903059.csv, the Device ID is 5cda2e5e70116a01001eb098

4. The processed .csv file will be stored in the current working directory.

#### If you prefer using the terminal to run the code, please follow the following steps after you clone the repository:

```
jupyter nbconvert --to python Complete\ -\ Browse\ file.ipynb
```
or
```
jupyter nbconvert --to python Complete\ -\ User\ path.ipynb
```

Then run the file from terminal using:
```
python Complete\ -\ Browse\ file.py or python Complete\ -\ User\ path.py
```
#### <ins> Data stored as a JSON file </ins>

#### If you want to convert a JSON file to a dataframe, please look into the [json_table_convertor.ipynb](./json_table_convertor.ipynb)

1. In this notebook, two situations are discussed based on the sample data provided by the Open_mHealth: https://www.openmhealth.org/documentation/#/schema-docs/schema-library.

2. The convertor code may need to be adjusted based on the structure of the actual data.

### Functions

The pipeline currently uses the following functions.

| Plugin | README |
| ------ | ------ |
| preprocessed_output | main function that calls respective functions based on choice of watch|
| readcsv | calls pandas read_csv function with or without header |
| apple | function to process raw data from apple watch |
| fitbit | function to process raw data from fitbit watch |
| garmin | function to process raw data from garmin watch |
| miband | function to process raw data from miband watch |
| ecg | function to process raw ecg data stored as a .EDF file |
| biovotion | function to process raw data from biovotion watch |
| empatica | function to process raw data from empatica watch |
| process_df | Modifies column names and adds watch types |
| output | Stores output file with watch name  |
| get_filenames | Used by biovotion and empatica to obtain all .csv files in a folder  |
| preprocess_empatica | Pre-processing function for empatica, used to obtain values of vitals and frequency rate |
| add_time_empatica | Add time function for empatica, used to add time for each vital sign |
| import_json | Receive the path of json files and create a dataframe |
| [FLIRT](https://github.com/DigitalBiomarkerDiscoveryPipeline/flirt) | a repository that assists with preprcessing data for: Empatica E4 or Holter ECGs |
| [devicely](https://github.com/hpi-dhc/devicely) | a python package for reading, de-identifying and writing data from 
various health monitoring sensors |


##### apple functions:
    main : calls all other functions to process raw data
    dict_df : Creates a data dictionary with information like Workout_date, Duration, Calories burnt, Mean heart rate, Maximum heart rate, and Notes
    pre_process_apple : Creates a header for the apple dataframe
    add_time : Calculates actual time using start time and elapsed time information
    rename_cols : Renames column names of the dataframe
    output_dict : Outputs apple watch processed data as .csv and data dictionary as a .json file
##### fitbit functions:
    main : calls all other functions to process raw data
    add_time : Calculates elapsed time using actual time information
    rename_cols : Renames column names of the dataframe
##### garmin functions:
    main : calls all other functions to process raw data
    add_time : Obtains actual time by converting timestamp to UTC. Also calculates elapsed time using actual time information
    rename_cols : Renames column names of the dataframe

##### miband functions:
    main : calls all other functions to process raw data
    add_time : Calculates elapsed time using actual time information
    rename_cols : Renames column names of the dataframe

##### ecg functions:
    get_data : Processes .EDF file to obtain raw data in a .CSV file. It stores raw data as a .CSV file in the current working directory.
    main : calls all other functions to process raw data
    pre_process_ECG : Drop unnecessary data columns from raw data .CSV file
    add_time : Calculates elapsed and actual time using start time and sampling rate information
    rename_cols : Renames column names of the dataframe

##### biovotion functions:
    main : calls all other functions to process raw data
    extract_names : Extracts names of the vital signs being measured by the watch using .CSV filenames
    read_data : Reads all CSV files in the folder containing vital sign measurements. Processes column names.
    create_df_final : Creates one single dataframe
    add_time : Calculates actual time by converting timestamp to UTC time. Also calculates elapsed time.

##### empatica functions:
    read_data : Reads all .CSV files data stored in the folder and processes each file. It calculates time using sampling frequency and start time for each file.
    all_dfs : All dataframes are combined to create one single dataframe
    main : calls all other functions to process raw data

#### JSON to dataframe convertor functions:
    initial_sole_json : Receive the path of the first json file and use this json file to initialize the dataframe.
    import_new_sole_json : Receive the path of the following json file and append the new json file to the dataframe.
    import_mul_json : Receive the path of the json file with information of all patient.

### Continued Development

### Data type conversion functions:
    data_conversion: with funciton used to convert the time feature in the csv file


We are frequently updating this package with new devices and insights from the DBDP (Digital Biomarker Discovery Pipeline).
