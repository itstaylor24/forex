### Conceptual Exercise

1. **Question:** What are important differences between Python and JavaScript?
   **Answer:** Python is is a programming language used for back-end developent, while Javascript is used mainly for front-end.

2. **Question:** Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
   can try to get a missing key (like "c") _without_ your programming
   crashing. **Answer:** You could use a condition statement to check if the the key is in the dictionary or you could use .get.

using get: `dict = {"a": 1, "b": 2}
val_of_c = dict.get("c")
print(val_of_c)`

using conditional: `dict = {"a": 1, "b": 2}
if "c" in my_dict:
    val_of_c = dict["c"]
    print(val_of_c)
else:
    print("Key of 'c' not present ")`

3. **Question:** What is a unit test?
   **Answe:r** A unit test tests small components of an application—usually just individually functions or methods. They are useful because the fix bugs early on in the application.

4. **Question:** What is an integration test? **Answer:**
   An integration tests how a process is executed in an application and usually tests how different processes work together. For example, redirects, or testing whether form data is submitted and how that data is then displayed on a webpage.

5. **Question:** What is the role of web application framework, like Flask? **Answer:** It makes it easier to create different view functions for url routes. It helps in the creation of different, dynamic, HTML templates for websites and webpages. It makes it easier for the server to handle different client requests.

6. **Question:** You can pass information to Flask either as a parameter in a route URL
   (like `'/foods/pretzel'`) or using a URL query param (like
   `'foods?type=pretzel'`). How might you choose which one is a better fit
   for an application? **Answer:** If you are passing information as a parameter in a route URL it is typically information that is essential or feels more like the subject of the page, while a query parameter is more like additional information commonly used for things like sorting and modifying.

7. **Question:** How do you collect data from a URL placeholder parameter using Flask?

**Answer:** (Here is an example)

from flask import Flask

app = Flask(**name**)

@app.route('/dog/<breed>')
def show_breed(breed):
return f'Here is a pict of a {breed}'

Above, in the route decorator we added the placeholder param between two lesser than and greater than symbols, then in the funcion, we used the placeholder as the argument.

8. **Question:** How do you collect data from the query string using Flask? **Answer:** (here is an example)

from flask import Flask, request

app = Flask(**name**)

@app.route('/age')
def state_age():
how_old = request.args.get('years', '')  
 return f'You are {how_old} years old'

Above, we use the request object, which handles incoming request query string data. We take info from the query string.

If our URL is /age?years=nine, the value 'nine' will be returned in the function

9. **Question:** How do you collect data from the body of the request using Flask? **Answer:** We can collect data from the body of a request object using a form, for example. (Here is an example)

@app.route('/submit', methods=['POST'])
def submit():
username = request.form['username']

    return f'Welcome, {username}'

    Above w collect data from a form by using the form method on the request object. We select the form input with the name 'username' and then return a string using the value of that input.

10. **Question** What is a cookie and what kinds of things are they commonly used for? **Answer** a cookie is a string of information stored on a specific browser. It is used to store information about a user. It is commonly used by advertisers and websites to keep unique info on the user. They can store things like user preferences, online shopping cart info, pages visited, videos or stories the user hovered over, etc. They may also keep track of user info across different browsers.

11. **Question:** What is the session object in Flask?
    **Answer:** The Flask session object is like a 'magic dictionary' that works with cookies in the browswer. The info stored in the session object do not have to be just strings--the type is preserved. They are signed so that the user of the the browser cannot modify them

12. **Question:** What does Flask's `jsonify()` do? **Answer:** It allows us to export JSON files with Flask instead of just text. We do this when we want to create an API. It changes the content-type header in the response to JSON. In the flask app, it changes any JSON serializable data type to application/JSON--such as a dictionary or list.
