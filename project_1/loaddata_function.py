import loaddata
import pandas as pd
movie_dicts = loaddata.load_mojo_data()
movie_df = pd.DataFrame(movie_dicts)
