#c.execute('DROP TABLE All_Habits') 		#RE-CREATE DATABASE FROM THE START
c.execute("""CREATE TABLE IF NOT EXISTS All_Habits (
				Habit TEXT,
				DW TEXT,
				Start_Date TEXT,
				CS INTEGER,
				LS INTEGER)""")

#INSERTING THE PRE-REQUISETS
#c.execute("INSERT INTO All_Habits VALUES('8 Glasses of water', 'DAILY' , '2021-11-26 11:30:28' , 9, 12)")
#c.execute("INSERT INTO All_Habits VALUES('Jog 2 miles', 'DAILY' , '2021-11-26 14:30:28' , 7, 9)")
#c.execute("INSERT INTO All_Habits VALUES('Walk the dog', 'WEEKLY' , '2021-11-26 15:30:28' , 2, 2)")
#c.execute("INSERT INTO All_Habits VALUES('Read 5 pages', 'DAILY' , '2021-11-26 16:50:21' , 4, 5)")
#c.execute("INSERT INTO All_Habits VALUES('Review budget', 'WEEKLY' , '2021-11-26 17:27:14' , 0, 1)")

c.execute("""CREATE TABLE IF NOT EXISTS Habit_data (
				Day_Date TEXT,
				Habit_1 INTEGER,
				Habit_2 INTEGER,
				Habit_3 INTEGER,
				Habit_4 INTEGER,
				Habit_5 INTEGER)""")

#c.execute("INSERT INTO Habit_data VALUES('2021-11-12',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-13',1,0,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-14',1,1,1,0,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-15',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-16',1,0,1,0,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-17',1,0,1,0,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-18',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-19',1,1,0,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-20',1,1,0,0,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-21',1,1,0,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-22',1,0,0,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-23',1,1,0,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-24',0,0,0,0,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-25',1,1,0,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-26',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-27',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-28',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-29',0,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-30',1,1,1,0,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-1',1,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-2',0,1,1,1,1)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-3',1,1,1,0,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-4',1,0,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-5',1,1,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-6',1,1,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-7',1,1,1,0,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-8',1,1,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-9',1,1,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-10',1,1,1,1,0)")
#c.execute("INSERT INTO Habit_data VALUES('2021-11-11',1,1,1,1,0)")


#SAVE AND CLOSE DATABASE
con.commit()
con.close()
