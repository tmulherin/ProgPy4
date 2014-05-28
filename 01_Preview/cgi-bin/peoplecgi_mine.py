#!c:\Python\python.exe
"""
    Implement a wev-based interface for viewing and updating class instances
    stored in a shelve that lives on the server (same machine if localhost)
"""

import cgi, shelve, sys, os                      # cgi.test() dumps inputs
shelvename = 'people-class-shelve'               # shelve files are in current working directory
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage                          # parse form data
print('Content-type: text/html')                 # hdr, blank line is in replyhtml
sys.path.insert(0, os.getcwd())                  # so this and pickler can find person 

#==> main html template
replyhtml = """
<!DOCTYPE html>
<html lang="en-us">
    <head>
        <meta charset="UTF-8" />
        <title>People Input Form</title>
    </head>
<body>
    <form method=POST action="peoplecgi.py">
        <table>
           <tr><th>key</th><td><input type="text" name="key" value="%(key)s" /></td>
           $ROWS$
        </table>
        <p>
            <input type="submit" value="fetch", name="action"
            <input type="submit" value="Update", name="action"
        </p>
    </form
</html>
"""

#==> insert html for data rows at $ROWS$
rowhtml = '<tr><th>%s</th><td><input type="text" name="%s" value="%%(%s)" /></td></tr>\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))

replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(aDict):
    new = aDict.copy()
    for field in fieldnames:                     # values may have '&', '>', etc.
        value = new[field]                       # display as code: quoted
        new[field] = cgi.escape(repr(value))     # html-escape special characters
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]                         
        fields = record.__dict__                 # use attribute dict
        fields['key'] = key                      # to fill reply string
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]                     # update existing record
        else:
            from person import Person            # make/store new one for key
            record = Person(name='?', age='?')   # eval: strings must be quoted

        for field in fieldnames:
            setattr(record, field, eval(form[field].value))

        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields

db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')      # bad submit button value
    fields['key'] = 'Missing or invalid action!'

db.close()
print(replyhtml % htmlize(fields))               # fill reply from dict