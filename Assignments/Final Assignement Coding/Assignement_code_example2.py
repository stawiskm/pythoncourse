import pandas as pd
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(filename='data_wrangling.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info("Loaded data from %s", file_path)
        return data
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
    except Exception as e:
        logging.error("Error loading data: %s", str(e))
        raise

def remove_duplicates(data):
    try:
        cleaned_data = data.drop_duplicates()
        logging.info("Removed duplicate entries")
        return cleaned_data
    except Exception as e:
        logging.error("Error removing duplicates: %s", str(e))
        raise

def create_summary_table(data):
    summary_table = data.groupby('Visit_Reason')['Visit_Duration'].mean().reset_index()
    logging.info("Created summary table")
    return summary_table

def visualize_data(summary_table):
    plt.figure(figsize=(10, 6))
    plt.bar(summary_table['Visit_Reason'], summary_table['Visit_Duration'])
    plt.xlabel('Visit Reason')
    plt.ylabel('Average Visit Duration')
    plt.title('Average Visit Duration by Visit Reason')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data_visualization.png')
    logging.info("Visualized data and saved the chart")

if __name__ == "__main__":
    try:
        file_path = 'visit_data.csv'
        data = load_data(file_path)
        print("Loaded data:")
        print(data.head())

        cleaned_data = remove_duplicates(data)

        summary_table = create_summary_table(cleaned_data)
        print("Summary Table:")
        print(summary_table)

        visualize_data(summary_table)

    except Exception as e:
        print("An error occurred:", str(e))
        logging.error("An error occurred: %s", str(e))
