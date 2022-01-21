from tkinter import *
import mysql.connector
from datetime import *
from tkinter import messagebox

# TODO: System Wyszukiwań
# TODO: Karta Użytkownika
# TODO: Dodaj / Usuń użytkownika
# TODO: Zapisz książkę
# ((n*i)+1),x dla n- miejsca w kolejności sekwencji, i- dla for i

# today = date.today()
# print(today)
plik = open()
mydb = mysql.connector.connect(host="localhost", user="root", passwd="!QAZxsw2", database="python")

global cursor

cursor = mydb.cursor()
window = Tk()
global counter
counter = 0


def find_win_close():
    find_win.destroy()


def szukaj_window():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="!QAZxsw2", database="python")
    global Results, bookt2
    global end_res
    end_res = []
    Results = []
    counter = 0
    global cursor, queiry_i1,query_i2,query_i3,query_i4,query_i5,query_i6,query_i7,query_i8,query_i9,query_i10,query_i11,query_i12
    find1 = txt1.get()  # IMIE
    find2 = txt2.get()  # NAZWISKO
    find3 = txt3.get()  # ID
    if find3 != '':
        cursor = mydb.cursor()
        query_i1 = 'Select USERID from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i2 = 'Select IMIE from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i3 = 'Select NAZWISKO from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i4 = 'Select bookt1 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i5 = 'Select bookid1 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i6 = 'Select bookd1 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i7 = 'Select bookt2 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i8 = 'Select bookid2 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i9 = 'Select bookd2 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i10 = 'Select bookt3 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i11 = 'Select bookid3 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'
        query_i12 = 'Select bookd3 from new_table WHERE USERID = ' + "'" + str(find3) + "'" + ';'

    elif find3 == '' and (find1 != '' or find2 != ''):
        if find1 != '' and find2 == '':
            cursor = mydb.cursor()
            query_i1 = 'Select USERID from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i2 = 'Select IMIE from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i3 = 'Select NAZWISKO from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i4 = 'Select bookt1 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i5 = 'Select bookid1 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i6 = 'Select bookd1 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i7 = 'Select bookt2 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i8 = 'Select bookid2 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i9 = 'Select bookd2 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i10 = 'Select bookt3 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i11 = 'Select bookid3 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'
            query_i12 = 'Select bookd3 from new_table WHERE IMIE = ' + "'" + str(find1) + "'" + ';'

        elif find1 == '' and find2 != '':
            cursor = mydb.cursor()
            query_i1 = 'Select USERID from new_table WHERE NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i2 = 'Select IMIE from new_table WHERE NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i3 = 'Select NAZWISKO from new_table WHERE NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i4 = 'Select bookt1 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i5 = 'Select bookid1 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i6 = 'Select bookd1 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i7 = 'Select bookt2 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i8 = 'Select bookid2 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i9 = 'Select bookd2 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i10 = 'Select bookt3 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i11 = 'Select bookid3 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
            query_i12 = 'Select bookd3 from new_table WHERE IMIE = ' + "'" + str(find2) + "'" + ';'
        elif find1 != '' and find2 != '':
            cursor = mydb.cursor()
            query_i1 = 'Select USERID from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i2 = 'Select IMIE from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i3 = 'Select NAZWISKO from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i4 = 'Select bookt1 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i5 = 'Select bookid1 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i6 = 'Select bookd1 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i7 = 'Select bookt2 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i8 = 'Select bookid2 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i9 = 'Select bookd2 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i10 = 'Select bookt3 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i11 = 'Select bookid3 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'
            query_i12 = 'Select bookd3 from new_table WHERE IMIE = ' + "'" + str(
                find1) + "'" + ' and NAZWISKO = ' + "'" + str(find2) + "'" + ';'

        else:
            messagebox.showwarning('ERROR #0001', 'find1 and find2 are wrong')
    else:
        messagebox.showwarning('ERROR #0000', 'find3, find1 and find2 are wrong')


    if find1 !='' or find2 !='' or find3 !='':
        cursor.execute(query_i1)
        for USERID in cursor:
            if USERID == (None,) or USERID == 'Null':
                end_res.append('')
            else:
                end_res.append(USERID)
        counter = 0
        cursor.execute(query_i2)
        for IMIE in cursor:
            if IMIE == (None,) or IMIE == 'Null':
                end_res.insert((2 * counter) + 1, '')
            else:
                end_res.insert((2 * counter) + 1, IMIE)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i3)
        for NAZWISKO in cursor:
            if NAZWISKO == (None,) or NAZWISKO == 'Null':
                end_res.insert((3 * counter) + 3, '')
            else:
                end_res.insert((3 * counter) + 2, NAZWISKO)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i4)
        for bookt1 in cursor:
            if bookt1 == (None,) or bookt1 == 'Null':
                end_res.insert((4 * counter) + 3, '')
            else:
                end_res.insert((4 * counter) + 3, bookt1)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i5)
        for bookid1 in cursor:
            if bookid1 == (None,) or bookid1 == 'Null':
                end_res.insert((5 * counter) + 4, '')
            else:
                end_res.insert((5 * counter) + 4, bookid1)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i6)
        for bookd1 in cursor:
            if bookd1 == (None,) or bookd1 == 'Null':
                end_res.insert((6 * counter) + 5, '')
            else:
                end_res.insert((6 * counter) + 5, bookd1)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i7)
        for bookt2 in cursor:
            if bookt2 == (None,) or bookt2 == 'Null':
                end_res.insert((7 * counter) + 6, '')
            else:
                end_res.insert((7 * counter) + 6, bookt2)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i8)
        for bookid2 in cursor:
            if bookid2 == (None,) or bookid2 == 'Null':
                end_res.insert((6 * counter) + 5, '')
            else:
                end_res.insert((8 * counter) + 7, bookid2)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i9)
        for bookd2 in cursor:
            if bookd2 == (None,) or bookd2 == 'Null':
                end_res.insert((9 * counter) + 8, '')
            else:
                end_res.insert((9 * counter) + 8, bookd2)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i10)
        for bookt3 in cursor:
            if bookt3 == (None,) or bookt3 == 'Null':
                end_res.insert((10 * counter) + 9, '')
            else:
                end_res.insert((10 * counter) + 9, bookt3)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i11)
        for bookid3 in cursor:
            if bookid3 == (None,) or bookid3 == 'Null':
                end_res.insert((11 * counter) + 10, '')
            else:
                end_res.insert((11 * counter) + 10, bookid3)
            counter = counter + 1
        counter = 0
        cursor.execute(query_i12)
        for bookd3 in cursor:
            if bookd3 == (None,) or bookd3 == 'Null':
                end_res.insert((12 * counter) + 11, '')
            else:
                end_res.insert((12 * counter) + 11, bookd3)
            counter = counter + 1
        counter = 0



#ID,I,N,b1,1id,b1,
    for i in range(len(end_res)):
        print(type(i))
    for i in range(len(end_res)):

        if i != 0 :
            end_res[i] = "".join(end_res[i])
        elif i == 0 or i == 4 or i == 7 or i == 10 and i != '':
            s = 0
            for x in end_res[i]:
                s += x
            end_res[i] = s
            print(s)
        if i == 5 and i == 8 and i == 11:
            end_res[i] = datetime.strptime("".join(end_res[5]), "%Y-%m-%d %H:%M:%S")
        print(type(end_res[i]))
    print(type(end_res))
    button = []
    global find_win
    find_win = Toplevel(window)

    find_win.title('Wyszukiwarka')
    find_win.geometry('500x500')
    find_win.resizable(True, True)
    print(end_res)
    New_button = Button(find_win, text='XD', command=find_win_close)
    New_button.grid(row=4, column=0)
    rameczka = Frame(find_win, borderwidth=8)
    rameczka.grid(row=0, column=0)
    rameczka.config(bg='gray')
    for i in range(int(len(end_res) / 12)):
        b = Button(rameczka,
                   text=str(end_res[12 * counter + 0])+' ' + end_res[12 * counter + 1]+' ' + end_res[12 * counter + 2]+' ' + end_res[
                       12 * counter + 3]+' ' + end_res[12 * counter + 6]+' ' + end_res[12 * counter + 9],
                   command=lambda i=i: boardWindow(i))

        b.pack()
        button.append(b)
        counter = counter + 1
    mydb.commit()
    mydb.close()
def main_window():

    global frame1, txt1,txt2,txt3

    frame1 = Frame(window, borderwidth=8)
    frame1.grid(row=0, column=0)
    frame1.config(bg='gray')

    txt1_info = Label(frame1, text='IMIE')
    txt1_info.grid(row=0, column=0)
    txt1 = Entry(frame1, width=50)
    txt1.grid(row=1, column=0)

    txt2_info = Label(frame1, text='NAZWISKO')
    txt2_info.grid(row=0, column=1)
    txt2 = Entry(frame1, width=50)
    txt2.grid(row=1, column=1)

    txt3_info = Label(frame1, text='ID')
    txt3_info.grid(row=0, column=2)
    txt3 = Entry(frame1, width=50)
    txt3.grid(row=1, column=2)

    button = Button(frame1, text='Szukaj', command=szukaj_window)
    button.grid(row=1, column=4)
    window.title('Main Window')


def boardWindow(i):
    print(i)
    # print(''+end_res[5],''+end_res[8])
    #t1 = datetime.strptime("".join(end_res[5]), "%Y-%m-%d %H:%M:%S")
    #t2 = datetime.strptime("".join(end_res[8]), "%Y-%m-%d %H:%M:%S")
    #print(t1, t2)


# cursor = mydb.cursor()
# query = "Select IMIE from new_table"
# cursor.execute(query)

# for row in cursor:
#    Data = []
#    Data.append(row)
#    print(Data)
main_window()
mydb.commit()
# mydb.close()
window.mainloop()
#:D
