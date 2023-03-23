"""Second assignment."""
import datetime
import pandas as pd


def merge_weekend_reports_into_one(saturday_filename: str, sunday_filename: str, output_filename: str) -> None:
    """Merge weekend reports into one and save it to a new file."""
    saturday = pd.read_csv(saturday_filename, encoding='utf8', delimiter=';')
    sunday = pd.read_csv(sunday_filename, encoding='utf8', delimiter=';')

    sunday['metric_id'] += saturday['metric_id'].max()

    # Add a new column that will contain current date
    saturday['file_generation_date'] = ''
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    saturday.at[0, 'file_generation_date'] = current_date

    # Concatenate dataframes and save to a new file
    result = pd.concat([saturday, sunday])
    result.to_csv(output_filename, encoding='utf8', index=False, sep=';')


if __name__ == '__main__':
    merge_weekend_reports_into_one('data_2023-02-11.csv', 'data_2023-02-12.csv', 'aggregated_data.csv')
