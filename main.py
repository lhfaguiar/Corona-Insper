import pandas as pd
import sklearn

def main():
    df = pd.read_csv('train.csv', sep=',')
    
    countries = df['Country_Region'].unique()
    
    for country in countries:
        print(country)
        country_df = df[df['Country_Region'] == country]
        
        
        print(country_df)
    
main()