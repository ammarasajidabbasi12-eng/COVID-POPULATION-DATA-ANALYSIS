import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from analysis import *
def plot_covid_trends(df,ax):
    grouped=(
        df
        .groupby('date')
        [['confirmed','deaths','recovered']]
        .sum()
    )
    #------------confirmed-------------
    ax.plot(
        grouped
        .index,
        grouped['confirmed'],
        marker='o',
        label='CONFIRMED CASES'
        )
    
    
    #-----------deaths----------------
    ax.plot(
        grouped
        .index,
        grouped['deaths'],
        marker='o',
        label='DEATHS'
        )
    
    #-----------recovered--------------
    ax.plot(
        grouped
        .index,
        grouped['recovered'],
        marker='o',
        label='RECOVERED'
        )
    ax.set_title("COVID TRENDS OVER TIME",fontsize=13)
    ax.set_ylabel("CASES",fontsize=10)
    ax.tick_params(axis='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
def plot_deaths_by_month(df,ax):
    total=total_death_by_month(df)
    total=total[total['deaths']>0]
    ax.bar(
        total['month'], 
        total['deaths']
        )
    ax.set_title("DEATH CASES BY MONTH",fontsize=13)
    ax.set_ylabel('DEATHS',fontsize=10)
    ax.tick_params(axis='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)
def plot_correlation(df,ax):
    corr=calculate_correlation(df)
    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        ax=ax,
        cbar_kws={'shrink': 0.7}

        )
    ax.set_title("correlation heatmap")
    ax.tick_params(axis='x', rotation=0)
    ax.tick_params(axis='y', rotation=0)
def plot_summary_metrix(df,ax):
    summary = summary_metrics(df)

    ax.axis('off')

    text = f"""
    Highest Cases Country : {summary['highest_cases_country'][0]}
    Highest Cases Value   : {summary['highest_cases_value'][0]}

    Highest Deaths Country: {summary['highest_deaths_country'][0]}
    Highest Deaths Value  : {summary['highest_deaths_value'][0]}

    Lowest Deaths Country : {summary['lowest_deaths_country'][0]}
    Lowest Deaths Value   : {summary['lowest_deaths_value'][0]}
    """

    ax.text(
    0.05,
    0.5,
    text,
    fontsize=11,
    va='center'
)

    ax.set_title("Summary Metrics")

def plot_income_group_ratios(df, ax):

    death_data = deaths_ratio_using_income_group(df)
    recovery_data = recovery_ratio_using_income_group(df)

    groups = death_data['income_group']

    x = np.arange(len(groups))  # positions for bars
    width = 0.35  # bar width

    # ---------------------------
    # Bars
    # ---------------------------
    ax.bar(x - width/2, death_data['death_ratio'], width, label='Death Ratio')
    ax.bar(x + width/2, recovery_data['recovery_ratio'], width, label='Recovery Ratio')

    # ---------------------------
    # Labels
    # ---------------------------
    ax.set_title("Death vs Recovery Ratio by Income Group",fontsize=13)
    ax.set_ylabel("Percentage (%)",fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(groups, rotation=30)
    ax.legend()
def plot_income_variation(df,ax):
    income_std,_=income_group_and_continent_death_variation(df)
    ax.bar(income_std['income_group'], income_std['deaths_std'])
    ax.set_title('DEATH VARIATION USING INCOME GROUP',fontsize=13)
    ax.set_ylabel('Standard Deviation',fontsize=10)
    ax.tick_params(axis='both', labelsize=9)
    ax.grid(True, linestyle='--', alpha=0.5)
