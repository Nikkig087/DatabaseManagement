

from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# connect our file to the db
db = create_engine("postgresql:///chinook") # /// means db is hosted locally within our workspace

meta = MetaData(db) # has a collection of our table objects and the associated data within the objects ie data about the tables and the data about data in tables

#create a variable for "Artist" table
# format when defining cols is Column name, then type of data presented then optional fields after that
artist_table = Table(
    "Artist", meta,
    Column("ArtistId",Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album",meta,
    Column("AlbumId",Integer,primary_key=True),
    Column("Title",String),
    Column("ArtistId",Integer,ForeignKey("artist_table.ArtistId")) # tell it what table to point to for the foreign key
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),#we are defining all tables, this is technically a foreign key but we dont want to have to refer to another table and have to define it
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)
#connecting to db
with db.connect() as connection:

    #Query 1 - Select all recordsd from the Artist table
    #select_query = artist_table.select()

    #Query 2 - Select only the Name column from the Artist table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name]) #.c means columns


    # Query 3 - select only 'Queen' from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results: # for each result in our results list
        print(result)