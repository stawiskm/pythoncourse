import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='data_wrangling.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Loaded data from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        return None

def remove_duplicates(data):
    try:
        data_cleaned = data.drop_duplicates()
        logging.info("Duplicates removed")
        return data_cleaned
    except Exception as e:
        logging.error(f"Error removing duplicates: {str(e)}")
        return data

def summarize_data(data):
    try:
        data['Month'] = pd.to_datetime(data['Date']).dt.to_period('M')
        summary_table = data.groupby(['Visit_Reason', 'Month'])['Patient'].count().reset_index()
        summary_table.columns = ['Visit_Reason', 'Month', 'Visit_Count']
        logging.info("Data summarized")
        return summary_table
    except Exception as e:
        logging.error(f"Error summarizing data: {str(e)}")
        return None

def visualize_data(data):
    try:
        import matplotlib.pyplot as plt
        unique_reasons = data['Visit_Reason'].unique()

        for reason in unique_reasons:
            reason_data = data[data['Visit_Reason'] == reason]
            plt.plot(reason_data['Month'].astype(str), reason_data['Visit_Count'], label=reason)

        plt.xlabel('Month')
        plt.ylabel('Visit Count')
        plt.title('Visit Count by Month and Visit Reason')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

        logging.info("Data visualized")
    except Exception as e:
        logging.error(f"Error visualizing data: {str(e)}")

def main():
    file_path = 'visit_data.csv'
    data = load_data(file_path)
    
    if data is not None:
        print("Data loaded successfully:")
        print(data.head())

        data_cleaned = remove_duplicates(data)

        summary_table = summarize_data(data_cleaned)
        if summary_table is not None:
            print("\nSummary Table:")
            print(summary_table)

            visualize_data(summary_table)

if __name__ == "__main__":
    main()
