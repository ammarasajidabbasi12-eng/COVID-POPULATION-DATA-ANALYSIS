import pandas as pd 
from loader import *
from analysis import *
from visualization import *
import os
def main():
    base_dir=os.path.dirname(__file__)
    country_path=os.path.join(base_dir,'..','data','country_info.csv')
    covid_path=os.path.join(base_dir,'..','data','covid_cases.csv')
    population_path=os.path.join(base_dir,'..','data','population.csv')
    df_covid,df_country,df_population=load_data(covid_path,country_path,population_path)
    covid_df,country_df,population_df=clean_data(df_covid,df_country,df_population)
    df=merge_data(covid_df,country_df,population_df)
    print(df)
    print(df.shape)
    print(df.columns)
    print(df.index)
    print(total_covid_cases(df))
    print(total_cases_by_date(df))
    print(total_death(df))
    total_death_by_month(df)
    total_death_per_continent(df)
    total_recovery_per_continent(df)
    death_to_case_ratio_by_country(df)
    recovery_case_ratio_per_country(df)
    deaths_ratio_using_income_group(df)
    recovery_ratio_using_income_group(df)
    summary_metrics(df)
    calculate_correlation(df)
    fig,axes=(plt
    .subplots(
        3,
        2,
        figsize=(22,18)
        )
    )
    fig.suptitle(
        "COVID-19 Global Analysis Dashboard",
        fontsize=18,
        fontweight='bold'
    )
    plot_covid_trends(df,axes[0,0])
    plot_deaths_by_month(df,axes[0,1])
    plot_income_variation(df,axes[1,0])
    plot_income_group_ratios(df,axes[1,1])
    plot_correlation(df,axes[2,0])
    plot_summary_metrix(df,axes[2,1])
    fig.subplots_adjust(
        hspace=0.5,
        wspace=0.3
    ) 
    plt.savefig("data/output/dashboard.png", dpi=300, bbox_inches='tight')
    plt.show()
if __name__ == "__main__":
    main()