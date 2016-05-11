#graphic setting
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns


#Challenge 17
def Residual_histogram(movies_df):
    """
    This function draw a histogram of the residuals.
    """
    movies_clean_weekend_take_gross = movies_df.dropna(subset=['opening_weekend_take','domestic_gross'], how='any')
    #Make a dataframe called df with both the opening weekend take and the domestic gross columns and drop all rows with missing data
    df= movies_clean_weekend_take_gross.loc[:,['opening_weekend_take', 'domestic_gross']]
    #fit linear regression
    import statsmodels.api as sm

    Y = df.domestic_gross
    X = sm.add_constant(df.opening_weekend_take)

    linmodel = sm.OLS(Y,X).fit()
    linmodel.summary()
    predicted_gross = linmodel.predict(X)
    residual= predicted_gross - df.domestic_gross
    plt.hist(residual)
    plt.title("Residual Histogram")
    plt.show()

#if __name__ == "__main__":  # if i'm run from cmd line
#    print "hello"
