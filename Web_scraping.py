import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import xlwt
from xlwt import Workbook

page = urllib.request.urlopen( 'https://www.imdb.com/chart/top/?ref_=nv_mv_250' ) # reference of url

soup = BeautifulSoup( page, 'html.parser' )  # returns the html content of the page
titles = soup.findAll( 'td', attrs={'class': 'titleColumn'} )  #list of tag values for movie name
ratings = soup.findAll( 'td', attrs={'class': 'ratingColumn imdbRating'} )   #list of tag values for movie rstings
movie = str( input( "Enter movie name: " ) )
wb = xlwt.Workbook()
sheet1 = wb.add_sheet( 'Sheet 1' )
row_num = 0
for (t, r) in zip( titles, ratings ):
    if movie.casefold() in t.text.strip().casefold():
        print( t.text.strip(), r.text.strip() )
    sheet1.write( row_num, 0, t.text.strip() )
    sheet1.write( row_num, 1, r.text.strip() )
    row_num += 1
wb.save( 'Movie_Ratings.csv' )