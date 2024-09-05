# DiamondStatsTool

**DiamondStatsTool** is a Python application that provides various statistics and insights about diamonds based on data from a CSV file. It includes functionality to analyze diamond prices, cuts, colors, and carat values.

## Project Structure

The project consists of the following main files:

- **`app.py`**: The main script that initializes the application and handles user interactions through a menu.
- **`helper.py`**: Contains helper functions for performing specific calculations on the diamond data.
- **`menu.py`**: Manages the display of the menu and handles user choices.

The dataset `diamonds.csv` is included in the repository.

## Functions

### 1. Maximum Diamond Price

Calculates the highest price of diamonds.

```python
def MaxDiamondPrice(file_path):
    df = pd.read_csv(file_path)
    max_price_loc = df['price'].max()
    return max_price_loc
```
### 2. Average Diamond Price

Computes the average price of diamonds.

```python
def AvgDiamondPrice(file_path):
    df = pd.read_csv(file_path)
    average_price_loc = df['price'].mean()
    return average_price_loc
```

### 3. Count of Ideal Cut Diamonds

Counts the number of diamonds with the "Ideal" cut.

```python
def CountIdealCutDiamonds(file_path):
    df = pd.read_csv(file_path)
    count_ideal_loc = len(df[df['cut'] == 'Ideal'])
    return count_ideal_loc
```

### 4. Unique Diamond Colors

Finds the number of unique diamond colors and lists them.

```python
def UniqDiamondColors(file_path):
    df = pd.read_csv(file_path)
    unique_colors = set(df['color'])
    num_colors_loc = len(unique_colors)
    return num_colors_loc, unique_colors
```

### 5. Average Price Per Color

Calculates the average price for each diamond color.

```python
def AvgPricePerColor(file_path):
    df = pd.read_csv(file_path)
    avg_price_color_loc = df.groupby('color')['price'].mean()
    return avg_price_color_loc
```

### 6. Median Carat of Premium Diamonds

Computes the median carat weight for diamonds with the "Premium" cut.

```python
def MedianCaratPremDiamonds(file_path):
    df = pd.read_csv(file_path)
    premium_diamonds = df[df['cut'] == 'Premium']
    median_carat_loc = premium_diamonds['carat'].median()
    return median_carat_loc
```

### 7. Average Carat Per Cut

Calculates the average carat value for each cut type.

```python
def AvgCaratPerCut(file_path):
    df = pd.read_csv(file_path)
    avg_carat_per_cut_loc = df.groupby('cut')['carat'].mean()
    return avg_carat_per_cut_loc
```
## Menu System

The menu system is managed using the **`enum`** module to define options. Here is how the menu options are defined:

```python
from enum import Enum

class MenuOption(Enum):
    MAX_PRICE = '1'
    AVG_PRICE = '2'
    COUNT_IDEAL = '3'
    UNIQUE_COLORS = '4'
    AVG_PRICE_PER_COLOR = '5'
    MEDIAN_CARAT_PREMIUM = '6'
    AVG_CARAT_PER_CUT = '7'
    CLEAR_SCREEN = '8'
    EXIT = '9'
```

## Menu Options

* 1: The highest diamond price
* 2: The average price of a diamond
* 3: Number of diamonds with Ideal cut
* 4: Number of different colors and list of colors
* 5: Average price per color
* 6: The median carat of Premium diamonds
* 7: Average carat for each cut type

## Usage
1. **Install Dependencies:** Make sure you have **`pandas`** installed. You can install it using **pip:**


```Python
pip install pandas
```

2. **Run the Application:** Execute the main script to start the application:


```Python
python app.py
```

3. **Interact with the Menu:** Follow the on-screen menu to select various options and view the results.

