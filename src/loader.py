import pandas as pd
import os 
def load_data(covid_path,country_path,population_path):
    covid_df=pd.read_csv(covid_path,parse_dates=['date'])
    country_df=pd.read_csv(country_path)
    population_df=pd.read_csv(population_path)
    return covid_df,country_df,population_df
def clean_data(df_covid,df_country,df_population):
    df_covid=df_covid.copy()
    df_country=df_country.copy()
    df_population=df_population.copy()
    #_____________covid data cleaning_____________________
    df_covid=df_covid[df_covid['confirmed']!=0]
    df_covid['country']=(
        df_covid['country']
        .str.strip()
        .str.upper()
        )
    df_covid['month']=(
        df_covid['date']
        .dt.month_name()
    )
    month_order=["January","February","March","April","May","June",
    "July","August","September","October","November","December"]
    df_covid['month']=pd.Categorical(df_covid['month'],categories=month_order,ordered=True)
    df_covid=df_covid.sort_values('date')
    print(df_covid['country'].unique())

    #____________country data cleaning______________________
    df_country['country']=(
        df_country['country']
        .str.strip()
        .str.upper()
    )
    for c in ['continent','income_group']:
        df_country[c]=(
            df_country[c]
            .str.strip()
            .str.title()
        )
        print(df_country['country'].unique())

    #___________population data cleaning_____________________
    df_population['country']=df_population['country'].str.strip().str.upper()
    print(df_population['country'].unique())
    return df_covid,df_country,df_population
def merge_data(covid_df,country_df,population_df):
    merged_df=covid_df.merge(country_df,on='country',how='left')
    merged_df=merged_df.merge(population_df,on='country',how='left')
    print(merged_df.isnull().sum())
    return merged_df