# helper.py
import pandas as pd

def MaxDiamondPrice(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Extract the maximum value from the 'price' column using the .max() method
    max_price_loc = df['price'].max()
    return max_price_loc

def AvgDiamondPrice(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Compute the mean of the 'price' column using the .mean() method
    average_price_loc = df['price'].mean()
    return average_price_loc

def CountIdealCutDiamonds(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Filter rows where 'cut' is 'Ideal' and count the number of such rows using len()
    count_ideal_loc = len(df[df['cut'] == 'Ideal'])
    return count_ideal_loc

def UniqDiamondColors(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Create a set of unique values from the 'color' column
    unique_colors = set(df['color'])
    # Count the number of unique colors and return both count and set
    num_colors_loc = len(unique_colors)
    return num_colors_loc, unique_colors

def AvgPricePerColor(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Group by 'color' and calculate the mean price for each color group using .groupby() and .mean()
    avg_price_color_loc = df.groupby('color')['price'].mean()
    return avg_price_color_loc

def MedianCaratPremDiamonds(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Filter rows where 'cut' is 'Premium' and calculate the median of 'carat' column using .median()
    premium_diamonds = df[df['cut'] == 'Premium']
    median_carat_loc = premium_diamonds['carat'].median()
    return median_carat_loc

def AvgCaratPerCut(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Group by 'cut' and calculate the mean carat value for each cut type using .groupby() and .mean()
    avg_carat_per_cut_loc = df.groupby('cut')['carat'].mean()
    return avg_carat_per_cut_loc
