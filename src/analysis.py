import pandas as pd
import numpy as np
def total_covid_cases(df):
    return df['confirmed'].sum()
def total_cases_by_date(df):
    return df.groupby('date')['confirmed'].sum().reset_index()
def avg_case_by_country(df):
    return df.groupby('country')['confirmed'].mean().reset_index()
def total_death(df):
    return df['deaths'].sum()
def total_death_by_month(df):
    return df.groupby('month')['deaths'].sum().reset_index()
def death_to_case_ratio_by_country(df):
    grouped=df.groupby('country')[['confirmed','deaths']].sum()
    grouped['death_ratio']=(grouped['deaths']/grouped['confirmed']) *100
    return grouped['death_ratio'].reset_index()
def total_recovery(df):
    return df['recovered'].sum()
def recovery_case_ratio_per_country(df):
    grouped=df.groupby('country')[['recovered','confirmed']].sum()
    grouped['recovery_ratio']=(grouped['recovered']/grouped['confirmed'])*100
    return grouped['recovery_ratio'].reset_index()
def avg_recovery_per_month(df):
    return df.groupby('month')['recovered'].mean().reset_index()
def total_death_per_continent(df):
    return df.groupby('continent')['deaths'].sum().reset_index()
def total_recovery_per_continent(df):
    return df.groupby('continent')['recovered'].sum().reset_index()
def deaths_ratio_using_income_group(df):
    total_deaths=df.groupby('income_group')['deaths'].sum()
    total_cases=df.groupby('income_group')['confirmed'].sum()
    death_ratio=(total_deaths/total_cases)*100
    death_ratio=(
        death_ratio
        .reset_index(name='death_ratio')
    )
    return death_ratio
def recovery_ratio_using_income_group(df):
    total_recovered=df.groupby('income_group')['recovered'].sum()
    total_cases=df.groupby('income_group')['confirmed'].sum()
    recovery_ratio=(total_recovered/total_cases)*100
    recovery_ratio=(
        recovery_ratio
        .reset_index(name='recovery_ratio')
    )
    return recovery_ratio
def summary_metrics(df):

    cases = df.groupby('country')['confirmed'].sum()
    deaths = df.groupby('country')['deaths'].sum()

    result = pd.DataFrame({
        'highest_cases_country': [cases.idxmax()],
        'highest_cases_value': [cases.max()],

        'highest_deaths_country': [deaths.idxmax()],
        'highest_deaths_value': [deaths.max()],

        'lowest_deaths_country': [deaths.idxmin()],
        'lowest_deaths_value': [deaths.min()],
    })

    return result
def calculate_correlation(df):
    return df[['confirmed','deaths','recovered']].corr()
def income_group_and_continent_death_variation(df):
    std_income_group=(df.groupby('income_group')['deaths'].std().reset_index(name='deaths_std'))
    std_continents=(df.groupby('continent')['deaths'].std().reset_index(name='continents_std'))
    return std_income_group,std_continents