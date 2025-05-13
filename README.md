# Popular_first_names
Based on Bonns (Germany) public available data we have the most popular names plotted and have a little script to see the popularity of a given first name over time.

More and more cities give their citizens access to their data. Bonn conveniently shares their data in (mostly) csv files with us (link). This little project looks at the most popular names and gives a little script to see the popularity of a given name over time.

## Prelude
### Prepare and get ready

Python packages I used
	pandas
	matplotlip
	pathlib

Some variables and annotations in the figures are in German. Here is the dictionary:
Vorname – First name
Jahr – Year
Anzahl – Count
Geschlecht – sex



## Chapter 1
### Get the data

[Here](https://opendata.bonn.de/search/type/dataset?query=&sorting=created%7CDESC) you can find the first names given to the new born citizens of Bonn. Most files are CSV files. Download the files. Here you find them in “`Raw_data`”.

## Chapter 2
### Clean up data

The data have inconsistent naming. Not every file is a `csv` file and they added a column (`position`) in some files. After my initial excitement and analysis I realized that some names are duplicates and appear with several positions. Sadly they don’t describe what the `position` means (maybe different Standesämter?). Therefore I did the following clean up to the data. 

Use any spreadsheet software you are familiar with:
- Rename all files in a consistent manner (`Vornamen_*.csv`) * = year
  - This is important, because our script will automatically load data from the files and uses the file name (the year) to link the count of a given name to a specific year. Therefore each year you can just add the new csv file and run it again and again.
- Save all `non-csv` files as `csv`, use `;` as separator
- I sorted all files columns in the same order `1. vornamen 2. anzahl 3. geschlecht 4. position`
- Store files in a folder called “`Vornamen`”

Here is the first script. Run Sum_up_dublicates.py.
- I dropped the `columns` `geschlecht` and `position` for further analysis. 
- I summed up all duplicate names. This would make it also easier to search by hand.
- The new `csv` files are `,` separated and are stored in a new folder “`Vornamen_dublicates_removal`”

## Chapter 3
### Popular first names in Bonn

I have prepared two scripts which display either the 5 most popular names or the 10 most popular names. It will then save it as a png.
    1. `Vornamen_Overtime.py` displays the 5 most popular names
    2. `Vornamen_Overtime_top10.py` displays the 10 most popular names

## Chapter 4
### Which name was popular in each year.

The script `Vornamen_each_year_separate.py` just produces a graph for each year separately. It displays the 5 most common names in a `png`.

## Chapter 5
### How many other people have my name?

I though it would be a nice addition to search for a specific name and display it overtime. The script `ask_for_name.py` will ask for an input after being started. You can write your name (e.g. Janina) and it will blot your name over time and saves it as a `png`.
