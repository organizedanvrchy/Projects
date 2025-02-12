# Purpose
This is a simple data extraction and manipulation project using a small public dataset. 
Data was obtained via [NYC Open Data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data).

---

## How to Run  
### Prerequisites  
Ensure you have Python and the required libraries installed. This project uses the `pandas` library for data manipulation.  

### Steps  
1. **Clone the repository** (or download the script manually):  
   ```sh
   git clone https://github.com/your-username/squirrel-census.git
   cd squirrel-census
   ```
2. **Install required libraries**: <br>
  If you haven't installed pandas, run:
  ```sh
  pip install pandas
  ```
3. **Run the script**:
   ```sh
   python main.py
   ```
4. **Result**: <br>
After running the script, you will find a new file squirrel_count.csv that contains the counts of each squirrel fur color in Central Park (in 2018).

---

## Notes
🐿️ Fur Color Count – <br> The script counts the number of squirrels for each fur color (Gray, Black, Cinnamon). <br>
📊 CSV Output – <br> The results are saved in a CSV file (squirrel_count.csv) for further analysis or visualization. <br>
⚡ Efficient Calculation – <br> The script uses both a direct filtering approach (via pandas) and an alternative for loop method to count the squirrels, with the direct approach being the more efficient solution. <br>
📅 Dataset – <br> Uses the 2018 Central Park Squirrel Census data for analysis. <br>
