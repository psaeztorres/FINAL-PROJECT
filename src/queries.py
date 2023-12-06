import pandas as pd
import requests
import json

def ree_query(start_date, end_date, ccaa_code,aacc_dicc):
    """
    Retrieve electricity generation data from Red Eléctrica de España (REE) API for a specific Autonomous Community (CCAA).

    Parameters:
    - start_date (str): The start date for the data query in the format 'YYYY-MM-DD'.
    - end_date (str): The end date for the data query in the format 'YYYY-MM-DD'.
    - ccaa_code (str): The code representing the Autonomous Community (CCAA) for which the data is requested.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing electricity generation data for the specified time range and Autonomous Community.
    
    Example:
    ```
    start_date = '2023-01-01'
    end_date = '2023-01-31'
    ccaa_code = '4'  # Example code for Andalusia
    data_frame = ree_query(start_date, end_date, ccaa_code)
    print(data_frame)
    ```
    """
    headers = {'Accept': 'application/json',
               'Content-Type': 'applic<ation/json',
               'Host': 'apidatos.ree.es'}
    url= f"https://apidatos.ree.es/es/datos/generacion/estructura-generacion?start_date={start_date}T00:00&end_date={end_date}T23:59&time_trunc=month&geo_trunc=electric_system&geo_limit=ccaa&geo_ids={ccaa_code}"    
    answer = requests.get(url, headers).json()
    res = answer['included']
    answer_list = []
    for i in res:

        fuente = i['attributes']['title']
        tipo = i['attributes']['type']
        fecha = pd.to_datetime(i['attributes']['values'][0]['datetime']).date()
        value = i['attributes']['values'][0]['value']
        percentage = i['attributes']['values'][0]['percentage']

        small_dict = {
        "class": fuente,
        "type": tipo,
        "date" : fecha,
        "value" : value,
        "percentage": percentage,
        "aacc":aacc_dicc[ccaa_code]}

        answer_list.append(small_dict)
        answer_list
        df=pd.DataFrame(answer_list)
    return df

def ree_yearly(years_list,aacc_dicc): 
    """
    Retrieve yearly electricity generation data for multiple years and Autonomous Communities (CCAA).

    Parameters:
    - years_list (list): A list of years for which the electricity generation data is requested.
    -aacc_dic : a dictionary containing autonomous commmunities codes and its names
    Returns:
    - pd.DataFrame: A pandas DataFrame containing aggregated electricity generation data for the specified years and Autonomous Communities.
    
    Example:
    ```
    years_list = [2021, 2022, 2023]
    aacc_dicc = {8742:'canarias', 
                8743:'baleares',
                8744:'ceuta'}
    yearly_data_frame = ree_yearly(years_list)
    print(yearly_data_frame)
    ```
    """
    years_df = []
    for i in years_list:
        lista_df=[]
        for community in aacc_dicc:
            ccaa_code = community
            df = ree_query(f"{i}-01-01", f"{i+1}-01-01", ccaa_code,aacc_dicc)
            lista_df.append(df)
        lista_df = pd.concat(lista_df, ignore_index=True) 
        years_df.append(lista_df)
    final_df = pd.concat(years_df, ignore_index=True) 
    return final_df