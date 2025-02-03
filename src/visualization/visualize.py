import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(df):
    '''
    Plot the distribution of house prices
    '''
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='price', bins=50)
    plt.title('Distribution of House Prices')
    plt.xlabel('Price')
    plt.ylabel('Count')
    return plt

def plot_correlation_matrix(df):
    '''
    Plot correlation matrix of numeric features
    '''
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    return plt

if __name__ == "__main__":
    # Add your visualization testing code here
    pass
