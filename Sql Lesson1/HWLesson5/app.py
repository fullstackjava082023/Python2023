from flask import Flask, render_template, request, redirect


app = Flask(__name__)

# list, set , dictionary, tuple
contacts_list = [
				{
					'number': 1,
					'name': 'Arja Stark',
					'phone': '044545',
					'email': 'Valan.Margulis@Winterfel.com',
					'photo': 'arya-stark.jpg',
                    'gender': 'Female'
				},
				{
                    'number': 2,
                    'name': 'Jon Snow',
                    'phone': '045456465',
                    'email': 'Night.Watch@Wall.com',
                    'photo': 'jon-snow.jpg',
                    'gender': 'Male'
				},
                {
                    'number': 3,
                    'name': 'Ned Stark',
                    'phone': '04545',
                    'email': 'Ned@WF.com',
                    'photo': 'ned-stark.jpg',
                    'gender': 'Male'
                },
                 {
                    'number': 4,
                    'name': 'Hodor',
                    'phone': 'hodor',
                    'email': 'hodor@hodor.com',
                    'photo': 'hodor.jpg',
                    'gender': 'Male'
                }
                ]


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/addContact', methods=['GET', 'POST'])
def addContact():
    return render_template('addContactForm.html')



@app.route('/viewContacts')
def viewContacts():
    return render_template('index.html', contacts=contacts_list)


@app.route('/createContact', methods=['POST'])
def createContact():
    # adding additional contact to the database (contacts_list)
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']   
    gender = request.form['gender']
    photo = request.files['photo']
    # create a name for the file to be saved
    file_path = 'HWLesson5/static/images/' + fullname + '.jpg'
    # save the file in the server
    photo.save(file_path)
    # create a new contact
    new_contact =  {
                'number': len(contacts_list) + 1,
                'name': fullname,
                'phone': phone,
                'email': email,
                'gender': gender,
                'photo': fullname + '.jpg'
            }
    # add new contact to the list (database)
    contacts_list.append(new_contact)
    return redirect('/viewContacts')


if __name__ == '__main__':
    app.run(debug=True)