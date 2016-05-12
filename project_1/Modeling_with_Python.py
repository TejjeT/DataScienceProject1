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

#Challenge 18
def build_numeric_model(movie_df):
        """
        This function build a linear regression model with all the numeric variables.
        """
        import statsmodels.formula.api as smf
        #build a multivariate reg model
        linmodel_multi_f = smf.ols(formula='domestic_gross ~ opening_per_theater + opening_weekend_take + production_budget + widest_release + worldwide_gross', data=movie_df).fit()
        return linmodel_multi_f.summary()


#Challenge 19
def build_more_model(movie_df):
        """
        This function add additional features and test the model out.
        """
        #number of theaters open to
        movie_df['number_of_theaters_open']= movie_df['opening_weekend_take']/movie['opening_per_theater']
        movie_df['title_length']= len(movie_df['alt_title'])

        #create some models
        import statsmodels.formula.api as smf
        #build a multivariate reg model
        linmodel_multi_2 = smf.ols(formula='domestic_gross ~  production_budget + widest_release + number_of_theaters_open+worldwide_gross', data=movie_df).fit()
        return linmodel_multi_2.summary()

#Challenge 20
def create_dummy_feature(movie_df):
        """
        This function creates dummy features.
        """
        movie_df.director.value_counts()[:5]
        N = 4
        top_directors = movies.director.value_counts().index[:N]
        top_dir_movies = movies[movies['director'].isin(top_directors)]
        dummies = pd.get_dummies(top_dir_movies['director'])
        movie_df_dir = pd.merge(movie_df, dummies, left_index=True,  right_index=True, how='left')
        #fill in missing value for the directors to 0
        movie_df_dir['Joel Schumacher'].fillna(0,inplace=True)
        movie_df_dir['Ridley Scott'].fillna(0,inplace=True)
        movie_df_dir['Steven Spielberg'].fillna(0,inplace=True)
        movie_df_dir['Woody Allen'].fillna(0,inplace=True)

        features = ['production_budget','widest_release', 'number_of_theaters_open',
                    'Steven Spielberg',
                    'Woody Allen',
                    'Ridley Scott',
                    'Joel Schumacher']
        related_columns = features + ['domestic_gross']
        print related_columns


        clean_movie_df_dir = movie_df_dir[related_columns].dropna()
        print '%i movies with all necessary info.' % len(clean_movie_df_dir)

        import statsmodels.api as sm
        Y = clean_movie_df_dir['domestic_gross']
        X = sm.add_constant(clean_movie_df_dir[features])


        #split train and test dataset
        from sklearn.cross_validation import train_test_split
        # splits x -> x_train, x_test
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

        #fit model on train set
        model = sm.OLS(Y_train, X_train).fit()
        model.summary()

        #fit model on test set
        predicted_gross = model.predict(X_test)
        plt.scatter(X_test.production_budget, Y_test, color='gray')
        plt.plot(X_test.production_budget, predicted_gross)
        plt.title("multivariate for Domestic Gross")
        plt.xlabel("Budget ($100M)")
        plt.ylabel("Domestic Gross ($100M)")
        plt.show()


#if __name__ == "__main__":  # if i'm run from cmd line
#    print "hello"
