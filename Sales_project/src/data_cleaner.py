import pandas as pd

class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def clean_data(self):
        try:
            # Remove duplicates
            self.df = self.df.drop_duplicates()

            # Remove missing values
            self.df = self.df.dropna()

            # Convert order_date to datetime
            self.df['order_date'] = pd.to_datetime(self.df['order_date'])

            # Create new column
            self.df['total_amount'] = self.df['quantity'] * self.df['unit_price']

            return self.df

        except Exception as e:
            raise Exception(f"Error while cleaning data: {e}")