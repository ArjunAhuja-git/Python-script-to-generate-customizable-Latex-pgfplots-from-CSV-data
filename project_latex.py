import csv
import sqlite3
import json
from json import dumps, load
from pprint import pprint
import csv
import os
import os.path

if os.path.isfile("new_file.json") == True :
    f = open("new_file.json", "w")
    f.seek(0, 0)
    f.truncate()
temp = open("Json.json")
count = 2
temp.seek(0, 0)

XCOL = []
YCOL = []

stop = 0
for line1 in temp :
    if line1[0] == "{" :
        stop = stop + 1
    if stop is 2 :
        f = open("new_file.json", "a")
        f.write("}")
        break
    f = open("new_file.json", "a")
    f.write(line1)
    f.close()
with open('new_file.json') as input_file:
    file_data = json.load(input_file)               # take input from the user for the database name (format : "name.db") and table name
    name_of_database = file_data["name_of_database"]
    table_name = file_data["name_of_table"]
    XCOL = [c for c in file_data["xheading"]]
    YCOL = [z for z in file_data["yheading"]]
    Queries = [m for m in file_data["queries"]]

conn = sqlite3.connect(name_of_database)            # make connection to the sqlite3 database
conn.text_factory = str                             # set the text factory to "string"
cur = conn.cursor()                                 # create a cursor object
cur.execute("DROP TABLE IF EXISTS %s;" % table_name)# drop all tables if same name table exists

if os.path.isfile("new_file.json") == True :
    f = open("new_file.json", "w")
    f.seek(0, 0)
    f.truncate()

with open('sample.csv') as f:
  reader = csv.reader(f)                            # read all the values in each column in list form
  row1 = next(reader)                               # we ignore the row which contains the column - NAMES
string = ','.join(row1)                             # making string from this row
if string[len(string) - 1] != ',' :
    string = string + ','
string = string.replace(',', ' INTEGER,')           # this part involves making INSERT into TABLE VALUES query since we don't know how many columns we may have
                                                    #   this string gives string in the form "column_name1 varchar(10), column_name2 varchar(10, ... and so on)"
temp = list(string)                                 # create a temporary list of the string to remove first garbage value
del temp[len(string) - 1]
string = ''.join(temp)                              # removing garbage value in the 'string' intially formed
cur.execute("CREATE TABLE %s (%s);" % (table_name, string))# execute the table CREATE TABLE with string as the column names taken from CSV File

script = open("latex.txt", "w")                     # open the script in write mode(create it initially)
                                                    # starting string for the latex scipt incluing "\begin, \document," etc.
sequence = ["\\documentclass{article}\n","\\usepackage[margin=0.5in]{geometry}\n","\\usepackage[utf8]{inputenc}\n","\\usepackage{pgfplots}\n","\\pgfplotsset{width=10cm,compat=1.9}\n","\\begin{document}\n"]
script.writelines(sequence)                         # write muliple lines in the script(latex script)


#*************************JSON-File Data Parsing*******************************#
line_counter = 0
scatter_counter = 0
bar_counter = 0
column_capture_counter = 0
temp = open("Json.json")
count = 0
counter = 0
for line in temp :
    if(line[0] == "{") :
        count = count + 1
track = count
temp.seek(0, 0)

title = []
xlabel = []
ylabel = []
scale = []
grid_style = []
legend_pos = []
single_legend = {}
legend_store = {}
line_nature = {}
line_color = {}
mark_shape = {}
xcolm = {}
ycolm = {}

label_count = []
label_name = {}
label_mark = {}
label_color = {}
choices = {}
xycolumn = {}

xcolm_bar = {}
ycolm_bar = {}
y_label = []
x_label = []
space_bars = []
xlegend = []
ylegend = []
anchor_pos = []
bar_interval = []
legend = []
title_bar = []
automatic_input = []

user_guide = {}
user_guide["line"] = 0
user_guide["scatter"] = 0
user_guide["bar"] = 0
take_count = 0
while(count != 0) :
    if(count < track) :
        f = open("new_file.json", "w")
        f.seek(0, 0)
        f.truncate()
    for line1 in temp :
        if line1[0] == "}" :
            f = open("new_file.json", "a")
            f.write("}")
            break
        f = open("new_file.json", "a")
        f.write(line1)
        counter = 0
        f = open("new_file.json", "r")
        for k in f :
            counter = counter + 1
    count = count - 1;
    f.close()
    with open('new_file.json') as input_file:
        file_data = json.load(input_file)

    if(counter == 13) :
        #**********************************************************************#
        if isinstance(file_data["xcolumn"], list) is True and len(file_data["xcolumn"]) > 1 :
            xcolm[line_counter] = []
            ycolm[line_counter] = []
            line_nature[line_counter] = []
            line_color[line_counter] = []
            mark_shape[line_counter] = []
            legend_store[line_counter] = []
            for i in range(0, len(file_data["xcolumn"])) :
                xcolm[line_counter].insert(i, file_data["xcolumn"][i])
                ycolm[line_counter].insert(i, file_data["ycolumn"][i])
                line_nature[line_counter].insert(i, file_data["nature_of_line"][i])
                line_color[line_counter].insert(i, file_data["color"][i])
                mark_shape[line_counter].insert(i, file_data["mark_style"][i])
                legend_store[line_counter].insert(i, file_data["legend"][i])
        else :
            xcolm[line_counter] = []
            xcolm[line_counter].insert(0, file_data["xcolumn"])
            ycolm[line_counter] = []
            ycolm[line_counter].insert(0, file_data["ycolumn"])
            line_nature[line_counter] = []
            line_nature[line_counter].insert(0, file_data["nature_of_line"])
            line_color[line_counter] = []
            line_color[line_counter].insert(0, file_data["color"])
            mark_shape[line_counter] = []
            mark_shape[line_counter].insert(0, file_data["mark_style"])
            single_legend[line_counter] = file_data["legend"]
        xlabel.insert(line_counter, file_data["xlabel"])
        ylabel.insert(line_counter, file_data["ylabel"])
        grid_style.insert(line_counter, file_data["grid_style"])
        title.insert(line_counter, file_data["title"])
        legend_pos.insert(line_counter, file_data["legend_position"])
        scale.insert(line_counter, file_data["scale"])
        #**********************************************************************#
        line_counter = line_counter + 1
        user_guide["line"] = line_counter
        automatic_input.append(1)
        take_count = take_count + 1
        #**********************************************************************#
    elif(counter == 7) :
        #**********************************************************************#
        label_count.insert(scatter_counter, file_data["no_labels"])
        #**********************************************************************#
        label_name[scatter_counter] = []
        for i in range(0, label_count[scatter_counter]) :
            label_name[scatter_counter].insert(i, file_data["label_name"][i])
        #**********************************************************************#
        label_mark[scatter_counter] = []
        for i in range(0, label_count[scatter_counter]) :
            label_mark[scatter_counter].insert(i, file_data["label_mark"][i])
        #**********************************************************************#
        label_color[scatter_counter] = []
        for i in range(0, label_count[scatter_counter]) :
            label_color[scatter_counter].insert(i, file_data["label_color"][i])
        #**********************************************************************#
        choices[scatter_counter] = []
        for i in range(0, len(file_data["choices"])) :
            choices[scatter_counter].insert(i, file_data["choices"][i])
        #**********************************************************************#
        xycolumn[scatter_counter] = []
        for i in range(0, len(file_data["x_y_col"])) :
            xycolumn[scatter_counter].insert(i, file_data["x_y_col"][i])
        #**********************************************************************#
        scatter_counter = scatter_counter + 1                                   #currently okay again
        user_guide["scatter"] = scatter_counter
        automatic_input.append(2)
        take_count = take_count + 1
        #**********************************************************************#
    elif(counter == 12) :
        #**********************************************************************#
        if isinstance(file_data["xcolumn"], list) is True and len(file_data["xcolumn"]) > 1 :
            xcolm_bar[bar_counter] = []
            ycolm_bar[bar_counter] = []
            for i in range(0, len(file_data["xcolumn"])) :
                xcolm_bar[bar_counter].insert(i, file_data["xcolumn"][i])
                ycolm_bar[bar_counter].insert(i, file_data["ycolumn"][i])
        else :
            xcolm_bar[bar_counter] = []
            xcolm_bar[bar_counter].insert(0, file_data["xcolumn"])
            ycolm_bar[bar_counter] = []
            ycolm_bar[bar_counter].insert(0, file_data["ycolumn"])
        y_label.insert(bar_counter, file_data["y_label"])
        x_label.insert(bar_counter, file_data["x_label"])
        space_bars.insert(bar_counter, file_data["space_over_bars"])
        xlegend.insert(bar_counter, file_data["xcord_legend"])
        ylegend.insert(bar_counter, file_data["ycord_legend"])
        anchor_pos.insert(bar_counter, file_data["anchor_position"])
        bar_interval.insert(bar_counter, file_data["interval_between_bars"])
        legend.insert(bar_counter, file_data["legend"])
        title_bar.insert(bar_counter, file_data["title"])
        #**********************************************************************#
        bar_counter = bar_counter + 1#---------------------------------------------------------------------------------#
        user_guide["bar"] = bar_counter
        automatic_input.append(3)
        take_count = take_count + 1
        #**********************************************************************#
#******************************************************************************#
def line_plot() :

    script.seek(0, 2)                               # set the position pointer at the end of the file offset by 0 spaces
    if len(xcolm[call_line]) > 1 :
        for i in range(0, len(xcolm[call_line])) :
            xcol = xcolm[call_line][i]              # asking the user to enter the column name if csv file for x-coordinate column
            ycol = ycolm[call_line][i]              # asking the user to enter the column name if csv file for y-coordinate column
            index1 = heading.index(xcol)            # storing the heading of both x and y columns in index1 and index2 variables
            index2 = heading.index(ycol)

            with open('sample.csv', 'r') as f:      # open the csv file as f
                reader = csv.reader(f)              # read rows into a dictionary format row
                subset0 = []
                subset = []
                reader.next()                       # advancing the reader to next row to avoid the column names
                for row in reader :
                    subset0 = []
                    subset0.append(int(row[index1]))# appending the x-coordinate of the selected row(input by user)
                    subset0.append(int(row[index2]))# appending the y-coordinate of the selected row(input by user)
                    subset.append(tuple(subset0))   # appending the tuple of x,y in the subset named list
            subset2 = [str(list(u)) for u in subset]# making every list in subset as a string
            no_question_marks = '?,'*len(row1)      # calculating the number of question mark characters(no. of columns in the table) to be included in the string
            no_question_marks = no_question_marks[0:len(no_question_marks) - 1]
            # execute the muliple INSERT into TABLE queries using cursor_object.executemany(query)
            cur.executemany("INSERT into %s values(%s);" % (table_name, no_question_marks), to_db)
            conn.commit()                           # commit the changes done in the data base(after extracting data from the csv file)

            xmin = 0                                # set the minimum x-coordinate
            ymin = 0                                # set the minimum y-coordinate
            xtick = scale[call_line]                # find xtick (space between ticks on axis) by taking average of the min and max x value
            ytick = scale[call_line]                # find ytick (space between ticks on axis) by taking average of the min and max y value
            xmax = subset[len(subset) - 1][0] + xtick
            ymax = subset[len(subset) - 1][1] + ytick

            l1 = [int(xmin),]
            for k in range(1, len(subset)) :
                s = int(l1[k - 1]) + xtick          # get the tick-values for x axis to mark the x axis
                l1.append(s)                        # keep appending in a list to get all the x ticks
            l1.append(l1[len(l1) - 1] + xtick)
            l1.append(xmax)
            temp = str(l1)
            t = list(temp)
            t[0] = ''                               # removing garbage values from the list
            t[len(t) - 1] = ''
            temp = ''.join(t)
            xtick = ''.join(("{",temp,"}"))         # get the list for all the ticks on the X-axis

            l2 = [int(ymin),]
            for k in range(1, len(subset)) :        # get the tick-values for x axis to mark the x axis
                s = int(l2[k - 1]) + ytick
                l2.append(s)                        # keep appending in a list to get all the x ticks
            l2.append(l2[len(l2) - 1] + ytick)
            l2.append(ymax)
            temp = str(l2)
            t = list(temp)
            t[0] = ''                               # removing garbage values from the list
            t[len(t) - 1] = ''
            temp = ''.join(t)
            ytick = ''.join(("{",temp,"}"))         # get the list for all the ticks on the X-axis

            put_legend = []
            put_legend = [k for k in legend_store[call_line]]
            convert_legend = str(put_legend)
            convert_legend =  convert_legend.replace("[", "{")
            convert_legend =  convert_legend.replace("]", "}")
            temp = list(convert_legend)
            temp2 = []
            for x in range(0, len(temp)) :
                if temp[x] is "u" :
                    if temp[x - 1] is "{" or temp[x - 1] is " " :
                        continue
                    else :
                        temp2.insert(x, temp[x])
                else :
                    temp2.insert(x, temp[x])
            convert_legend = ''.join(temp2)
            convert_legend = convert_legend.replace("\'", "")

            string = ''.join(subset2)               #******************get_coords******************#
            new = list(string)                      # convert the string in new list
            for j in range(0, len(new)) :
                if new[j] == '[' :
                    new[j] = '('
                if new[j] == ']' :
                    new[j] = ')'
                if new[j] == ' ' :
                    new[j] = ''
            coordinates = ''.join(new)              # replace '[', ']' characters with '(', ')' to make the coordinates string as required in the latex script

            script.seek(0, 2)                       # set the position pointer at the end of the latex script file offset by 0 characters
            add_plot = '''\\addplot[
                            %s, color=%s, mark=%s, mark options={scale=%d}
                            ]
                            coordinates {
                            %s
                            };
                        ''' % (line_nature[call_line][i], line_color[call_line][i], mark_shape[call_line][i], scale[call_line], coordinates)
            if i is 0 :
                string = '''\\begin{tikzpicture}
                            \\begin{axis}[
                            title={%s},
                            xlabel={%s},
                            ylabel={%s},
                            xmin=%d, xmax=%d,
                            ymin=%d, ymax=%d,
                            xtick=%s,
                            ytick=%s,
                            legend pos=%s,
                            ymajorgrids=true,
                            grid style=%s,
                            ]
                            %s
                            \legend%s
                            \end{axis}
                            \end{tikzpicture}''' % (title[call_line], xlabel[call_line], ylabel[call_line], int(xmin), int(xmax), int(ymin), int(ymax), xtick, ytick, legend_pos[call_line], grid_style[call_line], add_plot, convert_legend)
                script.write(string)                # write the finally formatted string for line plot in the latex script
            else :
                temp = open("latex.txt", "r")
                counter = temp.readlines()
                temp.close()

                len_file = len(counter)
                counter.insert(len_file - 4, add_plot)

                temp = open("latex.txt", "w")
                string = ''.join(counter)
                temp.write(string)
                temp.close()
    else :
        xcol = xcolm[call_line][0][0]                # asking the user to enter the column name if csv file for x-coordinate column
        ycol = ycolm[call_line][0][0]                # asking the user to enter the column name if csv file for y-coordinate column
        index1 = heading.index(xcol)                 # storing the heading of both x and y columns in index1 and index2 variables
        index2 = heading.index(ycol)
        with open('sample.csv', 'r') as f:           # open the csv file as f
            reader = csv.reader(f)                   # read rows into a dictionary format row
            subset0 = []
            subset = []
            reader.next()                            # advancing the reader to next row to avoid the column names
            for row in reader :
                subset0 = []
                subset0.append(int(row[index1]))     # appending the x-coordinate of the selected row(input by user)
                subset0.append(int(row[index2]))     # appending the y-coordinate of the selected row(input by user)
                subset.append(tuple(subset0))        # appending the tuple of x,y in the subset named list
        subset2 = [str(list(i)) for i in subset]     # making every list in subset as a string
        no_question_marks = '?,'*len(row1)           # calculating the number of question mark characters(no. of columns in the table) to be included in the string
        no_question_marks = no_question_marks[0:len(no_question_marks) - 1]
        # execute the muliple INSERT into TABLE queries using cursorobject.executemany(query)
        cur.executemany("INSERT into %s values(%s);" % (table_name, no_question_marks), to_db)
        conn.commit()                                # commit the changes done in the data base(after extracting data from the csv file)

        xmin = 0                                     # set the minimum x-coordinate
        ymin = 0                                     # set the minimum y-coordinate
        xtick = scale[call_line]                     # find xtick (space between ticks on axis) by taking average of the min and max x value
        ytick = scale[call_line]                     # find ytick (space between ticks on axis) by taking average of the min and max y value
        xmax = subset[len(subset) - 1][0] + xtick
        ymax = subset[len(subset) - 1][1] + ytick

        l1 = [int(xmin),]
        for k in range(1, len(subset)) :
            s = int(l1[k - 1]) + xtick               # get the tick-values for x axis to mark the x axis
            l1.append(s)                             # keep appending in a list to get all the x ticks
        l1.append(l1[len(l1) - 1] + xtick)
        l1.append(xmax)
        temp = str(l1)
        t = list(temp)
        t[0] = ''                                    # removing garbage values from the list
        t[len(t) - 1] = ''
        temp = ''.join(t)
        xtick = ''.join(("{",temp,"}"))              # get the list for all the ticks on the X-axis

        l2 = [int(ymin),]
        for k in range(1, len(subset)) :             # get the tick-values for x axis to mark the x axis
            s = int(l2[k - 1]) + ytick
            l2.append(s)                             # keep appending in a list to get all the x ticks
        l2.append(l2[len(l2) - 1] + ytick)
        l2.append(ymax)
        temp = str(l2)
        t = list(temp)
        t[0] = ''                                    # removing garbage values from the list
        t[len(t) - 1] = ''
        temp = ''.join(t)
        ytick = ''.join(("{",temp,"}"))              # get the list for all the ticks on the X-axis

        string = ''.join(subset2)                    #******************get_coords******************#
        new = list(string)                           # convert the string in new list
        for i in range(0, len(new)) :
            if new[i] == '[' :
                new[i] = '('
            if new[i] == ']' :
                new[i] = ')'
            if new[i] == ' ' :
                new[i] = ''
        coordinates = ''.join(new)                   # replace '[', ']' characters with '(', ')' to make the coordinates string as required in the latex script

        add_plot = '''\\addplot[
                        %s, color=%s, mark=%s, mark options={scale=%d}
                        ]
                        coordinates {
                        %s
                        };
                    ''' % (line_nature[call_line][0][0], line_color[call_line][0][0], mark_shape[call_line][0][0], scale[call_line], coordinates)
        string = '''\\begin{tikzpicture}
                    \\begin{axis}[
                    title={%s},
                    xlabel={%s},
                    ylabel={%s},
                    xmin=%d, xmax=%d,
                    ymin=%d, ymax=%d,
                    xtick=%s,
                    ytick=%s,
                    legend pos=%s,
                    ymajorgrids=true,
                    grid style=%s,
                    ]
                    %s
                    \legend{%s}
                    \end{axis}
                    \end{tikzpicture}''' % (title[call_line], xlabel[call_line], ylabel[call_line], int(xmin), int(xmax), int(ymin), int(ymax), xtick, ytick, legend_pos[call_line], grid_style[call_line], add_plot, single_legend[call_line])

        script.write(string)                    # write the finally formatted string for line plot in the latex script

#******************************************************************************#
def scatter_plot() :
    script.seek(0, 2)

    label = {}
    for i in range(0, label_count[call_scatter]) :
      label[label_name[call_scatter][i]] = []
      # make each element of label list as a dictionary
      # for each "name", add the mark and the color (make name as the key in the dictionary)
      # and append the color to the mark in the dictionary
      label[label_name[call_scatter][i]].append("mark=" + label_mark[call_scatter][i])
      label[label_name[call_scatter][i]].append(label_color[call_scatter][i])

    xcol = xycolumn[call_scatter][0]
    ycol = xycolumn[call_scatter][1]
    index1 = heading.index(xcol)                    # storing the heading of both x and y columns in index1 and index2 variables
    index2 = heading.index(ycol)
    with open('sample.csv', 'r') as f:              # open the csv file as f
        reader = csv.reader(f)                      # read rows into a dictionary format row
        subset0 = []
        subset = []
        reader.next()                               # advancing the reader to next row to avoid the column names
        for row in reader :
            subset0 = []
            subset0.append(int(row[index1]))        # appending the x-coordinate of the selected row(input by user)
            subset0.append(int(row[index2]))        # appending the y-coordinate of the selected row(input by user)
            subset.append(tuple(subset0))           # appending the tuple of x,y in the subset named list
    subset2 = [str(list(i)) for i in subset]        # making every list in subset as a string
    no_question_marks = '?,'*len(row1)              # calculating the number of question mark characters(no. of columns in the table) to be included in the string
    no_question_marks = no_question_marks[0:len(no_question_marks) - 1]# execute the muliple INSERT into TABLE queries using cursorobject.executemany(query)
    cur.executemany("INSERT into %s values(%s);" % (table_name, no_question_marks), to_db)
    conn.commit()

    output = str(label)
    output = output.replace("[", "")                # string formatting to make output as string to be written in the latex script
    output = output.replace("]", "")
    output = output.replace("{", " ")
    output = output.replace("}", "")
    output = output.replace(" ", "")
    output = output.replace("'", "")
    output = output.replace(":", "={")
    conv = list(output)
    del conv[0]
    conv_copy = []
    for i in range(0, len(conv)) :
        if conv[i] is "u" :
            if conv[i - 1] is "{" or conv[i - 1] is "," :
                continue
            else :
                conv_copy.insert(i, conv[i])
        else :
            conv_copy.insert(i, conv[i])
    conv = conv_copy
    output = ''.join(conv)
    temp = list(output)
    count = 0
    check = 0
    for i in temp :                                 # finally modifying temp list such that to have every entered "name" string by user as {name = {mark = %s, %s(color)}}
        if i == ',' :
            count = count + 1
        if count % 2 == 0 and count != 0 and i == ',':
            j = i.replace(",", "},")
            temp[check] = j
        check = check + 1
    temp.append('}')
    output = ''.join(temp)                          # final output string is the format : {a={mark=square*,blue}, # b={mark=triangle*,red}, # c={mark=o,draw=black}}
    string = ''.join(subset2)                       # convert the string in new list
    new = list(string)
    for i in range(0, len(new)) :
        if new[i] == '[' :
            new[i] = '('
        if new[i] == ']' :
            new[i] = ')'
        if new[i] == ' ' :
            new[i] = ''
    coordinates = ''.join(new)                      # replace '[', ']' characters with '(', ')' to make the coordinates string as required in the latex script
    coordinates1 = coordinates.replace("(", "")
    coordinates1 = coordinates1.replace(")", " \n")
    coordinates1 = coordinates1.replace(",", " ")   # final formatting the string to replace '(' with null string and ')' with next line character

    temp = list(coordinates1)
    del temp[len(temp) - 1]
    coordinates1 = ''.join(temp)                    # get the final coordinates string by last garbage value from the coordinates1 list

    s = ""
    for i in coordinates1.split("\n") :             # appending the list to store the name of label and its color with mark in final form
        color_of_mark = choices[call_scatter][coordinates1.split("\n").index(i)]
        i = i + color_of_mark
        s = s + i + "\n"

    temp = list(s)
    del temp[len(temp) - 1]                         # delete first garbage value
    s = ''.join(temp)

    add_plot = '''\\addplot[scatter,only marks,scatter src=explicit symbolic]
	               table[meta=label] {
                   x     y    label
                   %s
	               };
               ''' % (s)

    legend_list = []
    add_legendary = "\\addlegendentry{$%s$}\n"*label_count[call_scatter]
    for i in label_name[call_scatter] :
        legend_list.append(i)
    temp = ''.join(legend_list)
    temp.replace("u", "")
    temp_list = list(temp)
    legend_tuple = tuple(legend_list)
    final_legends = add_legendary % legend_tuple

    '''if(call_scatter > 0) :
        temp = open("latex.txt", "r")
        counter = temp.readlines()
        temp.close()

        len_file = len(counter)
        counter.insert(len_file - 3, add_plot)

        temp = open("latex.txt", "w")
        string = ''.join(counter)
        temp.write(string)
        temp.close()'''

    if(call_scatter == 0) :                         # writing the script for scatter_plot for latex file with several inputs inputed by the user formatted with the string laterly
        string = '''\\begin{tikzpicture}
	                \\begin{axis}[
	                clickable coords={(xy): \\thisrow{label}},
	                scatter/classes={
	                    %s}
                        ]
                        %s
	                  %s
	                \end{axis}
                    \end{tikzpicture}''' % (output, final_legends, add_plot)

        script.write(string)                        # write the final formatted string for the scatter plot in the latex script

#******************************************************************************#
def bar_chart() :

    script.seek(0, 2)                               # set the position pointer at the end of the file offset by 0 characters
    if(len(xcolm_bar[call_bar])) > 1 :
        for ix in range(0, len(xcolm_bar[call_bar])) :
            xcol = xcolm_bar[call_bar][ix]          # asking the user to enter the column name if csv file for x-coordinate column
            ycol = ycolm_bar[call_bar][ix]          # asking the user to enter the column name if csv file for y-coordinate column
            index1 = heading.index(xcol)            # storing the heading of both x and y columns in index1 and index2 variables
            index2 = heading.index(ycol)

            with open('sample.csv', 'r') as f:      # open the csv file as f
                reader = csv.reader(f)              # read rows into a dictionary format row
                subset0 = []
                subset = []
                reader.next()                       # advancing the reader to next row to avoid the column names
                for row in reader :
                    subset0 = []
                    subset0.append(int(row[index1]))# appending the x-coordinate of the selected row(input by user)
                    subset0.append(int(row[index2]))# appending the y-coordinate of the selected row(input by user)
                    subset.append(tuple(subset0))   # appending the tuple of x,y in the subset named list
            subset2 = [str(list(u)) for u in subset]# making every list in subset as a string
            no_question_marks = '?,'*len(row1)      # calculating the number of question mark characters(no. of columns in the table) to be included in the string
            no_question_marks = no_question_marks[0:len(no_question_marks) - 1]
            # execute the muliple INSERT into TABLE queries using cursor_object.executemany(query)
            cur.executemany("INSERT into %s values(%s);" % (table_name, no_question_marks), to_db)
            conn.commit()                           # commit the changes done in the data base(after extracting data from the csv file)


            string = ''.join(subset2)               # subset2 is the list containing the x and y coordinates for each column in the form [(x1,y1), (x2,y2),....]
            new = list(string)
            for i in range(0, len(new)) :
                if new[i] == '[' :
                    new[i] = '('
                if new[i] == ']' :
                    new[i] = ')'
                if new[i] == ' ' :
                    new[i] = ''
            coordinates = ''.join(new)
            coordinates = coordinates + "(14,14)";
            script.seek(0,2)
            add_plot = '''\\addplot
                       coordinates {
                       %s
                       };
                       ''' % (coordinates)

            if ix is 0 :                            # writing the script for bar_plot for latex file with several inputs inputed by the user formatted with the string laterly
                string = '''
                            \\begin{tikzpicture}
                            \\begin{axis}[
                            x tick label style={/pgf/number format/1000 sep=},
                            ylabel=%s,
                            xlabel=%s,
                            enlargelimits = %f,
                            legend style={at={(%f,%f)},	anchor=%s, legend columns=-1},
                            ybar interval=%f,
                            title={%s}
                            ]
                            %s
                            \legend{}
                            \end{axis}
                            \end{tikzpicture}''' % (y_label[call_bar], x_label[call_bar], space_bars[call_bar], xlegend[call_bar], ylegend[call_bar], anchor_pos[call_bar], bar_interval[call_bar], title_bar[call_bar], add_plot)
                script.write(string)                # write the final formatted string in the latex script for the bar plots

            else :
                temp = open("latex.txt", "r")
                counter = temp.readlines()

                add_legend = ""
                for j in legend[call_bar] :
                    add_legend = add_legend + j + ","
                t = list(add_legend)
                del t[len(add_legend) - 1]
                add_legend = ''.join(t)
                for i in counter :
                    if i == '                            \\legend{}\n' :
                        change = "\\legend{%s}\n" % (add_legend)
                        counter[counter.index(i)] = change
                temp.close()

                len_file = len(counter)
                counter.insert(len_file - 4, add_plot)

                temp = open("latex.txt", "w")
                string = ''.join(counter)
                temp.write(string)
                temp.close()
    else :
        #if isinstance(file_data["xcolumn"], list) is True :
        xcol = xcolm_bar[call_bar][0][0]            # asking the user to enter the column name if csv file for x-coordinate column
        ycol = ycolm_bar[call_bar][0][0]            # asking the user to enter the column name if csv file for y-coordinate column
        if(xcol != 0) :
            index1 = heading.index(xcol)            # storing the heading of both x and y columns in index1 and index2 variables
            index2 = heading.index(ycol)

        if xcol == 0 :                              #query excecution
            minm = []
            xcor = []
            for r in Queries :
                index = Queries.index(r) + 1
                cur.execute(r)
                temp = cur.fetchall()
                put = temp[0][0]
                minm.append(put)
                xcor.append(index)
            sup = []
            for v in range(0, len(minm)) :
                temp = []
                temp.append(xcor[v])
                temp.append(minm[v])
                qrs = str(temp)
                sup.append(qrs)
            conn.commit()                           # commit the changes done in the data base(after extracting data from the csv file)
            string = ''.join(sup)                   # subset2 is the list containing the x and y coordinates for each column in the form [(x1,y1), (x2,y2),....]
            new = list(string)
            for i in range(0, len(new)) :
                if new[i] == '[' :
                    new[i] = '('
                if new[i] == ']' :
                    new[i] = ')'
                if new[i] == ' ' :
                    new[i] = ''

            qcords = ''.join(new)
            dum = "(5,5)"
            qcords = qcords + dum
            script.seek(0,2)
            add_plot = '''\\addplot
                       coordinates {
                       %s
                       };
                       ''' % (qcords)
            string = '''
                        \\begin{tikzpicture}
                        \\begin{axis}[
                        x tick label style={/pgf/number format/1000 sep=},
                        ylabel=%s,
                        xlabel=%s,
                        enlargelimits = %f,
                        legend style={at={(%f,%f)},	anchor=%s, legend columns=-1},
                        ybar interval=%f,
                        title={%s}
                        ]
                        %s
                        \legend{%s}
                        \end{axis}
                        \end{tikzpicture}''' % (y_label[call_bar], x_label[call_bar], space_bars[call_bar], xlegend[call_bar], ylegend[call_bar], anchor_pos[call_bar], bar_interval[call_bar], title_bar[call_bar], add_plot, legend[call_bar][0])
            script.write(string)                    # write the final formatted string in the latex script for the bar plots
        else :
            with open('sample.csv', 'r') as f:          # open the csv file as f
                reader = csv.reader(f)                  # read rows into a dictionary format row
                subset0 = []
                subset = []
                reader.next()                           # advancing the reader to next row to avoid the column names
                for row in reader :
                    subset0 = []
                    subset0.append(int(row[index1]))    # appending the x-coordinate of the selected row(input by user)
                    subset0.append(int(row[index2]))    # appending the y-coordinate of the selected row(input by user)
                    subset.append(tuple(subset0))       # appending the tuple of x,y in the subset named list
            subset2 = [str(list(u)) for u in subset]    # making every list in subset as a string
            no_question_marks = '?,'*len(row1)          # calculating the number of question mark characters(no. of columns in the table) to be included in the string
            no_question_marks = no_question_marks[0:len(no_question_marks) - 1]
            # execute the muliple INSERT into TABLE queries using cursor_object.executemany(query)
            cur.executemany("INSERT into %s values(%s);" % (table_name, no_question_marks), to_db)

            conn.commit()                               # commit the changes done in the data base(after extracting data from the csv file)

            string = ''.join(subset2)                   # subset2 is the list containing the x and y coordinates for each column in the form [(x1,y1), (x2,y2),....]
            new = list(string)
            for i in range(0, len(new)) :
                if new[i] == '[' :
                    new[i] = '('
                if new[i] == ']' :
                    new[i] = ')'
                if new[i] == ' ' :
                    new[i] = ''
            coordinates = ''.join(new)
            coordinates = coordinates + "(14,14)"
            script.seek(0,2)
            add_plot = '''\\addplot
                          coordinates {
                          %s
                          };
                       ''' % (coordinates)
            string = '''
                    \\begin{tikzpicture}
                    \\begin{axis}[
                    x tick label style={/pgf/number format/1000 sep=},
                    ylabel=%s,
                    xlabel=%s,
                    enlargelimits = %f,
                    legend style={at={(%f,%f)},	anchor=%s, legend columns=-1},
                    ybar interval=%f,
                    title={%s}
                    ]
                    %s
                    \legend{%s}
                    \end{axis}
                    \end{tikzpicture}''' % (y_label[call_bar], x_label[call_bar], space_bars[call_bar], xlegend[call_bar], ylegend[call_bar], anchor_pos[call_bar], bar_interval[call_bar], title_bar[call_bar], add_plot, legend[call_bar][0])
            script.write(string)                        # write the final formatted string in the latex script for the bar plots
#******************************************************************************#

def a() :
    line_plot()

def b() :
    scatter_plot()

def c() :
    bar_chart()

def choose(input_dict, which_plot) :
    return input_dict.get(which_plot)

count = 0
call_line = -1
call_scatter = -1
call_bar = -1
print
print '********************************************************************************'
print 'I have detected %d Line-Plot(s), %d Scatter-Plot(s) and %d Bar-Plot(s) in Your JSONFile. Have a look at your corresponding Graphs.' % (user_guide["line"], user_guide["scatter"], user_guide["bar"])
print '********************************************************************************'
print
while(count < user_guide["line"] + user_guide["scatter"] + user_guide["bar"]) :
    to_db = []                                      # initialize the the to_db list to store the tuples of x and y cords
    with open('sample.csv', 'r') as f:              # open the csv file as f
        reader = csv.reader(f)                      # read rows into a dictionary format
        i = 0
        for row in reader :                         # read a row as {column1: value1, column2: value2,...}
            if i == 0 :
                heading = row
            if i is not 0 :
                row = [int(k) for k in row]
            i = i + 1
            to_db.append(tuple(row))                # append the tuple of column and its corresponding value
        del to_db[0]                                # remove the first name tuple from the to_db list

    input_dict = {1 : a, 2 : b, 3 : c}

    which_plot = automatic_input[count - 1]
    if(which_plot == 1 or which_plot == 2 or which_plot == 3) :
        count = count + 1
        if(which_plot == 1) :
            if(call_scatter > -1 or call_bar > -1) :
                script.seek(0, 2)
                script.write("\n\t\t\t\t\t\t\t\t\t\t\t\hskip 5pt\n")
            call_line = call_line + 1
        elif(which_plot == 2) :
            if(call_line > -1 or call_bar > -1) :
                script.seek(0, 2)
                script.write("\n\t\t\t\t\t\t\t\t\t\t\t\hskip 5pt\n")
            call_scatter = call_scatter + 1
        elif(which_plot == 3) :
            if(call_scatter > -1 or call_line > -1) :
                script.seek(0, 2)
                script.write("\n\t\t\t\t\t\t\t\t\t\t\t\hskip 5pt\n")
            call_bar = call_bar + 1
        result = choose(input_dict, which_plot)()

script.seek(0, 2)
script.write("\n\end{document}\n")                  # set the position pointer at the end of the string offset by zero characters and write the final line of the general latex script
